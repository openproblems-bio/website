## OpenProblems.bio

This repository is used to build [openproblems.bio](https://openproblems.bio).

## Installation

* Install [quarto](https://quarto.org) v1.3, R v4.2 and Python v3.10.

* Run `Rscript -e 'install.packages("renv")'` if you don't have `{renv}` installed.

* Run `Rscript -e 'renv::restore()'` to install R and Python packages recorded in the renv lockfile (`renv.lock`) and Python requirements (`requirements.txt`).
  This might take a while.

## Preview

Run `quarto preview` to render a preview version of the site.

## Build

Run `quarto render` to render the site.

