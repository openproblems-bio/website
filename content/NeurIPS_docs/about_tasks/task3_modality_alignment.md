---
title: "Task 3: Joint Embedding"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 3
---
## Learn a joint embedding from multiple modalities
The functioning of organs, tissues, and whole organisms is determined by the interplay of cells. Cells are characterised into broad types, which in turn can take on different states. Here, a cell state is made up of the sum of all processes that are occurring within the cell. We can gain insight into the state of a cell by different types of measurements: e.g., RNA expression, protein abundance, or chromatin conformation. Combining this information to describe cellular heterogeneity requires the formation of joint embeddings generated from this multimodal data. These embeddings must account for and remove possible batch effects between different measurement batches. The reward for methods that can achieve this is great: a highly resolved description of the underlying biological state of a cell that determines its function, how it interacts with other cells, and thus the cell’s role in the functioning of the whole tissue.

<figure>
  <img src="/media/tasks/integrate.svg">
  <figcaption>
    <h3>
      Task 3: Joint embedding
    </h3>
    <p style="font-size: medium;">
      In this task, the goal is to learn an embedded space that leverages the information of multiple modalities. Quality of the embedding will be scored using a number of metrics derived from expert annotation.
    </p>
  </figcaption>
</figure>


## Task API

### Input data formats

This component expects two inputs, `--input_mod1` and `--input_mod2`. They are both [AnnData](https://anndata.readthedocs.io/en/latest/) h5ad files for which the rows are shuffled and anonymised. These files have the attributes below. If the `feature_types` of one file is "GEX", then that of the other must be either "ATAC" or "ADT".

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
    Ids for the cells.
```

### Output data formats

This component should output only *one* h5ad file, `--output`, containing the predicted pairings of the two input datasets. We are placing a limit of the embedding space to 100 dimensions. The output file must have the following attributes.

```plaintext
adata
  Output AnnData object for task 2

  Attributes
  ----------
  adata.X : ndarray, shape=(n_obs, 100)
    Embedding matrix.
  adata.uns['dataset_id'] : str
    The name of the dataset.
  adata.uns['method_id']: str
    The name of the prediction method.
  adata.obs_names : ndarray, shape=(n_obs,)
    Ids for the cells.

```



### Metric

Performance in task 3 will be measured using a number of different metrics.



## Prizes

For this task, three prizes of $1000 will be awarded to the submissions for each of the following criteria:
1. Best performance on CITE-seq
2. Best performance on ATAC-seq
3. Best performance average across modalities
