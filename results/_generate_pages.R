library(tidyverse)

# where to find this data in openproblems?
task_info <- jsonlite::read_json("results/task_info.json", simplifyVector = TRUE)

index_template <- readr::read_lines("results/_template_index.qmd") %>%
  paste0(collapse = "\n") %>%
  gsub("```\\{r interactive\\}[^`]+```", "", .)

pwalk(task_info, function(id, name, description) {
  description <- gsub("\n", " ", description)
  newlines <- glue::glue("---
title: {name}
description: {description}
engine: knitr
image: thumbnail.png
---

```{{r noninteractive}}
#| include: FALSE
path <- '.'
task_id <- '{id}'
```
")

  readr::write_lines(c(newlines, index_template), paste0("results/", id, "/index.qmd"))
})
