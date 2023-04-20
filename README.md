## OpenProblems.bio

This repository is used to build [openproblems.bio](https://openproblems.bio).

## Installation

* Install [quarto](https://quarto.org) v1.2, R v4.2 and Python v3.10.

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

## Build

Run `quarto render --profile evaluate_code` to render the site.