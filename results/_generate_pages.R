library(tidyverse)

# where tof ind this data in openproblems?
task_info <- tibble(
  id = c(
    "batch_integration_embed",
    "batch_integration_feature",
    "batch_integration_graph",
    "cell_cell_communication_ligand_target",
    "cell_cell_communication_source_target",
    "denoising",
    "dimensionality_reduction",
    "label_projection",
    "multimodal_data_integration",
    "regulatory_effect_prediction",
    "spatial_decomposition"
  ),
  name = c(
    "Batch integration embed",
    "Batch integration feature",
    "Batch integration graph",
    "Cell-Cell Communication Inference (Ligand-Target)",
    "Cell-Cell Communication Inference (Source-Target)",
    "Denoising",
    "Dimensionality reduction for visualisation",
    "Label Projection",
    "Multimodal Data Integration",
    "Regulatory effect prediction",
    "Spatial Decomposition"
  ),
  description = c(
    "Removing batch effects while preserving biological variation (embedding output)",
    "Removing batch effects while preserving biological variation (feature output)",
    "Removing batch effects while preserving biological variation (graph output)",
    "Detect interactions between ligands and target cell types",
    "Detect interactions between source and target cell types",
    "Removing noise in sparse single-cell RNA-sequencing count data",
    "Reduction of high-dimensional datasets to 2D for visualization & interpretation",
    "Automated cell type annotation from rich, labeled reference data",
    "Alignment of cellular profiles from two different modalities",
    "...",
    "Calling cell-type compositions for spot-based spatial transcriptomics data"
  )
)

template <- readr::read_lines("results/_template.qmd") %>%
  paste0(collapse = "\n") %>%
  gsub("```\\{r noninteractive\\}[^`]+```", "", .)

pwalk(task_info, function(id, name, description) {
  newlines <- glue::glue("---
title: {name}
engine: knitr
image: thumbnail.png
---

```{{r noninteractive}}
#| include: FALSE
path <- '.'
task_id <- '{id}'
```
")

  readr::write_lines(c(newlines, template), paste0("results/", id, "/index.qmd"))
})