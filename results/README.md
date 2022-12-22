# Results

Each task contains an `index.qmd` file which reads the JSON files in `data/` and renders some plots and tables.

If you want to make changes to the way these results are rendered, you can edit and run parts of the template 
(located at `results/_template_index.qmd`). When you feel happy with the new template, run 
`Rscript results/_generate_pages.R` to update the task-specific `index.qmd` files.