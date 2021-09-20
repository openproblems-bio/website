---
title: "Frequently Asked Questions"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 100
---

Here are a list of common questions and answers related to the competition

## What if I only want to compete for one of the prizes in a task?

As described in the Tasks documentation, each task has up to five prizes. However, competitors need not compete for all prizes in a task. In Task 1 - Modality Prediction, for example, a competitor may compete on the subtask of predicting RNA from ATAC measurements. In this case, a submitted method may simply exit without writing a submission to disk.

## How can I upload a pre-trained model?
Competitors may submit pre-trained models for any of the tasks in the competition. Model parameters may included in the submission directory. They can be then made accessible to the submission script by editing the `config.vsh.yaml` file to list the parameter file under the `resources` section.

For example if you'd like to add a file containing model weights with the filename `weights.pt`, edit the resources block to look like the following:
```yaml
resources:
  # Script containing method
  - type: python_script
    path: script.py
  # Model weights file
  - type: file
    path: weights.pt
```
The model parameter file will now be accessible to the script in the working directory. This could be accessed, for example, by running `torch.load("./weights.pt")`.

For more information, see [Updating the Configuration](neurips_docs/submission/starter_kit_contents/#updating-the-configuration).

## Can I pre-train on public data?

Pre-training on public data is allowed. We've already compiled a large number of public datasets [here](https://github.com/openproblems-bio/neurips2021_multimodal_viash/tree/main/src/common/datasets). Note, these datasets are not all filtered, preprocessed, and annotated in the same way as the competition training and test data. We have no prior expectation about whether including public data will or will not improve performance on the in house test data. Use of public data is at the competitors risk.

## Why am I seeing "Process terminated with an error exit status (137)" when I generate a submission?

Exit code 137 is the SIGKILL out of memory error. It means one of the processed in the submission script ran out of memory. One common cause of is the default memory constraint for Docker Desktop is 2GB. If you're using Docker Desktop, you can edit the [Resources Configuration](https://docs.docker.com/desktop/mac/#resources).

If this isn't the issue, your script might be using too much memory and getting killed by your kernel. To limit the memory used by your script, try deleting unused variables or working with sparse matrix formats.

## How are the libraries in `config.vsh.yaml` installed?

If you'd like to see how the viash docker image is built, run `bin/viash run -- ---dockerfile`. Here's an example from the predict modality starter kit.

```sh
> bin/viash run -- ---dockerfile

FROM dataintuitive/randpy:py3.8

RUN pip install --upgrade pip && \
  pip install --no-cache-dir "scikit-learn" "anndata" "scanpy"
```

Here you can see the base Docker image is https://hub.docker.com/r/dataintuitive/randpy at the [py3.8](https://hub.docker.com/layers/dataintuitive/randpy/py3.8/images/sha256-21c7d4fb8ecf787040590b62753fb1439022e706800cde110f7d20c1fdccaab3?context=explore) tag.

## How can I increase the memory/CPU/runtime limits of my method?

The resource use of the submission components is set through the `config.vsh.yaml` file available in the starter kits.

```yaml
# By specifying a 'nextflow', viash will also build a viash module
# which uses the docker container built above to also be able to
# run your method as part of a nextflow pipeline.
- type: nextflow
  labels: [ lowmem, lowtime, lowcpu ]
```

Available options are `[low|med|high]` for each of `mem`, `time`, and `cpu`. The corresponding resource values can be found in the `scripts/nextflow.config` file.
