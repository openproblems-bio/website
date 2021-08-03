---
title: "Task 1: Modality Prediction"
linktitle: "Task 1: Modality Prediction"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 2
---
## Predicting the flow of information from DNA to RNA and RNA to Protein
Experimental techniques to measure multiple modalities within the same single cell are increasingly becoming available. The demand for these measurements is driven by the promise to provide a deeper insight into the state of a cell. Yet, the modalities are also intrinsically linked. We know that DNA must be accessible (ATAC data) to produce mRNA (expression data), and mRNA in turn is used as a template to produce protein (protein abundance). These processes are regulated often by the same molecules that they produce: for example, a protein may bind DNA to prevent the production of more mRNA. Understanding these regulatory processes would be transformative for synthetic biology and drug target discovery. Any method that can predict a modality from another must have accounted for these regulatory processes, but the demand for multi-modal data shows that this is not trivial.

<figure>
  <img src="/media/tasks/predict.svg">
  <figcaption>
    <h3>
      Task 1: Prediction
    </h3>
    <p style="font-size: medium;">
      In this task, the goal is to take one modality (ATAC or RNA) and predict the other modality (RNA or Protein) for all features in each cell. Performance is measured using Mean Square Error.
    </p>
  </figcaption>
</figure>

This task requires translating information between multiple layers of gene regulation. In some ways, this is similar to the task of machine translation. In machine translation, the same sentiment is expressed in multiple languages and the goal is to train a model to represent the same meaning in a different language. In this context, the same cellular state is measured in two different feature sets and the goal of this task is to translate the information about cellular state from one modality to the other. We chose to limit the prediction task in the direction that genetic information generally flows (DNA ➞ RNA ➞ Protein).

## Task API

### Input data formats

This component expects two inputs, `--input_mod1` and `--input_mod2`. They are both [AnnData](https://anndata.readthedocs.io/en/latest/) h5ad files with the attributes below. If the `feature_types` of one file is "GEX", then that of the other must be either "ATAC" or "ADT". These objects can be opened in Python using the [`anndata.read_h5ad()`](https://anndata.readthedocs.io/en/latest/anndata.read_h5ad.html) function or the [`scanpy.read_h5ad()`](https://scanpy.readthedocs.io/en/stable/generated/scanpy.read_h5ad.html) function. This object can be opened in R using the [`readH5AD`](https://rdrr.io/github/theislab/zellkonverter/man/readH5AD.html) function


```plaintext
adata
  Input AnnData object for modality 1 or 2

  Attributes
  ----------
  adata.X : ndarray, shape=(n_obs, n_var)
    Sparse profile matrix of given modality. If .var['feature_types'] == "GEX" or "ADT",
    values in adata.X represent expression counts for each gene. If
    .var['feature_types'] == "ATAC", values represent counts of reads in peaks for
    chromatin accessibility
  adata.uns['dataset_id'] : str
    The name of the dataset.
  adata.obs['group']: ndarray, shape=(n_obs,)
    Denotes whether a cell belongs to the 'train' or the 'test' set.
  adata.obs_names : ndarray, shape=(n_obs,)
    Ids for the cells.
  adata.var['feature_types']: ndarray, shape=(n_var,)
    The modality of this file, should be equal to "GEX", "ATAC" or "ADT".
  adata.var_names : ndarray, shape=(n_var,)
    Ids for the features.
```

{{% callout note  %}}
Note, the dimensions of these two input h5ad files are different;
* `input_mod1` contains the modality 1 data of both the `train` and the `test` cells.
* `input_mod2` contains only modality 2 data of the `train` cells.
{{% /callout  %}}


### Output data formats

This component should output only one h5ad file, `--output_prediction`, containing the predicted profile values of modality 2 for the **test cells only**. It has the following attributes:

```plaintext
adata
  Output AnnData object containing predictions for modality 2 in the "test" cells

  Attributes
  ----------
  adata.X : ndarray, shape=(n_obs, n_var)
    Sparse profile matrix.
  adata.uns['dataset_id'] : str
    The name of the dataset.
  adata.uns['method_id'] : str
    The name of the prediction method. This is used to track submissions.
  adata.var['feature_types'] : ndarray, shape=(n_var,)
    The modality of this file, should be equal to "GEX", "ATAC" or "ADT".
  adata.obs['group'] : ndarray, shape=(n_obs,)
    Should be "test" for all cells
  adata.obs_names : ndarray, shape=(n_obs,)
    Ids for the cells.
```

### Metric

Performance in task 1 is measured using mean square error between the observed and predicted values for modality 2 in the `test` set. Lower is better.

The metric function used to evaluate the prediction has the following structure:

```plaintext
def calculate_mse(adata_mod2, adata_mod2_answer):  
    '''Function to calcualte MSE between prediction and solution for the test sets  

    Params
    ------
    adata_mod2 : AnnData, shape=(n_obs, n_var)
      User-submitted prediction for expression of mod2 in cells from the test set
    adata_mod2_answer : AnnData, shape=(n_obs, n_var)
      Measured values for expression of mod2 in the test set

    Returns
    -------
    mean_square_error : float
      The mean square error between the predicted and observed values for all features in
      the test set.
    '''

    return mean_square_error(adata_mod2.X, adata_mod2_answer.X)
```

## Prizes

For this task, three prizes of $1000 will be awarded to the submissions for each of the following criteria:
1. Best performance on CITE-seq
2. Best performance on ATAC-seq
3. Best performance average across modalities
