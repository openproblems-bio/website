---
title: "Starter Kit to Submission"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 10
---

This page provides information to go from starter kit to a submission ready for EvalAI.

## List of Starter Kits

All of the starter kits for the competition are available here:

### Task 1 - Modality prediction

* Starter Kit in Python
* [Starter Kit in R](https://github.com/openproblems-bio/neurips2021_multimodal_challenge/raw/master/starter_kits/starter_kit_predict_modality_r_0.4.0.zip)

### Task 2 - Modality matching

* Starter Kit in Python
* Starter Kit in R

### Task 3 - Modality alignment

* Starter Kit in Python
* Starter Kit in R

## Editing the Starter Kit

To go from Starter Kit to Submission, you need to edit two files:
* `script.[py/R]` - A Python or R script containing the method to be evaluated
* `config.vsh.yaml` - A YAML configuration script that tells Viash how to create a component from the script

### Editing the script

The following section will use the Python kit for Modality Prediction (Task 1) as an example.

The starter kit `script.py` looks like this:


```python
# Dependencies:
# pip: scikit-learn, anndata, scanpy, umap-learn
#
# Python starter kit for the NeurIPS 2021 Single-Cell Competition. Parts
# with `TODO` are supposed to be changed by you.
#
# More documentation:
#
# https://viash.io/docs/creating_components/python/

import logging
import anndata as ad
import umap
from scipy.sparse import csc_matrix
from sklearn.neighbors import KNeighborsRegressor

logging.basicConfig(
    level=logging.INFO
)

## VIASH START

# Anything within this block will be removed by `viash` and will be
# replaced with the parameters as specified in your config.vsh.yaml.

par = {
    'input_mod1': 'sample_data/test_resource.mod1.h5ad',
    'input_mod2': 'sample_data/test_resource.mod2.h5ad',
    'distance_method': 'minkowski',
    'output': 'output.h5ad',
    'n_pcs': 4,
    'n_neighbors': 5,
}

## VIASH END

# TODO: change this to the name of your method
method_id = "python_starter_kit"

logging.info('Reading `h5ad` files...')

ad_mod1 = ad.read_h5ad(par['input_mod1'])
ad_mod2 = ad.read_h5ad(par['input_mod2'])

# TODO: implement own method

logging.info('Performing dimensionality reduction on modality 1 values...')

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

adata.write(par['output'])
```
