---
title: "About AnnData Objects"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 30
---

All the datasets provided in the competition are organized in [AnnData](https://anndata.readthedocs.io) objects. This page describes the structure of AnnData objects so that you can work with the data in the competition efficiently.

AnnData is a generic data storage format especially well suited for single-cell data. The class stores a data matrix `X` together with annotations of observations and variables in Pandas DataFrames. The advantage of storing the annotations and data in the same object is to ensure that when inspecting slices of the data, relevant annotations are properly linked with the views of the data.

The most common attributes are:
* `adata.X` - The data. This can by a sparse array or a numpy array.
* `adata.n_obs` - The number of observations, equal to `adata.X.shape[0]`
* `adata.obs_names` - The index for the observations, similar to a Pandas DataFrame `index`. Typically this contains cell barcodes.
* `adata.obs` - A Pandas DataFrame containing annotations of the observations, for example, cluster labels or the donor of origin. The index of the DataFrame must be the same as `adata.obs_names`.
* `adata.obsm` - A dictionary of n-dimensional arrays (ndarrays) of shape `(n_obs, m)`. For example, it is common to store a PCA or UMAP embedding of the data in `adata.obsm["X_pca"]` or `adata.obsm["X_umap"]`.
* `adata.obsp` - Pairwise annotations of the observations. Most often this contains a graph adjacency matrix where the nodes in the graph are observations.
* `adata.n_var` - The number of variables or features in the data, equal to `adata.X.shape[1]`
* `adata.var_names` - The index for the variables, similar to a Pandas DataFrame `columns`. Typically this contains gene names.
* `adata.var` - Annotations on the variables, e.g. whether a feature is a protein coding gene or a non-coding gene. Index of this DataFrame must match `adat.var_names`.
* `adata.varm`, `adata.varp` - Analogous to the `obsm` and `obsp` attributes. Not commonly used.
* `adata.uns` - A dictionary to story any unstructured annotations associated with the data. E.g, a data version.

The following diagram shows these attributes and their relation to the data:

<figure>
  <img src="/media/learning/anndata.svg">
  <figcaption>
    <h3>
      AnnData  - Annotated Data Containers
    </h3>
    <p style="font-size: medium;">
      AnnData provides a scalable way of keeping track of data and learned annotations.
    </p>
  </figcaption>
</figure>

AnnData objects can be opened in Python using the [`anndata.read_h5ad()`](https://anndata.readthedocs.io/en/latest/anndata.read_h5ad.html) function or the [`scanpy.read_h5ad()`](https://scanpy.readthedocs.io/en/stable/generated/scanpy.read_h5ad.html) function. This object can be opened in R using the [`readH5AD`](https://rdrr.io/github/theislab/zellkonverter/man/readH5AD.html) function




For the full AnnData API, please consult the [docs](https://anndata.readthedocs.io/en/latest/anndata.AnnData.html).
