---
title: "Using the Starter Kits"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 10
---

This page provides information to go from starter kit to a submission ready for EvalAI.

## List of Starter Kits

All of the starter kits for the competition are available here:

### Task 1 - Predict Modality

* [Starter Kit in Python](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/download/0.5.0/starter_kit-predict_modality-python.zip)
* [Starter Kit in R](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/download/0.5.0/starter_kit-predict_modality-r.zip)

### Task 2 - Match Modality

* [Starter Kit in Python](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/download/0.5.0/starter_kit-match_modality-python.zip)
* [Starter Kit in R](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/download/0.5.0/starter_kit-match_modality-r.zip)

### Task 3 - Joint Embedding

* [Starter Kit in Python](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/download/0.5.0/starter_kit-joint_embedding-python.zip)
* [Starter Kit in R](https://github.com/openproblems-bio/neurips2021_multimodal_viash/releases/download/0.5.0/starter_kit-joint_embedding-r.zip)

## What's in the kit

The Starter Kits have all you need to compete in the Multimodal Single-Cell Data Integration Challenge.

Let's look at the Task 1 Starter Kit (Python):

```
starter_kit-predict_modality-python/
├── README.md                     # Read this
├── bin/                          # Binaries needed to generate a submission
│   ├── nextflow
│   └── viash
├── config.vsh.yaml               # Configuration for the submission component
├── generate_submission.sh        # Script to generate a submission.zip that can be uploaded to EvalAI
├── nextflow.config               # Configuration for Nextflow (ignore)
├── sample_data/                  # Sample data to test your code
│   ├── test_resource.mod1.h5ad
│   └── test_resource.mod2.h5ad
└── script.py                     # Script containing your method
```

The most important parts of this directory are the `script.py` and `config.vsh.yaml` files. You'll need to edit these components to create a submission for the competition.

You'll also need to run the `generate_submission.sh` script to build a `submission.zip` file to submit to EvalAI so your method is registered on the leaderboards.

The rest of the starter kit contains files to build a `submission.zip` file.

## Configuring your local environment

For this competition, we want competitors to share code and we will evaluate results on a remote server. To facilitate running arbitrary scripts submitted by contestants, we are using [viash](https://viash.io), a tool designed to turn R, Python, C, etc. scripts into Dockerized components that can be executed from the command line and integrated into a workflow system like [Nextflow](https://www.nextflow.io/).

Before you get started with the competition you will need to install two  prerequisites:

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Install Java Runtime ≥8.0, available from [OpenJDK](https://adoptopenjdk.net/?variant=openjdk11&jvmVariant=hotspot)

## Editing the Starter Kit

To go from Starter Kit to Submission, you need to edit two files:
* `script.[py/R]` - A Python or R script containing the method to be evaluated
* `config.vsh.yaml` - A YAML configuration script that tells Viash how to create a component from the script

### Editing the script

The following section will use the Python kit for Modality Prediction (Task 1) as an example.

The starter kit `script.py` has 3 components:
* Imports
* Viash block
* Method

Let's look at the file section by section

#### Imports

This section defines which packages the method expects, if you want to import a new different package, add the import statment here and add the dependency to the config.vsh.yaml

```python
import logging
import anndata as ad
import umap
from scipy.sparse import csc_matrix
from sklearn.neighbors import KNeighborsRegressor

logging.basicConfig(
    level=logging.INFO
)
```
#### Viash block

This optional code block exists to facilitate prototyping so your script can run when called directly with `$ python script.py`. The most common pattern is to use this block to instantiate a `par` dictionary of default arguments that would typically be dynamically generated based on the command-line execution of the component.

```python
## VIASH START

# Anything within this block will be removed by `viash` and will be
# replaced with the parameters as specified in your config.vsh.yaml.

par = {
    # Required arguments for the task
    'input_mod1': 'sample_data/test_resource.mod1.h5ad',
    'input_mod2': 'sample_data/test_resource.mod2.h5ad',
    'output': 'output.h5ad',
    # Optional method-specific arguments
    'distance_method': 'minkowski',
    'n_pcs': 4,
    'n_neighbors': 5,
}

## VIASH END
```

Here, the `par` dictionary contains all the `arguments` defined in the `config.vsh.yaml` file. When you create the component using the `generate_submission.sh` script, Viash will remove everything between the `## VIASH START` and `## VIASH END` comments.

#### Method

This block reads in data, runs a method, and writes output.

```
## Data reader
logging.info('Reading `h5ad` files...')

ad_mod1 = ad.read_h5ad(par['input_mod1'])
ad_mod2 = ad.read_h5ad(par['input_mod2'])

# TODO: change this to the name of your method
method_id = "python_starter_kit"

logging.info('Performing dimensionality reduction on modality 1 values...')

## Method

# Notice how this instantiation also uses the pre-defined parameter for
# the distance method to be used here.
embedder = umap.UMAP(
    n_components=par['n_pcs'],
    metric=par['distance_method'],
)

X = embedder.fit_transform(ad_mod1.X)

X_train = X[ad_mod1.obs['group'] == 'train']
X_test = X[ad_mod1.obs['group'] == 'test']

assert len(X_train) + len(X_test) == len(X)

# Get all responses of the training data set to fit the
# KNN regressor later on.
#
# Make sure to use `toarray()` because the output might
# be sparse and `KNeighborsRegressor` cannot handle it.
y_train = ad_mod2.X.toarray()

logging.info('Running KNN regression...')

reg = KNeighborsRegressor(
    n_neighbors=par['n_neighbors'],
    metric=par['distance_method']
)

reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

# Store as sparse matrix to be efficient. Note that this might require
# different classifiers/embedders before-hand. Not every class is able
# to support such data structures.
y_pred = csc_matrix(y_pred)

adata = ad.AnnData(
    X=y_pred,
    uns={
        'dataset_id': ad_mod1.uns['dataset_id'],
        'method_id': method_id,
    },
)

## Data writer
adata.write(par['output'])
```

Your job is to replace the Method section with code that operates on `ad_mod1` and `ad_mod2` to minimize the mean square error between `y_pred` and `y_true` for the test data that is only accessible to the EvalAI worker.

### Updating the configuration

Once the script is working, you'll want to update the `config.vsh.yaml` file. The configuration has two sections:
* Functionality about the script, including method arguments and resources
* Platform targets that define how to build the component, including dependencies

Full documentation on the configuration is available on the Viash [docs](https://viash.io/docs/reference_config/config/).

#### Functionality

The first section of the configuration file contains information about the metadata of the script including parameters for the script and a list of resource files. You can read more about this section in the Viash [docs](https://viash.io/docs/reference_config/functionality/).

```yaml
functionality:
  name: method

  # metadata for your method
  description: A description for your method.
  authors:
    - name: John Doe
      email: johndoe@youremailprovider.com
      roles: [ author, maintainer ]
      props: { github: johndoe, orcid: "0000-1111-2222-3333" }

  # parameters
  arguments:
    # required inputs
    - name: "--input_mod1"
      type: "file"
      example: "dataset_mod1.h5ad"
      description: Modality 1 dataset.
      required: true
    - name: "--input_mod2"
      type: "file"
      example: "dataset_mod2.h5ad"
      description: Modality 2 dataset.
      required: true
    # required outputs
    - name: "--output"
      type: "file"
      direction: "output"
      example: "output.h5ad"
      description: Data for all cells in mod1 and mod2 embedded to ≤100 dimensions.
      required: true
    # Method-specific parameters. Change these to expose parameters of your method to Nextflow (optional)
    - name: "--distance_method"
      type: "string"
      default: "minkowski"
      description: The distance metric to use. Possible values include `euclidean` and `minkowski`.
    - name: "--n_pcs"
      type: "integer"
      default: 4
      description: Number of components to use for dimensionality reduction.
    - name: "--n_neighbors"
      type: "integer"
      default: 5
      description: Number of neighbors to use.

  # files your script needs
  resources:
    - type: python_script
      path: script.py

```

In this section of the configuration you should focus on updating the following sections:
1. Description and Authors - Information about who contributed the method
2. Arguments - Each section here defines a command-line argument for the script. These sections are all passed  to the script in the form of a dictionary called `par`. You only need to change the method-specific parameters, and if you would like these parameters hard-coded into the script, you do not need to provide any parameters here.
3. Resources - This section describes the files that need to be included in your component. For example if you'd like to add a file containing model weights called `weights.pt`, add the following section the the resources block:
    ```yaml
    - type: file
    path: weights.pt
    ```
    This file will now be accessible to the script in the working directory so you could run `torch.load("./weights.pt")`


#### Platform

The Platform section defines the information about how the Viash component is run on various backend platforms. The two platforms that are important for the competition are:

1. Docker ([docs](https://viash.io/docs/reference_config/platform-docker/))
2. Nextflow ([docs](https://viash.io/docs/reference_config/platform-nextflow/))

```yaml
# target platforms
platforms:

  # By specifying 'docker' platform, viash will build a standalone
  # executable which uses docker in the back end to run your method.
  - type: docker
    # you need to specify a base image that contains at least
    # R, python, bash and the 'anndata' python package.
    image: dataintuitive/randpy:r4.0_py3.8_bioc3.12
    # You can specify additional dependencies with 'setup'.
    # See https://viash.io/docs/reference_config/platform-docker/#setup-list
    # for more information on how to add more dependencies.
    setup:
      # - type: apt
      #   packages:
      #     - bash
      # - type: python
      #   packages:
      #     - scanpy
      - type: python
        packages:
          - scikit-learn
          - anndata
          - scanpy

  # By specifying a 'nextflow', viash will also build a viash module
  # which uses the docker container built above to also be able to
  # run your method as part of a nextflow pipeline.
  - type: nextflow
    publish: true
    directive_time: 5m
    directive_memory: 10 GB
```

The most important part of this section to update is the `setup` definition that describes the packages that need to be installed in the docker container for the method to run. There are many different methods for specifying these requirements described in the Viash [docs](https://viash.io/docs/reference_config/platform-docker/#setup-list).

{{< callout note >}}
**Tip:** After making changes to the components dependencies, you will need to rebuild the docker container as follows:

```sh
$ bin/viash run -- ---setup cachedbuild
[notice] Running 'docker build -t method:dev /tmp/viashsetupdocker-method-tEX78c'
```
{{</ callout >}}

{{< callout note >}}
**Tip #2:** You can view the dockerfile that Viash generates from the config file using the `---dockerfile` argument:
```sh
$ bin/viash run -- ---dockerfile
```
{{</ callout >}}


## Running the component locally

As you're working on the component for your submission, you will likely want to prototype the component locally to ensure that it works.

### Running `scripy.py`

The first way you can do this is to simply run the `script.py` file.

```ruby
$ python script.py
```

As long as you left the Viash block in the script, the `par` dictionary will be instantiated when you run the script and the script will work as a normal Python script. We included some sample data in starter kits in the `sample_data/` directory. These are very small datasets that have the same structure as the training and evaluation datasets but with fewer observations and variables.

### Using Viash build to build the component
If you can run the script directly, you should next proceed to building a Viash component and running on the sample data.

From within the starter kit, you can run the code on the sample dataset as follows:

```sh
$ bin/viash run config.vsh.yaml -- \
  --input_mod1 sample_data/test_resource.mod1.h5ad \
  --input_mod2 sample_data/test_resource.mod2.h5ad \
  --output test_output.h5ad
```

**Tip:** You can also omit the `config.vsh.yaml` in the above command.

**Tip #2:** Run `bin/viash run -- --help` to view the command-line interface of your component.

### Generating a submission

If you can run your contribution on sample data, you can now proceed to generating a submission file.

```ruby
$ ./generate_submission.sh
```

This function runs a Nextwork workflow to:
1. Build a Viash module from your `script.py` and `config.vsh.yaml`
2. Download public datasets from `s3://neurips2021-multimodal-public-datasets/`
3. Run your method against the public data
4. Generate a `submission.zip` file to upload to EvalAI

Note, it may take up to 20 minutes to download the public data. You should only need to do this once.

If this process runs successfully, then you will be instructed to upload the submission to EvalAI.

## Troubleshooting
What if running your method on the sample data works but fails when applied to the submission datasets? Given the following output:

```sh
$ ./generate_submission.sh
```
    ...
    [78/9f8fc2] NOTE: Process `method:method_process (dyngen_atac_disconnected_mod2)` terminated with an error exit status (127) -- Error is ignored
    [20/330b8a] NOTE: Process `method:method_process (dyngen_atac_bifurcating_converging_mod2)` terminated with an error exit status (127) -- Error is ignored
    Completed at: 05-Aug-2021 12:13:39
    Duration    : 1m 32s
    CPU hours   : 0.3 (100% failed)
    Succeeded   : 0
    Ignored     : 32
    Failed      : 32

You can still submit your solutions to eval.ai but you will get penalized for every failed execution.

You can check out what went wrong by looking at the tag for the process that failed (e.g. `20/330b8a`):

```sh
$ ls -1a work/20/330b8a52b1a71489e7c53c66ef686e/
```
    .command.begin
    .command.err
    .command.log
    .command.out
    .command.run
    .command.sh
    dyngen_atac_bifurcating_converging_mod2.censor_dataset.output_mod1.h5ad
    dyngen_atac_bifurcating_converging_mod2.censor_dataset.output_mod2.h5ad
    .exitcode

You can view the `stdout` and `stderr` of this process by viewing the `.command.log` and `.command.err` files respectively. You can also try to run your component manually by editing the `VIASH START` and `VIASH END` code block in your script (see below) and running through the code manually.

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


If you need any help, please reach out on the competition [Discord](https://discord.gg/Q3RKGMGD3E) server. See the #troubleshooting or #viash-help channels.
