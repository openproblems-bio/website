---
title: "Task 2: Modality Matching"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 3
---
## Matching profiles of each cell from different modalities.
While joint profiling of two modalities in the same single cell is now possible, most single-cell datasets that exist measure only a *single* modality. These modalities complement each other in their description of cellular state. Yet, it is challenging to analyse uni-modal datasets together when they do not share observations (cells) or a common feature space (genes, proteins, or open chromatin peaks). If we could map observations to one another across modalities, it would be possible to treat separately profiled datasets in the same manner as new multi-modal sequencing data. Mapping these modalities to one another opens up the vast amount of uni-modal single-cell datasets generated in the past years to multi-modal data analysis methods.

Unlike in task 1, where the goal was to predict all values of RNA or protein abundances from ATAC or RNA (respectively) in each cell, the goal of this task is to identify the correspondence between single-cell profiles. Because we are only interested in matching observations, the competitors are encouraged to consider feature selection to identify the representation of the input most important for matching observations.

<figure>
  <img src="/media/tasks/match.svg">
  <figcaption>
    <h3>
      Task 2: Matching
    </h3>
    <p style="font-size: medium;">
      In this task, competitors are given a jointly measured multimodal dataset (only ATAC + RNA shown) where the cell barcodes linking the two measures are obscured for the purposes of the competition. Competitors must estimate which profiles match across modalities and provide the probability distribution of these predictions. The sum of weights in the correct correspondences is used to score submissions.
    </p>
  </figcaption>
</figure>

## Task API

### Input data formats

This component expects two inputs, `--input_mod1` and `--input_mod2`. They are both [AnnData](https://anndata.readthedocs.io/en/latest/) h5ad files for which the rows are shuffled and anonymized. These files have the attributes below. If the `feature_types` of one file is "GEX", then that of the other must be either "ATAC" or "ADT" (antibody-derived tag, a measure of protein abundance).

```plaintext
adata
  Input AnnData object for task 2

  Attributes
  ----------
  adata.X : ndarray, shape=(n_obs, n_var)
    Sparse profile matrix of given modality. If .var['feature_types'] == "GEX" or "ADT",
    values in adata.X represent expression counts for each gene. If
    .var['feature_types'] == "ATAC", values represent counts of reads in peaks for
    chromatin accessibility
  adata.uns['dataset_id'] : str
    The name of the dataset.
  adata.var['feature_types']: ndarray, shape=(n_var,)
    The modality of this file, should be equal to "GEX", "ATAC" or "ADT".
  adata.var_names : ndarray, shape=(n_var,)
    Ids for the features.
  adata.obs_names : ndarray, shape=(n_obs,)
    Anonymised ids for the cells.
```




### Output data formats

This component should output only *one* h5ad file, `--output`, containing the predicted probabilities of the matchings between the two input datasets.

```plaintext
adata
  Output AnnData object for task 2

  Attributes
  ----------
  adata.X : ndarray, shape=(n_obs)
    Sparse pairing matrix.
  adata.uns['dataset_id'] : str
    The name of the dataset.
  adata.uns['method_id']: str
    The name of the prediction method.
  adata.obs_names : ndarray, shape=(n_obs,)
    Anonymised ids for the cells.

```

{{% callout note  %}}
**Restrictions on the pairing matrix**

There are two restrictions on the pairing matrix:
1. Row stochastic - The sum of each row of the matrix should be 1. This limits the amount of weight that can be placed on each pairing $i,j$
2. Sparsity - If `input_mod1` has shape `(n_obs, n_var1)` and `input_mod2` has shape `(n_obs, n_var2)`, the pairing matrix must be a sparse matrix with shape `(n_obs, n_obs)` containing **at most `100×N` non-zero values**. Predictions with more than `100×N` non-zero values will be rejected by the metric component.
{{% /callout  %}}



### Metric

Performance in task 2 is measured using a weighted sum of the confidences placed on correct pairings `i,j`.
Specifically the score is calculated using the following equation:
$$ Score = \sum_i \sum_j X_{i,j} * \delta_{i,j} $$
where $X_{i,j}$ is the entry in the sparse pairing matrix from the user's submission and $\delta_{i,j}$ is $1$ if profile $i$ and $j$ were measured in the same cells and $0$ otherwise.
## Prizes

For this task, three prizes of $1000 will be awarded to the submissions for each of the following criteria:
1. Best performance on CITE-seq
2. Best performance on ATAC-seq
3. Best performance average across modalities
