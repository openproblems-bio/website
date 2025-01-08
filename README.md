# OpenProblems.bio

This repository is used to build [openproblems.bio](https://openproblems.bio).

## Installation

* Install [quarto](https://quarto.org) v1.4.527, R >= 4.3 and Python >= 3.10.

* Clone this repo with `git clone --recursive git@github.com:openproblems-bio/website.git`

* Run `Rscript -e 'install.packages("renv")'` if you don't have `{renv}` installed.

* Run `Rscript -e 'renv::restore()'` to install R and Python packages recorded in the renv lockfile (`renv.lock`) and Python requirements (`requirements.txt`).
  This might take a while.

If contributing to the documentation, install Java, Docker and Viash (See [Requirements](https://openproblems.bio/documentation/fundamentals/requirements)).

## Preview

Run `quarto preview` to render a preview version of the site.

To reduce the time it takes to render the site, quarto is set to not execute runnable code by default. As such, some content may be missing -- mostly the output of code blocks. Use `quarto preview --profile evaluate_code` to evaluate runnable code blocks. 

Tip: When you already did a render or preview with or without the profile argument, you need to remove the `_site` and `_freeze` directories to see a change by executing `rm -r _site _freeze`

## Build

Run `quarto render --profile evaluate_code` to render the site.

## License

This repository contains a Quarto website with different types of content:

- Markdown content and JSON data files are licensed under the Creative Commons Attribution 4.0 International License (CC-BY). See [`LICENSE-CC-BY`](./LICENSE-CC-BY) for details.

- All other source files (e.g. R, Python, CSS, SCSS, and EJS) are licensed under the MIT License. See [`LICENSE-MIT`](./LICENSE-MIT) for details.
