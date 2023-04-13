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

### without documentation (Recommended)

Run `quarto preview --profile no_docs` to render a preview version of the site without documentation pages.

### with documentation

Run `quarto preview` to render a preview version of the site. This will take longer because of the codeblocks that are being evaluated.


## Build

Run `quarto render` to render the site.

Add `--profile no_docs` to not render the documentation if you have not installed the dependencies. This is __recommended__ if not working on the documentation

