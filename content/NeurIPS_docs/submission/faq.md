---
title: "Frequently Asked Questions"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 90
---

Here are a list of common questions and answers related to the competition

## What if I only want to compete for one of the prizes in a task?

As described in the Tasks documentation, each task has up to five prizes. However, competitors need not compete for all prizes in a task. In Task 1 - Modality Prediction, for example, a competitor may compete on the subtask of predicting RNA from ATAC measurements. In this case, a submitted method may simply exit without writing a submission to disk.


## Can I store helper functions as separate files?

Yes, though you'll need to let Viash know which additional files are required to run the component. If several helper functions are stored in an additional file `mymodule.py` or `mymodule.R`, use the following code to import helper functions:

### Python

In the functionality resources section in the config:

```yaml
resources:
  - type: python_script
    path: script.py
  - path: mymodule.py
```

In the main Python script:

```python
import sys

## VIASH START
meta = { 'resources_dir': '.' }
## VIASH END

sys.path.append(meta['resources_dir'])
from mymodule import helper_fun
```

### R


In the functionality resources section in the config:

```yaml
resources:
  - type: r_script
    path: script.R
  - path: mymodule.R
```

In the main R script:

```r
## VIASH START
meta <- list(resources_dir = ".")
## VIASH END

source(paste0(meta[["resources_dir"]], "/mymodule.R"))
helper_fun(...)
```

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

This file will now be made accessible to the script using the "resources directory". Youc an load the file as follows:

```python
## VIASH START
# ...
meta = { 'resources_dir': '.' }
## VIASH END

torch.load(meta['resources_dir'] + '/weights.pt')
```

For more information, see [Updating the Configuration](/neurips_docs/submission/starter_kit_contents/#updating-the-configuration).


## Can I pre-train on public data?

Pre-training on public data is allowed. We've already compiled a large number of public datasets [here](https://github.com/openproblems-bio/neurips2021_multimodal_viash/tree/main/src/common/datasets). Note, these datasets are not all filtered, preprocessed, and annotated in the same way as the competition training and test data. We have no prior expectation about whether including public data will or will not improve performance on the in house test data. Use of public data is at the competitors risk.


## How are the libraries in `config.vsh.yaml` installed?

If you'd like to see how the viash docker image is built, run `bin/viash run -- ---dockerfile`. Here's an example from the predict modality starter kit.

```sh
> bin/viash run -- ---dockerfile

FROM dataintuitive/randpy:py3.8

RUN pip install --upgrade pip && \
  pip install --no-cache-dir "scikit-learn" "anndata" "scanpy"
```

Here you can see the base Docker image is https://hub.docker.com/r/dataintuitive/randpy at the [py3.8](https://hub.docker.com/layers/dataintuitive/randpy/py3.8/images/sha256-21c7d4fb8ecf787040590b62753fb1439022e706800cde110f7d20c1fdccaab3?context=explore) tag.




## Error message "Process terminated with an error exit status (xxx)"

When running a Nextflow pipeline, it's possible your component might fail when running on one of multiple datasets. Here is an example output of a nextflow execution that failed:

```sh
$ ./scripts/2_generate_submission.sh

N E X T F L O W  ~  version 21.04.1
Pulling openproblems-bio/neurips2021_multimodal_viash ...
Launching `openproblems-bio/neurips2021_multimodal_viash` [small_montalcini] - revision: 24adec7995 [1.1.1]

...
[5f/5ff487] process > method:method_process (openproblems_bmmc_cite_phase1) [100%] 2 of 2, failed: 1 ✔
[e2/7371b2] NOTE: Process `method:method_process (openproblems_bmmc_multiome_phase1)` terminated with an error exit status (1) -- Error is ignored
Completed at: 24-Sep-2021 09:33:36
Duration    : 1m 27s
CPU hours   : 0.1 (5.7% failed)
Succeeded   : 1
Ignored     : 1
Failed      : 1
```

Pay attention to the exit status as well as the number of succeeded instances. If you managed to generate at least one output file (i.e. Succeeded > 0), you can still submit your solutions to eval.ai but will only get scored on the solutions you submitted.

### View exit codes
The error notifications might have disappeared by the time the pipeline has finished running. Use the `nextflow log` command to view the hash codes and exit statuses of the different executions.

```
$ bin/nextflow log small_montalcini -f hash,name,exit,status
5f/5ff487	  method:method_process (openproblems_bmmc_cite_phase1)	      0   COMPLETED
e2/7371b2	  method:method_process (openproblems_bmmc_multiome_phase1)	  1   FAILED
```

### Interpret exit codes

The reason why an execution failed can often be derived from the exit code:

* 1: An exception occurred from within the script. See the relevant section below.
* 127: The Docker container could not be built. Rerunning the submission script might help, otherwise contact the #support channel in Discord.
* 137: The process ran out of memory. See the relevant section below.

### Solving exit code 1

The first step in finding out what went wrong with this execution is to check the Nextflow work directory. This contains all the information that was generated
throughout the process. Note that the Nextflow log only shows the first few characters of the hashcode, so you will need to use autocomplete to get the full path name.


```sh
$ ls -a1 work/e2/7371b25a57ecc11946346b462e7d2f/

.command.begin
.command.err
.command.log
.command.out
.command.run
.command.sh
.exitcode
openproblems_bmmc_multiome_phase1.censor_dataset.output_mod1.h5ad
openproblems_bmmc_multiome_phase1.censor_dataset.output_mod2.h5ad
```

{{< callout note >}}
**Tip:** Modify the command above depending on the output you got from Nextflow. For example, if Nextflow tells you process `5f/5ff487` failed, you should be looking in the `work/5f/5ff487...` directory and not the `work/e2/7371b2..` directory. Use auto-completion to get the full name of the directory as Nextflow only displays the first 6 characters hash.
{{</ callout >}}

You can view the `exitcode`, `stdout` and `stderr` of this process by viewing the `.exitcode`, `.command.log` and `.command.err` files, respectively.

In this case, an exception was thrown after the data was loaded because the method at hand is specifically designed for GEX+ADT and not GEX+ATAC data.

```
$ cat work/e2/7371b25a57ecc11946346b462e7d2f/.exitcode
1

$ cat work/e2/7371b25a57ecc11946346b462e7d2f/.command.log 
Loading dependencies
Loading datasets
Error: this method only works on GEX+ADT data
Execution halted

$ cat work/e2/7371b25a57ecc11946346b462e7d2f/.command.err 
Error: this method only works on GEX+ADT data
Execution halted
```

If the error log is not sufficient in figuring out the issue, we suggest debugging your script by editing the viash codeblock and running through your code step by step.
To do this, change the paths specified as follows (example shown for Python but analagous in R):

```python
## VIASH START
par = {
    'input_mod1' : "output/datasets/joint_embedding/openproblems_bmmc_multiome_phase1/openproblems_bmmc_multiome_phase1.censor_dataset.output_mod1.h5ad",
    'input_mod2' : "output/datasets/joint_embedding/openproblems_bmmc_multiome_phase1/openproblems_bmmc_multiome_phase1.censor_dataset.output_mod2.h5ad",
    'output' : "debug_output.h5ad",
    # ... other parameters
}
## VIASH END
```

### Solving exit code 137

Exit code 137 means that one of the instances where your script was ran on one of the datasets ran out of memory (max 10GB by default).

If you're using Docker Desktop on Mac OS X, a common cause is the default memory constraint being 2GB. To increase the memory constraint, please edit the [Resources Configuration](https://docs.docker.com/desktop/mac/#resources).

If this isn't the issue, your script is simply using too much memory. By default, methods get 10GB to run on one of the datasets. Try manually running the code blocks in your script and try to optimize where possible:

* Remove large data objects when not being used anymore
* Use sparse data matrices whenever possible
* Use algorithms with a lower algorithmic complexity

If none of the options above are possible, consider upgrading the memory limits of your component, as documented below.


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

## My submission is stuck at status 'Submitted'

This status means your submission has been submitted to the queue but hasn't been picked up by the evaluation worker yet.
Depending on how many submissions are being submitted by yourself and other competitors, a delay of about 30 minutes is expected.
If you're experiencing longer waiting times, please contact @rcannood in the Discord #support channel.

## How does the Nextflow execution in `2_generate_submission.sh` work?

The codeblock which executes the actual execution of your method on each of the datasets is the following:

```bash
bin/nextflow \
  run openproblems-bio/neurips2021_multimodal_viash \
  -r $PIPELINE_VERSION \
  -main-script src/predict_modality/workflows/generate_submission/main.nf \
  --datasets 'output/datasets/predict_modality/**.h5ad' \
  --publishDir output/predictions/predict_modality/ \
  -resume \
  -latest \
  -c scripts/nextflow.config
```

You can split up the command above as follows:

* Starting a Nextflow pipeline:
  ```
  bin/nextflow run
  ```
* Specify where the pipeline is located:
  ```
  openproblems-bio/neurips2021_multimodal_viash -r 1.2.0
  ```
* Specify the path of the pipeline script within the repository:
  ```
  -main-script src/predict_modality/workflows/generate_submission/main.nf
  ```
* Path to datasets:
  ```
  --datasets 'output/datasets/predict_modality/**.h5ad'
  ```
* Path to output:
  ```
  --publishDir output/predictions/predict_modality/
  ```
* Resource parameter file:
  ```
  -c scripts/nextflow.config
  ```
* Resume on previous executions:
  ```
  -resume
  ```
* Always pull latest GitHub repository if possible:
  ```
  -latest
  ```

The pipeline script (`src/predict_modality/workflows/generate_submission/main.nf`) contains more or less the following code:

```nextflow
nextflow.enable.dsl=2

include { method } from "$launchDir/target/nextflow/main.nf" params(params)

params.datasets = "s3://neurips2021-multimodal-public-datasets/predict_modality/**.h5ad"

workflow {
  main:
  print(params.datasets)
  Channel.fromPath(params.datasets)
    | map { [ it.getParent().baseName, it ] }
    | filter { !it[1].name.contains("output_test_mod2") }
    | groupTuple
    | map { id, datas -> 
      def fileMap = datas.collectEntries { [ (it.name.split(/\./)[-2].replace("output_", "input_")), it ]}
      [ id, fileMap, params ]
    }
    | method
}
```

This script might me a little hard to read if you don't know any Nextflow DSL or Groovy, but it's actually rather simple. This script:

* looks in the path specified by the --datasets parameter, which is a list of all h5ad files in the output/datasets/predict_modality folder. 
* it maps the files to a tuple [ parent dir name, file ]
* it filters away files containing the term output_test_mod2 because these are the solution files
* it groups the files by the directory name (name of the dataset)
* it transforms the list of tuples to the correct parameter names, e.g. [ dataset_id, [ input_train_mod1: file, input_train_mod2: file, input_test_mod1: file ], params ]
* runs the nextflow module generated by viash