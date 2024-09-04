# OpenProblems.bio

This repository is used to build [openproblems.bio](https://openproblems.bio).

## Installation

* Install [quarto](https://quarto.org) v1.3, R v4.2 and Python v3.10.

* Clone this repo with `git clone --recursive git@github.com:openproblems-bio/website.git`

* Run `Rscript -e 'install.packages("renv")'` if you don't have `{renv}` installed.

* Run `Rscript -e 'renv::restore()'` to install R and Python packages recorded in the renv lockfile (`renv.lock`) and Python requirements (`requirements.txt`).
  This might take a while.

If contributing to the documentation:

* Install Oracle Java >=11 or OpenJDK >=11

* Install Docker

* Install Viash:

```bash
mkdir -p "$HOME/.local/bin"

curl -fsSL get.viash.io | bash -s -- --bin "$HOME/.local/bin"
```

Tip: Make sure that the $HOME/.local/bin folder is in your $PATH variable.

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