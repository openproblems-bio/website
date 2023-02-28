+++
title = "Denoising"
summary = "Removing noise in sparse single-cell RNA-sequencing count data"
headless = false
theme = "op"
+++

## The task

Single-cell RNA-Seq protocols only detect a fraction of the mRNA molecules present
in each cell. As a result, the measurements (UMI counts) observed for each gene and each
cell are associated with generally high levels of technical noise ([Grün et al.,
2014](https://openproblems.bio/bibliography#grn2014validation)). Denoising describes the
task of estimating the true expression level of each gene in each cell. In the
single-cell literature, this task is also referred to as *imputation*, a term which is
typically used for missing data problems in statistics. Similar to the use of the terms
"dropout", "missing data", and "technical zeros", this terminology can create confusion
about the underlying measurement process ([Sarkar and Stephens,
2021](https://openproblems.bio/bibliography#sarkar2021separating)).

A key challenge in evaluating denoising methods is the general lack of a ground truth. A
recent benchmark study ([Hou et al.,
2020](https://openproblems.bio/bibliography#hou2020systematic))
relied on flow-sorted datasets, mixture control experiments ([Tian et al.,
2019](https://openproblems.bio/bibliography#tian2019benchmarking)), and comparisons with
bulk RNA-Seq data. Since each of these approaches suffers from specific limitations, it
is difficult to combine these different approaches into a single quantitative measure of
denoising accuracy. Here, we instead rely on an approach termed molecular
cross-validation (MCV), which was specifically developed to quantify denoising accuracy
in the absence of a ground truth ([Batson et al.,
2019](https://openproblems.bio/bibliography#batson2019molecular)). In MCV, the observed
molecules in a given scRNA-Seq dataset are first partitioned between a *training* and a
*test* dataset. Next, a denoising method is applied to the training dataset. Finally,
denoising accuracy is measured by comparing the result to the test dataset. The authors
show that both in theory and in practice, the measured denoising accuracy is
representative of the accuracy that would be obtained on a ground truth dataset.

