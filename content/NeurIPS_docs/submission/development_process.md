---
title: "Development process"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 30
---

The typical workflow for developing a new method and submitting the results to the EvalAI repository is described below.

## Editing the script and config file

Implement your method in `script.py` (or `script.R` for R users) and update the Viash config accordingly. The file format of the script and config are described in the [Starter kit contents](/neurips_docs/submission/starter_kit_contents) description.

## Manually running the component

The easiest way to run a viash component is by using the command-line interface. You can view a component's interface using the `--help` flag:

```bash
$ bin/viash run config.vsh.yaml -- --help
python_starter_kit dev
A description for your method.

Options:
   --input_train_mod1
        type: file, required parameter
        example: dataset_mod1.h5ad
        Censored dataset, training cells.

   --input_test_mod1
        type: file, required parameter
        example: dataset_mod1.h5ad
        Censored dataset, test cells.

...
```

To run the component, simply provide parameters required by the component:

```bash
$ DATA_PATH="sample_data/openproblems_bmmc_cite_starter/openproblems_bmmc_cite_starter"
$ bin/viash run config.vsh.yaml -- \
  --input_train_mod1 "${DATA_PATH}.train_mod1.h5ad" \
  --input_train_mod2 "${DATA_PATH}.train_mod2.h5ad" \
  --input_test_mod1 "${DATA_PATH}.test_mod1.h5ad" \
  --output "output.h5ad"
```

Behind the screens, Viash will run your code inside a Docker container where the input data is automatically mounted. 

Alternatively, for debugging purposes, you can also run the script manually by running `python script.py` (or `Rscript script.R` for R users). Note that this bypasses any containerization or code generation functionality provided by Viash.

## Unit test the component

If you can run the script directly, you should next proceed to running unit tests on the data.

From within the starter kit, you can run the code on the sample dataset as follows:

```sh
$ ./scripts/1_unit_test.sh
```

## Generating a submission

If you can run your contribution on sample data, you can now proceed to generating a submission file.

```sh
$ ./scripts/2_generate_submission.sh
```

If this process runs successfully, then you will be instructed to upload the submission to EvalAI. If you see any warnings, please consult our [FAQ](/neurips_docs/about/questions).

## Evaluate locally

You can evaluate the results of your submission using the included evaluation script. Note this must be run after generating a submission.

```sh
$ ./scripts/3_evaluate_submission.sh
```

The evaluation results will be saved at a path like `output/evaluation/predict_modality`.

## Advanced topics

### Use additional files

For your component to be able to access additional files (such as a pre-trained model) from within your script, you need to specify these files under `.functionality.resources` in the config script as follows:
```yaml
  # files your script needs
  resources:
    # the script itself
    - type: python_script
      path: script.py
    # additional resources your script needs (optional)
    - path: pretrained_model.pt
```

For Python users, you can access the file at `meta['resources_dir'] + '/pretrained_model.pt'`. Similarly, R users can access the script at `paste0(meta$resources_dir, "/pretrained_model.pt")`.

## Troubleshooting

### Method fails on submission datasets
What if running your method on the sample data works but fails when applied to the submission datasets? Given the following output:

```sh
$ ./scripts/2_generate_submission.sh

    ...

    [78/9f8fc2] NOTE: Process `method:method_process (dyngen_atac_disconnected_mod2)` terminated with an error exit status (127) -- Error is ignored
    [20/330b8a] NOTE: Process `method:method_process (dyngen_atac_bifurcating_converging_mod2)` terminated with an error exit status (127) -- Error is ignored
    Completed at: 05-Aug-2021 12:13:39
    Duration    : 1m 32s
    CPU hours   : 0.3 (100% failed)
    Succeeded   : 0
    Ignored     : 32
    Failed      : 32
```

You can still submit your solutions to eval.ai but you will get penalized for every failed execution.

You can check out what went wrong by looking at the tag for the process that failed (e.g. `20/330b8a`):

```sh
$ ls -1a work/20/330b8a52b1a71489e7c53c66ef686e/
    .command.begin
    .command.err
    .command.log
    .command.out
    .command.run
    .command.sh
    dyngen_atac_bifurcating_converging_mod2.censor_dataset.output_mod1.h5ad
    dyngen_atac_bifurcating_converging_mod2.censor_dataset.output_mod2.h5ad
    .exitcode
```

You can view the `stdout` and `stderr` of this process by viewing the `.command.log` and `.command.err` files, respectively. You can also try to run your component manually by editing the `VIASH START` and `VIASH END` code block in your script (see below) and running through the code manually.

```python
## VIASH START
par = {
    input_mod1 : "work/20/330b8a52b1a71489e7c53c66ef686e/dyngen_atac_bifurcating_converging_mod2.censor_dataset.output_mod1.h5ad",
    input_mod2 : "work/20/330b8a52b1a71489e7c53c66ef686e/dyngen_atac_bifurcating_converging_mod2.censor_dataset.output_mod2.h5ad",
    output : "debug.h5ad",
    # ... other parameters
}
## VIASH END
```

If you need any help, please reach out on the competition [Discord](https://discord.gg/Q3RKGMGD3E) server. See the `#neurips2021-help` channel.
