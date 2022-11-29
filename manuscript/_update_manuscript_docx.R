library(readr)
library(stringr)
library(cli)
library(purrr)
library(googledrive)
d2b <- reticulate::import("doi2bib")

cli::cli_alert("google drive authentication")
zip_file <- fs::path_wd("manuscript/auth_token.zip")
auth_file <- paste0(Sys.getenv("HOME"), "/.cache/gargle/134f22af3ae3a9f0b7f0eb57dd61916f_", Sys.getenv("GOOGLE_DRIVE_EMAIL"))

# zip_file created with:
#   processx::run(
#     "zip",
#     args = c(zip_file, basename(auth_file), "--password", Sys.getenv("GOOGLE_DRIVE_PASSWORD")),
#     wd = dirname(auth_file)
#   )

if (is.null(Sys.getenv("GOOGLE_DRIVE_EMAIL"))) {
  stop("Need the email to authenticate")
}

if (!file.exists(auth_file)) {
  if (is.null(Sys.getenv("GOOGLE_DRIVE_PASSWORD"))) {
    stop("Need the password to unzip")
  }
  dir.create(dirname(auth_file), recursive = TRUE, showWarnings = FALSE)
  processx::run("unzip", c("-D", "-P", Sys.getenv("GOOGLE_DRIVE_PASSWORD"), zip_file), wd = dirname(auth_file))
}

googledrive::drive_auth(email = Sys.getenv("GOOGLE_DRIVE_EMAIL"), path = auth_file)

cli::cli_alert("download manuscript from gdrive")
temp_manuscript <- tempfile()
dest_manuscript <- "manuscript/index.qmd"

drive <- drive_download(
  as_id("1FqmINEd4miXlXvIR2JLZhu2n8AIU_5h3gc_5QoCmRsQ"),
  type = "docx",
  overwrite = TRUE,
  path = temp_manuscript
)

cli::cli_alert("read docx and write to qmd")
content <- processx::run("pandoc", c("--from=docx", "--to=markdown", drive$local_path))$stdout


content %>%
  str_replace_all("\\[([^\\]]*)\\]\\(https?://paperpile.com/[^\\)]*\\)", "\\1") %>%
  write_lines(dest_manuscript)
