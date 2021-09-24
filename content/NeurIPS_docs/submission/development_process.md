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

If this process runs successfully, then you will be instructed to upload the submission to EvalAI. If you see any warnings, please consult our [FAQ](/neurips_docs/submission/faq).

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
If you encounter any issues, please look at the [Frequently Asked Questions](/neurips_docs/submission/faq). If this doesn't solve your problem, visit the #support channel on Discord.