+++
title = "Dimensionality reduction for visualisation"
summary = "Reduction of high-dimensional datasets to 2D for visualization & interpretation"
headless = false
theme = "op"
+++

## The task

Dimensionality reduction is one of the key challenges in single-cell data
representation. Routine single-cell RNA sequencing (scRNA-seq) experiments measure cells
in roughly 20,000-30,000 dimensions (i.e., features - mostly gene transcripts but also
other functional elements encoded in mRNA such as lncRNAs). Since its inception,
scRNA-seq experiments have been growing in terms of the number of cells measured.
Originally, cutting-edge SmartSeq experiments would yield a few hundred cells, at best.
Now, it is not uncommon to see experiments that yield over [100,000
cells](<https://www.nature.com/articles/s41586-018-0590-4>) or even [> 1 million
cells.](https://doi.org/10.1126/science.aba7721)

Each *feature* in a dataset functions as a single dimension. While each of the ~30,000
dimensions measured in each cell contribute to an underlying data structure, the overall
structure of the data is challenging to display in few dimensions due to data sparsity
and the [*"curse of
dimensionality"*](https://en.wikipedia.org/wiki/Curse_of_dimensionality) (distances in
high dimensional data don’t distinguish data points well). Thus, we need to find a way
to [dimensionally reduce](https://en.wikipedia.org/wiki/Dimensionality_reduction) the
data for visualization and interpretation.

## The metrics

* **Root mean square error**: the square root of the mean squared difference between
  ground truth distances in the high-dimensional data and Euclidean distances in the
  dimension-reduced data, invariant to scalar multiplication. *RMSE* computes
  high-dimensional distances in Euclidean space, while *RMSE (spectral)* computes
  [diffusion distances](http://dx.doi.org/10.1016/j.acha.2006.04.006) (i.e. Euclidean
  distances on the [Laplacian Eigenmap](http://dx.doi.org/10.1162/089976603321780317)).
* **Trustworthiness**: a measurement of similarity between the rank of each point's
  nearest neighbors in the high-dimensional data and the reduced data ([Venna & Kaski,
  2001](http://dx.doi.org/10.1007/3-540-44668-0_68)).
* **Density preservation**: similarity between local densities in the high-dimensional
  data and the reduced data ([Narayan, Berger & Cho,
  2020](https://doi.org/10.1038/s41587-020-00801-7))
* **NN Ranking**: a set of metrics from
  [pyDRMetrics](https://doi.org/10.17632/jbjd5fmggh.2) relating to the preservation
  of nearest neighbors in the high-dimensional data and the reduced data.

