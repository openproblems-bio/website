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
