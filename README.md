# OpenProblems.bio

This repository is used to build [openproblems.bio](https://openproblems.bio).

## Installation

* Install [quarto](https://quarto.org) v1.2, R v4.2 and Python v3.10.

* Run `Rscript -e 'install.packages("renv")'` if you don't have `{renv}` installed.

* Run `Rscript -e 'renv::restore()'` to install R and Python packages recorded in the renv lockfile (`renv.lock`) and Python requirements (`requirements.txt`).
  This might take a while.

## Preview

Run `quarto preview` to render a preview version of the site.

## Build

Run `quarto render` to render the site.

## License

This repository contains a Quarto website with different types of content:

- Markdown content and JSON data files are licensed under the Creative Commons Attribution 4.0 International License (CC-BY). See [`LICENSE-CC-BY`](./LICENSE-CC-BY) for details.
- All other source files (e.g. R, Python, CSS, SCSS, and EJS) are licensed under the MIT License. See [`LICENSE-MIT`](./LICENSE-MIT) for details.
