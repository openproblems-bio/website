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
dest_library <- "manuscript/library.bib"

drive <- drive_download(
  as_id("1gcfToxQ5cVgHfQ5Z6M0mbaCzUISEC-CQt352CXvP4s4"),
  type = "docx",
  overwrite = TRUE,
  path = temp_manuscript
)

cli::cli_alert("read docx and write to qmd")
doc <- officer::read_docx(drive$local_path)
content <- officer::docx_summary(doc)

content$text %>%
  # add spaces before citations
  # str_replace_all("([^ ])(\\[@[^\\]]*\\])", "\\1 \\2") %>% 
  # add newlines before sections
  str_replace_all("^#", "\n#") %>%
  write_lines(dest_manuscript)


cli::cli_alert("extract citation yaml")
manu_txt <- read_lines(dest_manuscript) %>% paste(collapse = "\n")
citations_yaml <- gsub(".*```\\{citations[^\n]*\n([^`]*)```.*", "\\1", manu_txt)
citations <- yaml::read_yaml(text = citations_yaml)$citations

cli::cli_alert("convert to bibtex")
bibs <- map2_chr(names(citations), citations, function(name, text) {
  bib <-
    if (grepl("^@", text)) {
      # text is already a bibtex
      text
    } else {
      out <- d2b$crossref$get_bib_from_doi(text)
      if (!out[[1]]) {
        cli::cli_alert_warning(paste0("Could not find doi '", text, "'"))
        ""
      } else {
        out[[2]]
      }
    }
  gsub("(@[a-zA-Z]+\\{)[A-Za-z0-9_-]+", paste0("\\1", name), bib)
})

cli::cli_alert("write library file")
write_lines(bibs, dest_library)
