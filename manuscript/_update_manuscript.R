library(readr)
library(stringr)
library(cli)
library(purrr)

temp_manuscript <- tempfile()
dest_manuscript <- "manuscript/index.qmd"
dest_library <- "manuscript/library.bib"

if (FALSE) {
  library(googledrive)
  library(textreadr)

  # httr::set_config(httr::config(http_version = 0)) # avoid http2 framing layer bug
  drive <- drive_download(
    as_id("1FqmINEd4miXlXvIR2JLZhu2n8AIU_5h3gc_5QoCmRsQ"),
    type = "docx",
    overwrite = TRUE,
    path = temp_manuscript
  )

  # read docx
  doc <- officer::read_docx(drive$local_path)
  content <- officer::docx_summary(doc)
  
  content$text %>%
    # add spaces before citations
    # str_replace_all("([^ ])(\\[@[^\\]]*\\])", "\\1 \\2") %>% 
    # add newlines before sections
    str_replace_all("^#", "\n#")# %>%
    #write_lines(dest_manuscript)
}

# convert references
d2b <- reticulate::import("doi2bib")

manu <- read_lines(dest_manuscript) %>% paste(collapse = "\n")

# extract citation yaml
citations_yaml <- gsub("```\\{yaml[^\\}]*\\}\n(citations:[^`]*)```", "\\1", manu)
citations <- yaml::read_yaml(text = citations_yaml)$citations

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

write_lines(bibs, dest_library)
