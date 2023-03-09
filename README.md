## Experimental website repository

This is a repository for hosting experimental website designs.

## Installation

* Install [quarto](https://quarto.org) v1.2, R v4.2 and Python v3.10.

* Run `Rscript -e 'install.packages("renv")'` if you don't have `{renv}` installed.

* Run `Rscript -e 'renv::restore()'` to install R and Python packages recorded in the renv lockfile (`renv.lock`) and Python requirements (`requirements.txt`).
  This might take a while.

## Preview

Run `quarto preview` to render a preview version of the site.

## Build

Run `quarto render` to render the site.

## Helper scripts

* Run `Rscript results/_generate_pages.R` to generate the `index.qmd` pages for all subtasks.

* Run `Rscript manuscript/_update_manuscript.R` to fetch the latest version of the manuscript from Google Drive and generate the corresponding `index.qmd`.

## Update results manually

This is normally done through a GitHub action. In case it isn't, do the following:

* Download a `results.zip` from the OpenProblems GitHub Action named [Process Nextflow results](https://github.com/openproblems-bio/openproblems/actions/workflows/process_results.yml) and extract in the `results/` folder. 
