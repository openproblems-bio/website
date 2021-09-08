---
title: "The benchmarking dataset"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 3
---

We are currently in the process of creating a benchmarking dataset for the competition. There will be two types of data:
* Joint profiling of single-cell RNA and protein using the [10X Genomics
Single Cell Gene Expression with Feature Barcoding](https://support.10xgenomics.com/single-cell-gene-expression/overview/doc/getting-started-single-cell-gene-expression-with-feature-barcoding-technology) with the  [Biolegend TotalSeq™-B Universal Cocktail v1.0](https://www.biolegend.com/en-us/products/totalseq-a-human-universal-cocktail-v1-0-20321?GroupID=GROUP28) panel  
* Joint profiling of single-nucleus RNA and chromatin accessibility using the [10X Genomics Single Cell Multiome ATAC + Gene Expression Kit](https://www.10xgenomics.com/products/single-cell-multiome-atac-plus-gene-expression)  

The current forms of the data are public available on S3. To download the data, first install the AWS CLI on your computer: https://aws.amazon.com/cli/

You can then access the data at the following locations:

* `s3://openproblems-bio/public/cite/CITE_ADT_processed.h5ad`
* `s3://openproblems-bio/public/cite/CITE_GEX_processed.h5ad`
* `s3://openproblems-bio/public/multiome/Multiome_ATAC_processed.h5ad`
* `s3://openproblems-bio/public/multiome/Multiome_GEX_processed.h5ad`
* `s3://openproblems-bio/public/LICENSE.txt`

You can download these files to your local computer with the following command:

```sh
aws s3 sync s3://openproblems-bio/public/  /tmp/public/ --no-sign-request
```

Note the dataset size is roughly 10GiB.

## Data format

The training data is accessible in an [AnnData](https://anndata.readthedocs.io/en/latest/) h5ad file with the attributes below. More information can be found on AnnData objects [here](/neurips_docs/submission/anndata_quickstart/).

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
  adata.obs["batch"] : ndarray, shape=(n_obs,)
    The batch from which the data was sequenced. Has format "s[1-4]d[1-9]" indicating the site and
    donor associated with the batch.
  adata.obs_names : ndarray, shape=(n_obs,)
    Ids for the cells.
  adata.var['feature_types']: ndarray, shape=(n_var,)
    The modality of this file, should be equal to "GEX", "ATAC" or "ADT".
  adata.var_names : ndarray, shape=(n_var,)
    Ids for the features.
```
