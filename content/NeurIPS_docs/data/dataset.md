---
title: "The benchmarking dataset"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 3
---


{{% callout note  %}}
All the training data is released! Due to supply chain issues, we've had to deviate from the planned study design for Site 3 Multiome.

The currently available training batches are:

**Multiome**
* Site 1 - Donors 1, 2, 3
* Site 2 - Donors 1, 4, 5
* Site 3 - Donors 3, 6, 7, 10

**CITE**
* Site 1 - Donors 1, 2, 3
* Site 2 - Donors 1, 4, 5
* Site 3 - Donors 1, 6, 7

Site 4 Donors 1, 8, 9 will be used for testing for both Multiome and Cite

{{% /callout  %}}

We are currently in the process of creating a benchmarking dataset for the competition. There will be two types of data:
* Joint profiling of single-cell RNA and protein using the [10X Genomics
Single Cell Gene Expression with Feature Barcoding](https://support.10xgenomics.com/single-cell-gene-expression/overview/doc/getting-started-single-cell-gene-expression-with-feature-barcoding-technology) with the  [Biolegend TotalSeq™-B Universal Cocktail v1.0](https://www.biolegend.com/en-us/products/totalseq-a-human-universal-cocktail-v1-0-20321?GroupID=GROUP28) panel  
* Joint profiling of single-nucleus RNA and chromatin accessibility using the [10X Genomics Single Cell Multiome ATAC + Gene Expression Kit](https://www.10xgenomics.com/products/single-cell-multiome-atac-plus-gene-expression)  



## Download the data

The current forms of the data are public available on S3. To download the data, first install the AWS CLI on your computer: https://aws.amazon.com/cli/

You can download the data to your local computer with the following command (note the dataset size is roughly 1.2 GiB):

```sh
aws s3 sync s3://openproblems-bio/public/explore  /tmp/public/ --no-sign-request
```

You'll find the following files:

```sh
explore
├── LICENSE.txt
├── README.txt
├── cite/cite_adt_processed_training.h5ad
├── cite/cite_gex_processed_training.h5ad
├── multiome/multiome_atac_processed_training.h5ad
└── multiome/multiome_gex_processed_training.h5ad
```

These are all [AnnData](https://anndata.readthedocs.io/en/latest/) h5ad files, as described in the following section.

## Data file format

The training data is accessible in an [AnnData](https://anndata.readthedocs.io/en/latest/) h5ad file. More information can be found on AnnData objects [here](/neurips_docs/submission/quickstart/). You can load these files is to use the `AnnData.read_h5ad()` function. The easiest way to get started is to [spin up a free Jupyter Server on Saturn Cloud](/neurips_docs/about/explore).

```python
!pip install anndata
import anndata as ad

adata_gex = ad.read_h5ad("cite/cite_gex_processed_training.h5ad")
adata_adt = ad.read_h5ad("cite/cite_adt_processed_training.h5ad")
```

You can find code examples for exploring the data in our data [exploration notebooks](https://github.com/openproblems-bio/neurips2021-notebooks/tree/main/notebooks/explore).

## Preprocessing

To facilitate exploring the data, each dataset has been preprocessed to remove low quality cells and doublets. The following sections detail this process for each data modality.

### Preprocessing of gene expression (GEX)

In this dataset, gene expression was measured using 3' capture of nuclear RNA as described in the [10X Multiome Product Guide](https://www.10xgenomics.com/products/single-cell-multiome-atac-plus-gene-expression). Note, not all RNA is found in the nucleus. Comparisons of nuclear and cytosolic RNA have been previously reported (e.g. [Bakken 2018](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0209648); [Abdelmoez 2018](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-018-1446-9)) as have comparisons of single-nucleus and single-cell RNA sequencing ([Lake 2017](https://www.nature.com/articles/s41598-017-04426-w)).

For gene expression data, cells were filtered based on mitochondrial content, UMI counts per cell, and genes detected per cell. Size factors were then calculated using [scran](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0947-7) and stored in `adata.obs["size_factors"]`.

Counts were then normalized per cell by divided the UMI counts by the size factors. Original counts are stored in `adata.layers["counts"]`. The size factor normalized counts are stored in `adata.X`.

Finally, normalized counts are [log1p transformed](https://scanpy.readthedocs.io/en/stable/generated/scanpy.pp.log1p.html). These normalized counts are stores in `adata.layers["log_norm"]`.

More information about best practices for single-cell analysis can be found [here](https://www.embopress.org/doi/full/10.15252/msb.20188746).

### Preprocessing of ATAC

The chromatin accessibility data acquired by ATAC-seq as part of the 10X Multiome protocol was processed using [Signac](https://satijalab.org/signac/). Quality control, dimensionality reduction and translating peaks to gene activity scores was performed using Signac, following the authors' instructions. After loading the peak-by-cell matrix, counts were binarized to only represent an accessible versus non-accessible state of each region. Cells were then filtered based on 5 quality control metrics comprising the total number of fragments, the enrichment of fragments detected at transcription start sites (TSS), the fraction of fragments in peak regions compared to peak-flanking regions, the fraction of peaks blacklisted by the ENCODE consortium, and the nucleosome signal, which describes the length distribution of fragments which is expected to follow the length of DNA required span across one nucleosome or multiples of it.

Since ATAC data is sparser than gene expression data, peaks were included if they were accessible in at least 15 cells.

Finally, the data was binarized by setting all values `>0` to `1` and stored in `adata.X`. Raw UMI counts for each peak can be found in `adata.layers["counts"]`.

### Preprocessing of protein abundance (ADT)

The protein data was measured using the [TotalSeq™-B Human Universal Cocktail, V1.0](https://www.biolegend.com/en-us/products/totalseq-b-human-universal-cocktail-v1dot0-20960) of 134 cell surface markers and 6 isotype controls. The isotype controls are stored in `adata.obsm["isotype_controls"]`. These controls do not target any human proteins and their expression should be considered background.

The ADT protein measurements were run through quality control based on the total number of ADTs (ranging from 1100-1200 to 24000 across samples), the number of proteins captured in each cell (with a lower limit of 80) and the ADT count of the 6 isotype controls summed up in each cell (ranging from 1 to 100).

Since the total number of captured ADTs is limited, absolute ADT counts appear to be lower if highly abundant proteins are present. To account for this effect, normalization was performed using the centered log ratio (CLR) transformation. CLR counts are stored in `adata.X` and the raw counts are stored in `adata.layers["counts"]`.

## Metadata

More information about the features are available in the `.var` and `.obs` DataFrames of each object.


### Gene expression observation metadata

The GEX `adata` objects have the following columns:
* `.obs.index` - The cell barcode for that observation with the batch label appended.
* `.obs["n_genes_by_counts"]` - The number of genes with at least 1 count in a cell.
* `.obs["pct_counts_mt"]` - Percent of UMI counts mapped to mitochondrial genes.
* `.obs["n_counts"]` - Number of UMIs detected in the cell
* `.obs["n_genes"]` - Number of genes detected in the cell
* `.obs["size_factors"]` - The estimated size factor for the cell. See [OSCA Ch. 7 - Normalization](https://bioconductor.org/books/release/OSCA/normalization.html)
* `.obs["phase"]` - The [cell cycle](https://www.genome.gov/genetics-glossary/Cell-Cycle) phase for each cell as calculated by [scanpy.tl.score_genes_cell_cycle](https://scanpy.readthedocs.io/en/stable/generated/scanpy.tl.score_genes_cell_cycle.html)
* `.obs["leiden_final"]` -
* `.obs["atac_ann"]` - The cell type annotation of the cell from the joint ATAC data
* `.obs["cell_type"]` - The cell type annotation of the cells from the GEX data
* `.obs["pseudotime_order_GEX"]` - The [diffusion pseudotime](https://www.nature.com/articles/nmeth.3971) annotation for the developmental trajectories annotated in the data.
* `.obs["batch"]` - The batch from which the cell was sampled. Format is `s1d1` for Site 1 Donor 1.

For more info on how the QC metrics were calculated, consult [scanpy.pp.calculate_qc_metrics](https://scanpy.readthedocs.io/en/stable/generated/scanpy.pp.calculate_qc_metrics.html)

### Gene expression feature metadata

The GEX `adata.var` DataFrames have the following columns:

* `.var.index` - [Ensembl Gene Names](https://m.ensembl.org/info/genome/genebuild/gene_names.html) for each gene
* `.var["gene_ids"]` - [Ensembl Stable IDs](https://useast.ensembl.org/info/genome/stable_ids/index.html) used to uniquely track genes whose Gene Names may change over time.
* `.var["feature_types"]` - Denotes the each feature as a gene expression feature. Should be `GEX` for all genes
* `.var["genome"]` - The [Genome Assembly](https://www.ncbi.nlm.nih.gov/assembly/GCF_000001405.26/) used for read mapping.
* `.var["n_cells-[batch]"]` - The number of cells in `[batch]` in which the gene was detected.
* `.var["highly_variable-[batch]"]` - Whether the gene was determined to be [highly variable](https://scanpy.readthedocs.io/en/stable/generated/scanpy.pp.highly_variable_genes.html) in `[batch]`

### ATAC observation metadata

The ATAC `adata.obs` DataFrames have the following columns:
* `.obs.index` - The cell barcode for that observation with the batch label appended.
* `.obs["nCount_peaks"]` - The number of peaks detected in the cell.
* `.obs["atac_fragments"]` - Number of UMI counts in the cell (both in and not in peaks)
* `.obs["reads_in_peaks_frac"]` - Fraction of UMIs in peaks
* `.obs["blacklist_fraction"]` - Fraction of UMIs in [Encode Blacklisted](https://www.nature.com/articles/s41598-019-45839-z) regions
* `.obs["nucleosome_signal"]` - The [nucleosome signal](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-1929-3#Sec17), which describes the length distribution of fragments which is expected to follow the length of DNA required span across one nucleosome or multiples of it
* `.obs["phase"]` - The [cell cycle](https://www.genome.gov/genetics-glossary/Cell-Cycle) phase for each cell as calculated by [scanpy.tl.score_genes_cell_cycle](https://scanpy.readthedocs.io/en/stable/generated/scanpy.tl.score_genes_cell_cycle.html)
* `.obs["leiden_final"]` -
* `.obs["rna_ann"]` - The cell type annotation of the cell from the joint RNA data
* `.obs["cell_type"]` - The cell type annotation of the cells from the ATAC data
* `.obs["pseudotime_order_ATAC"]` - The [diffusion pseudotime](https://www.nature.com/articles/nmeth.3971) annotation for the developmental trajectories annotated in the data.
* `.obs["batch"]` - The batch from which the cell was sampled. Format is `s1d1` for Site 1 Donor 1.

For more info on how the QC metrics were calculated, consult the [Signac documentation](https://satijalab.org/signac/).

### ATAC feature metadata

The ATAC `adata.var` DataFrames have the following columns:

* `.var.index` - [Genomic coordinates](https://www.idtdna.com/pages/support/faqs/how-are-genomic-coordinates-defined) for each [ATAC peak](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-020-1929-3) that are directly related to the reference genome, and include the chromosome name*, start position, and end position in the following format: `chr1-1234570-1234870`.
* `.var["feature_types"]` - Denotes the each feature as a gene expression feature. Should be `ATAC` for all peaks
* `.var["n_cells-[batch]"]` - The number of cells in `[batch]` in which the peak was detected.

*For the curious, chromosome names like `KI270726.1` represent scaffold that are either unlocalized or unplaced (see [Genome Assemblies from Ensembl](https://grch37.ensembl.org/info/genome/genebuild/assembly.html))

There is also information about the observations in the `.obs` DataFrame of each AnnData object.
