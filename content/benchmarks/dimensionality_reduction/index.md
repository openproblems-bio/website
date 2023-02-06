---
title: "Dimensionality reduction for visualisation"
summary: "Reduction of high-dimensional datasets to 2D for visualization & interpretation"
---

<script src="index_files/libs/htmlwidgets-1.5.4/htmlwidgets.js"></script>
<link href="index_files/libs/datatables-css-0.0.0/datatables-crosstalk.css" rel="stylesheet" />
<script src="index_files/libs/datatables-binding-0.25/datatables.js"></script>
<script src="index_files/libs/jquery-3.6.0/jquery-3.6.0.min.js"></script>
<link href="index_files/libs/dt-core-1.11.3/css/jquery.dataTables.min.css" rel="stylesheet" />
<link href="index_files/libs/dt-core-1.11.3/css/jquery.dataTables.extra.css" rel="stylesheet" />
<script src="index_files/libs/dt-core-1.11.3/js/jquery.dataTables.min.js"></script>
<link href="index_files/libs/dt-ext-select-1.11.3/css/select.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-select-1.11.3/js/dataTables.select.min.js"></script>
<link href="index_files/libs/dt-ext-searchpanes-1.11.3/css/searchPanes.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-searchpanes-1.11.3/js/dataTables.searchPanes.min.js"></script>
<script src="index_files/libs/jszip-1.11.3/jszip.min.js"></script>
<link href="index_files/libs/dt-ext-buttons-1.11.3/css/buttons.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/dataTables.buttons.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.html5.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.colVis.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.print.min.js"></script>
<link href="index_files/libs/crosstalk-1.2.0/css/crosstalk.min.css" rel="stylesheet" />
<script src="index_files/libs/crosstalk-1.2.0/js/crosstalk.min.js"></script>
<script src="index_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="index_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


## Description

## The task

Dimensionality reduction is one of the key challenges in single-cell data
representation. Routine single-cell RNA sequencing (scRNA-seq) experiments measure cells
in roughly 20,000-30,000 dimensions (i.e., features - mostly gene transcripts but also
other functional elements encoded in mRNA such as lncRNAs). Since its inception,
scRNA-seq experiments have been growing in terms of the number of cells measured.
Originally, cutting-edge SmartSeq experiments would yield a few hundred cells, at best.
Now, it is not uncommon to see experiments that yield over [100,000
cells](https://openproblems.bio/bibliography#tabula2018single) or even [\> 1 million
cells.](https://openproblems.bio/bibliography#cao2020human)

Each *feature* in a dataset functions as a single dimension. While each of the \~30,000
dimensions measured in each cell contribute to an underlying data structure, the overall
structure of the data is challenging to display in few dimensions due to data sparsity
and the [*"curse of
dimensionality"*](https://en.wikipedia.org/wiki/Curse_of_dimensionality) (distances in
high dimensional data don't distinguish data points well). Thus, we need to find a way
to [dimensionally reduce](https://en.wikipedia.org/wiki/Dimensionality_reduction) the
data for visualization and interpretation.

## The metrics

-   **Distance correlation**: the Spearman correlation between
    ground truth distances in the high-dimensional data and Euclidean distances in the
    dimension-reduced data, invariant to scalar multiplication. *Distance correlation*
    computes high-dimensional distances in Euclidean space, while *Distance correlation
    (spectral)* computes [diffusion distances](http://dx.doi.org/10.1016/j.acha.2006.04.006)
    (i.e. Euclidean distances on the [Laplacian Eigenmap](http://dx.doi.org/10.1162/089976603321780317)).
-   **Trustworthiness**: a measurement of similarity between the rank of each point's
    nearest neighbors in the high-dimensional data and the reduced data ([Venna & Kaski,
    2001](https://openproblems.bio/bibliography#venna2001neighborhood)).
-   **Density preservation**: similarity between local densities in the high-dimensional
    data and the reduced data ([Narayan, Berger & Cho,
    2020](https://openproblems.bio/bibliography#narayan2021assessing))
-   **NN Ranking**: a set of metrics from
    [pyDRMetrics](https://openproblems.bio/bibliography#zhang2021pydrmetrics) relating to
    the preservation of nearest neighbors in the high-dimensional data and the reduced
    data.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="902" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **continuity**<sup><a href="/bibliography#zhang2021pydrmetrics" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **density preservation**<sup><a href="/bibliography#narayan2021assessing" target="_blank">2</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Distance correlation**<sup><a href="/bibliography#schober2018correlation" target="_blank">3</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Distance correlation (spectral)**<sup><a href="/bibliography#coifman2006diffusion" target="_blank">4</a></sup>: Missing 'metric_description'.

<!-- -->

-   **local continuity meta criterion**<sup><a href="/bibliography#zhang2021pydrmetrics" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **global property**<sup><a href="/bibliography#zhang2021pydrmetrics" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **local property**<sup><a href="/bibliography#zhang2021pydrmetrics" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **co-KNN size**<sup><a href="/bibliography#zhang2021pydrmetrics" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **co-KNN AUC**<sup><a href="/bibliography#zhang2021pydrmetrics" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **trustworthiness**<sup><a href="/bibliography#venna2001neighborhood" target="_blank">5</a></sup>: Missing 'metric_description'.

## Results

<div id="htmlwidget-9cc1f38189dd947313ca" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-9cc1f38189dd947313ca">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["densMAP (logCP10k) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","UMAP (logCP10k) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","NeuralEE (CPU) (Default) <sup><a href=\"/bibliography#xiong2020neuralee\" target=\"_blank\">7<\/a><\/sup>","PyMDE Preserve Neighbors (logCP10k) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k) <sup><a href=\"/bibliography#vandermaaten2008visualizing\" target=\"_blank\">9<\/a><\/sup>","densMAP PCA (logCP10k) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","densMAP PCA (logCP10k) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","densMAP PCA (logCP10k, 1kHVG) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","densMAP (logCP10k, 1kHVG) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","densMAP (logCP10k) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","UMAP PCA (logCP10k) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","UMAP PCA (logCP10k) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","PHATE (default) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","PHATE (logCP10k) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","NeuralEE (CPU) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#xiong2020neuralee\" target=\"_blank\">7<\/a><\/sup>","densMAP PCA (logCP10k) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","PyMDE Preserve Distances (logCP10k) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","densMAP PCA (logCP10k, 1kHVG) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k) <sup><a href=\"/bibliography#vandermaaten2008visualizing\" target=\"_blank\">9<\/a><\/sup>","densMAP (logCP10k, 1kHVG) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","PyMDE Preserve Neighbors (logCP10k) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","NeuralEE (CPU) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#xiong2020neuralee\" target=\"_blank\">7<\/a><\/sup>","densMAP (logCP10k) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","PHATE (gamma=0) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k) <sup><a href=\"/bibliography#vandermaaten2008visualizing\" target=\"_blank\">9<\/a><\/sup>","PyMDE Preserve Neighbors (logCP10k, 1kHVG) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","Principle Component Analysis (PCA) (logCP10k) <sup><a href=\"/bibliography#pearson1901pca\" target=\"_blank\">11<\/a><\/sup>","PyMDE Preserve Neighbors (logCP10k, 1kHVG) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","UMAP (logCP10k, 1kHVG) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#vandermaaten2008visualizing\" target=\"_blank\">9<\/a><\/sup>","PyMDE Preserve Neighbors (logCP10k) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#vandermaaten2008visualizing\" target=\"_blank\">9<\/a><\/sup>","PHATE (logCP10k, 1kHVG) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","PHATE (logCP10k) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","PHATE (gamma=0) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","UMAP PCA (logCP10k, 1kHVG) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","Principle Component Analysis (PCA) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#pearson1901pca\" target=\"_blank\">11<\/a><\/sup>","UMAP PCA (logCP10k) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","UMAP (logCP10k) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","densMAP PCA (logCP10k, 1kHVG) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","PHATE (logCP10k, 1kHVG) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","Principle Component Analysis (PCA) (logCP10k) <sup><a href=\"/bibliography#pearson1901pca\" target=\"_blank\">11<\/a><\/sup>","densMAP (logCP10k, 1kHVG) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","PHATE (default) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","PyMDE Preserve Distances (logCP10k, 1kHVG) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","NeuralEE (CPU) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#xiong2020neuralee\" target=\"_blank\">7<\/a><\/sup>","NeuralEE (CPU) (Default) <sup><a href=\"/bibliography#xiong2020neuralee\" target=\"_blank\">7<\/a><\/sup>","Principle Component Analysis (PCA) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#pearson1901pca\" target=\"_blank\">11<\/a><\/sup>","NeuralEE (CPU) (Default) <sup><a href=\"/bibliography#xiong2020neuralee\" target=\"_blank\">7<\/a><\/sup>","PyMDE Preserve Neighbors (logCP10k, 1kHVG) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","PyMDE Preserve Distances (logCP10k) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","PHATE (logCP10k) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#vandermaaten2008visualizing\" target=\"_blank\">9<\/a><\/sup>","PHATE (gamma=0) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","Principle Component Analysis (PCA) (logCP10k) <sup><a href=\"/bibliography#pearson1901pca\" target=\"_blank\">11<\/a><\/sup>","PHATE (default) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","UMAP (logCP10k) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","UMAP (logCP10k, 1kHVG) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","densMAP (logCP10k) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","densMAP PCA (logCP10k) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","UMAP PCA (logCP10k, 1kHVG) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","PHATE (logCP10k, 1kHVG) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","UMAP (logCP10k, 1kHVG) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","Principle Component Analysis (PCA) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#pearson1901pca\" target=\"_blank\">11<\/a><\/sup>","UMAP PCA (logCP10k, 1kHVG) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","PyMDE Preserve Distances (logCP10k) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k) <sup><a href=\"/bibliography#vandermaaten2008visualizing\" target=\"_blank\">9<\/a><\/sup>","PyMDE Preserve Distances (logCP10k) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","PyMDE Preserve Distances (logCP10k, 1kHVG) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","PyMDE Preserve Distances (logCP10k, 1kHVG) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","UMAP (logCP10k) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","PyMDE Preserve Neighbors (logCP10k) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","UMAP PCA (logCP10k) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","NeuralEE (CPU) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#xiong2020neuralee\" target=\"_blank\">7<\/a><\/sup>","densMAP (logCP10k, 1kHVG) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","PyMDE Preserve Neighbors (logCP10k, 1kHVG) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","densMAP PCA (logCP10k, 1kHVG) <sup><a href=\"/bibliography#narayan2021assessing\" target=\"_blank\">2<\/a><\/sup>","PyMDE Preserve Distances (logCP10k, 1kHVG) <sup><a href=\"/bibliography#agrawal2021mde\" target=\"_blank\">8<\/a><\/sup>","t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#vandermaaten2008visualizing\" target=\"_blank\">9<\/a><\/sup>","Principle Component Analysis (PCA) (logCP10k) <sup><a href=\"/bibliography#pearson1901pca\" target=\"_blank\">11<\/a><\/sup>","UMAP PCA (logCP10k, 1kHVG) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","UMAP (logCP10k, 1kHVG) <sup><a href=\"/bibliography#mcinnes2018umap\" target=\"_blank\">6<\/a><\/sup>","NeuralEE (CPU) (Default) <sup><a href=\"/bibliography#xiong2020neuralee\" target=\"_blank\">7<\/a><\/sup>","PHATE (gamma=0) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","PHATE (default) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","Principle Component Analysis (PCA) (logCP10k, 1kHVG) <sup><a href=\"/bibliography#pearson1901pca\" target=\"_blank\">11<\/a><\/sup>","PHATE (logCP10k) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>","PHATE (logCP10k, 1kHVG) <sup><a href=\"/bibliography#moon2019visualizing\" target=\"_blank\">10<\/a><\/sup>"],["Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Overall mean","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Overall mean","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Overall mean","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Overall mean","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Overall mean","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Overall mean","Overall mean","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","5k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2019pbmc\" target=\"_blank\">13<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Overall mean","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Mouse myeloid lineage differentiation <sup><a href=\"/bibliography#olsson2016single\" target=\"_blank\">12<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>","Mouse hematopoietic stem cell differentiation <sup><a href=\"/bibliography#nestorowa2016single\" target=\"_blank\">14<\/a><\/sup>"],[0.716919205897347,0.6071008475787,0.561064340538389,0.55836343466235,0.550239627918363,0.547893119257068,0.547702745517425,0.535230845179018,0.526134366209654,0.511599973903663,0.504702609602798,0.49241460621469,0.49205193609608,0.490010095594666,0.486225979613032,0.484022096444771,0.479977051989744,0.478787493036964,0.474175348020033,0.467572015160139,0.464266214542565,0.461883111293331,0.459304960669095,0.454433069780878,0.452163265789766,0.4508512714821,0.44768154423545,0.445823538835605,0.444600035925496,0.440874890758484,0.438519749220916,0.434566920394272,0.434496959122161,0.432738463797541,0.432016492087508,0.430371221309788,0.428736897397162,0.425059565242819,0.42233357162542,0.420940220775172,0.420649976708485,0.41998975180086,0.41632285446164,0.408617123033281,0.406374010186916,0.403874817005835,0.390671612343826,0.388151555925842,0.382295129840706,0.381833798967917,0.380114951385045,0.375300359907798,0.373076364363905,0.369599557164506,0.368884457640884,0.368883764746452,0.366806522394018,0.362144188314711,0.358575755144547,0.356470424559819,0.354940145283338,0.348908923612988,0.347006637114599,0.34079805053507,0.339946586613957,0.336321966382503,0.332074821430902,0.324045835782888,0.318446634165274,0.302012941665332,0.293093344903543,0.292929598457832,0.27806147991097,0.263515360111142,0.255262182015126,0.248826586586046,0.248802324109534,0.246952950643575,0.24378728193896,0.238982076886343,0.234528393248746,0.234275687103591,0.228655366652382,0.222349109625133,0.205982235109995,0.205505698282207,0.203152520331186,0.191579835008319],[0.960344007455354,0.952131120947567,0.961647004551449,0.9457369554546,0.954390877161558,0.715396200753174,0.954010843382656,0.935890379940841,0.657745451847242,0.722712434898157,0.942835248006259,0.693496982314972,0.940900438416025,0.934655819341168,0.914317168520226,0.635297349826744,0.667857369605826,0.64737517179642,0.666212560184241,0.913652574099405,0.716973493696809,0.662986399959896,0.706713486743055,0.685028311427868,0.641526063651966,0.658450767879823,0.917728009706154,0.933460292891307,0.641415195379428,0.631067015273901,0.639148142388571,0.942645146627306,0.609782675808035,0.681025566187168,0.931412098389715,0.638177601105234,0.924338806281626,0.597590367735139,0.717732984032854,0.595873558990393,0.930437427497446,0.62840880742173,0.595304918401347,0.63820206276748,0.533629434749193,0.636647452500708,0.59257722651426,0.594443157215933,0.474009362199062,0.615613780422978,0.555808152051704,0.624686997193882,0.629982651927438,0.597127452167105,0.581256474008377,0.589707089282588,0.728613988619358,0.906373127607029,0.501079810496062,0.236485005344402,0.93423083714733,0.604828484473639,0.608064178345853,0.572791735710445,0.612192710811529,0.372625412187034,0.303974753610098,0.626941674362252,0.431398389362251,0.572678798795855,0.472453842531636,0.254733978014305,0.156438872884185,0.332638789022002,0.214516729257394,0.254930280497803,0.204355125233918,0.187886934541703,0.316235793881108,0.197632604897247,0.264169694182022,0.2764042120511,0.342075312792268,0.174941946683732,0.190018766664259,0.199593243633775,0.258379606053312,0.274265350115437],[1.15101090360284,0.132092760872108,0.33577639313298,0.116881186555732,0.548420764644782,0.697383643128893,1.05078896051817,0.916428533843486,0.633140076021223,0.899929260606263,0.140047065817504,0.129663383408589,-0.0459176922055718,0.204434408449497,0.55794593162055,0.821384092729116,0.513493081971024,0.536597001429284,0.153345879810549,0.87395934505356,0.125086144527444,0.280842944374194,0.861098778726014,0.248292061934603,0.361908819184476,0.0695981344743066,0.266997562726798,-0.0421803712312748,0.0886738831933094,0.243084920322086,0.14684717994172,0.204554720129498,0.107145662494195,0.263958077584999,-0.406938441152526,0.0540911365420068,0.765690230328046,0.111416562284191,0.187103962900711,0.587209633421107,0.350451327400214,0.485690964855126,0.622003860531901,0.214320694910269,0.319689131673496,0.375260233270955,0.148422443340886,0.22667430377918,-0.01589962282068,0.0742449826126318,0.510997233199608,-0.0128655585084382,0.210473274733265,-0.133157680273505,0.199615016529824,-0.0797689601025747,0.0385434726181107,-0.0854127097115491,0.687678099489932,0.71597967454028,-0.18454845116,0.0595811132159043,0.0472999148973587,0.347036104192344,-0.0040475706815963,0.380792051030549,0.383959813098098,0.638706566597252,0.461464667017003,0.87689890300081,0.390675655211914,0.198574208741982,0.0645392376264797,0.28699182381812,0.358912160520921,0.195317184594864,0.308603364990551,0.187805966376702,0.183780183748212,-0.153843477992451,0.118314602573205,0.138638571210316,0.125390559710359,-0.240826661602591,-0.407709883012421,0.0487437784698051,-0.506989161559811,-0.278853650246696],[0.64405743504552,0.627087821338393,0.599564822202342,0.5726791539781,0.400919714792247,0.761931682032816,0.338047468102552,0.560702445486943,0.512680475539296,0.712379763319494,0.492019345002484,0.763707061242891,0.615290527445373,0.592722450730076,0.462192883286977,0.576085266239045,1.01211608354177,0.469437197914438,0.686528834549629,0.402307912962151,0.556583423553536,0.512026303679674,0.882304029126287,0.565897261756579,0.569789035605546,0.510607045935578,0.33733930990875,0.589734829181762,0.514400980181514,0.364053197085731,0.557856993942593,0.420034892538634,0.555824462017403,0.583351389258053,0.572867755026088,0.443687353458155,0.316336584522845,0.60308897048029,0.646725460826058,0.440989637211764,0.452678329332311,0.993976649673868,0.408481478869966,0.602186673977615,0.548705072660744,0.443939745858936,0.549251072634456,0.536207970470864,0.70954600134297,0.493852505276974,0.809957228377465,0.529431974732915,0.370892408911839,0.515279584165079,0.648099824845065,0.54541366119077,0.865231127304444,0.392779074082447,0.610777825786674,0.628276648581768,0.319929850010203,0.430371064519863,0.404432767464086,0.356457227247923,0.370086139401963,0.866698693801643,0.621918557474762,0.551056907788979,0.427577816734811,0.339032482393153,0.447857433835336,0.544308404296144,0.553540505195494,0.357600050610157,0.31045604810845,0.381215640713581,0.29282926823391,0.394995895150537,0.328589137111152,0.612983514952578,0.346641214737531,0.306118248128297,0.338642394358057,0.407073735712568,0.41876378214932,0.216827126750061,0.412222084210615,0.282610402209875],[1.84737913736224,2.05732748915735,1.33015648533406,1.7298362967269,1.32306401581745,1.25278985570963,1.09250012929818,0.741914131129767,1.59568438249164,1.04298071750094,1.31575178933952,1.28063905251967,1.43185006576503,1.26100642542443,0.851012723953746,1.10129383556513,0.53831640439776,1.37069339452311,1.23853979229461,0.801094586727822,1.36735712127698,1.34152899226881,0.263817352276619,1.19730676525353,1.16013541669346,1.44471025860097,1.45386058541628,0.920200763064435,1.47438436693895,1.51729725444691,1.35803733277348,0.721123829560164,1.27541209742717,1.04890488121342,1.25233586432397,1.48363237044081,0.20327733060671,1.2034971767514,1.06492368864317,1.02951403617745,0.554583125492635,0.159632304142568,1.12004469396934,0.899523385431099,1.02036402241743,1.03727020733744,1.02408309551068,0.932454851221518,0.838019802825359,1.09452463555596,0.857364581873052,1.1355427226019,1.01054888552472,1.19999651463493,0.897093465045765,1.15493764907231,0.170161541223167,0.737967562881686,1.01774566286396,0.958591521687571,0.609854420358358,0.930006494814715,1.04065948159926,0.725749453490305,0.997477409809569,0.85412104332181,0.918802441968318,1.17965629789958,0.661721593659608,0.0115434897612555,0.967282035549009,0.976918580316561,1.01410068839499,0.919268905789778,0.963355112688542,0.918662885002467,0.975934582879477,0.953257268800133,0.793225572567091,1.07778750557844,0.898945438629541,0.909626514977153,0.904072998372624,1.15034691432728,1.13343949602081,1.04151617864269,1.09671686116786,0.960024261524343],[0.530893975161655,0.480293544082931,0.498101200862157,0.463306989633583,0.515139074207123,0.0450486109393167,0.497536693010366,0.437750179616135,0.0378621082057245,0.210370353770299,0.465257107667043,0.0430880934121663,0.414246125423381,0.407420712306271,0.419224058298265,0.20978635217097,0.0240642703411424,0.038257922469881,0.0471018974346288,0.423842758903828,0.0436447072211365,0.031158004106573,0.0227222126017366,0.0364891274769314,0.218907163707424,0.039006258813052,0.384686441547778,0.444421636046392,0.0372931252009994,0.0426428023649902,0.197657856572899,0.467053269013651,0.0317517255028078,0.0398164411349974,0.388997228779637,0.037453924745813,0.436980396181874,0.199802695187715,0.192550497723278,0.175444259136897,0.404546854151699,0.0234272567597655,0.170454367869965,0.0356665759592311,0.0198092670014596,0.16728388181779,0.184852398122176,0.0232973802043391,0.0213739702644534,0.179130783818493,0.0844009715914795,0.172768957731733,0.188661506590784,0.164909213762442,0.154276678200942,0.17256146778828,0.0251774979590827,0.418248999281535,0.0774948735475051,0.0867737525632262,0.419172739402648,0.160356532703245,0.170137418117555,0.167147729973349,0.171097017463932,0.0485987696514012,0.0944805194805195,0.180539874781895,0.113697655050875,0.282613158164836,0.0721804511278196,0.0860218728639781,0.0910628844839371,0.0514695830485304,0.0496582365003418,0.0539644565960355,0.0503246753246753,0.0386705399863295,0.0562884483937115,0.0547163362952837,0.0566643882433356,0.0548701298701299,0.035082023239918,0.0692412850307587,0.0677717019822283,0.0411654135338346,0.0710697197539303,0.044771018455229],[-0.0409592330653478,-0.135006199622915,-0.100415874072712,-0.151187585045637,-0.198407734100849,0.559409517410454,-0.310647729169397,-0.0886449399009579,0.508461751908686,0.208374567988021,-0.196772440924613,0.580127758875653,-0.191544184684303,-0.23128993299292,-0.10663479750316,0.142407170116085,0.658454853981899,0.459374121426287,0.550182354141701,-0.346337454467359,0.476858819473489,0.514491538911185,0.537473411838244,0.497536596051245,0.181576582811153,0.517129785884617,-0.380267872046782,-0.141429431015897,0.477836255603702,0.406138322872388,0.159232380750717,-0.208430655207294,0.511016594830827,0.433694910115396,-0.146030058103141,0.439719295949542,-0.157301056905426,0.180188167414029,0.17964160910474,0.166768690001498,-0.206494837994689,0.597681402035241,0.0983271666734068,0.44120405482255,0.522313387449903,0.188314827253907,0.1758177478722,0.487820920738923,0.50829168819296,0.170625733848846,0.143764189939282,0.102319016329984,0.119806423096676,0.146632234689632,0.111950812162499,0.113755545573897,0.567794274073791,-0.339563135603598,0.128609525191166,0.178459722107198,-0.289427136792984,0.14778387705974,0.08640283893012,0.147365795340286,0.0910008959033931,0.251330046746698,0.192955128392606,-0.478492330910751,0.17596800220323,-0.190365817746727,0.106136752863344,0.152025907824298,0.157209184291047,0.157087740353697,0.132857202578894,0.136176846677817,0.129576888479166,0.195956436906514,0.161711601624934,0.11843890649904,0.122710528553622,0.120935396790255,0.119577429496351,0.088390166120791,0.0916067665834444,0.11157752218736,0.104552071867475,0.138829874343081],[0.191073304243703,0.180007451690307,0.180600218557358,0.155613350149878,0.161801030422612,0.397280459691745,0.131876516962433,0.116541365639162,0.383815045239682,0.255104554972298,0.155825282976279,0.376407337141934,0.0966253774523509,0.0962193434036381,0.0658870943676657,0.23805665480907,0.36105846200348,0.367963361856571,0.344768466298165,0.0277872416045552,0.379862092636362,0.379473080089912,0.391259495617399,0.371348627139078,0.229982772484324,0.365709850866925,0.069459901023256,0.0419525630164762,0.359107404149654,0.331780317180912,0.235316802301351,0.0815339720602245,0.372382794408224,0.360512195529124,0.0777039192369072,0.347197197828777,0.113045054855873,0.237069314975703,0.238027100900867,0.213777487942103,0.0838786712684606,0.356884229006247,0.188579670006428,0.357046149366505,0.331613078825667,0.201157548125488,0.229595871028426,0.339160354538243,0.360240163701098,0.188565614904317,0.0996887283707764,0.204473741419133,0.192272804163642,0.198090805462479,0.189036305111598,0.199576304326165,0.365590887596856,0.0185070252022364,0.182980865055792,0.185012987773033,0.119877716076708,0.202024209098721,0.178131191573005,0.200034991355926,0.210127206903461,0.153649005128728,0.183378820732195,-0.215641282019879,0.127998041287129,-0.110108828191947,0.168482963415438,0.170474964117814,0.178975324808895,0.158112469918886,0.154136723175048,0.15803443082955,0.156827736330574,0.162489873227666,0.163504123249789,0.140764785305291,0.1633067068049,0.156779145367125,0.147947230826823,0.145219870011452,0.14505738615964,0.147899564673662,0.156689685324636,0.149811161619478],[0.531739912618864,0.481058853765099,0.498894885633513,0.464045232588024,0.515959907478797,0.0450572494293614,0.498329478283218,0.438447699820098,0.0378693686170443,0.210667476448783,0.465998457979954,0.0430963559547448,0.414906193780519,0.408069904908764,0.419892058596762,0.210068823865348,0.0240688848887487,0.0382652587822666,0.047110929661452,0.424518118735544,0.0436530764995886,0.0311639789435918,0.0227265697972919,0.0364961246064295,0.219200477545613,0.03901373862589,0.385299408892316,0.445129786687227,0.0373002765045373,0.0426509795188697,0.19792192492164,0.467797481367258,0.0317578141914253,0.0398240763078293,0.389617065021845,0.0374611068841588,0.437676689796967,0.200068654346553,0.192819962511581,0.175688102239701,0.405191467489077,0.0234317491540941,0.170690681140987,0.0356734153568269,0.0198130656126091,0.16751763339943,0.185124523921863,0.0233018476936305,0.0213780689220035,0.179378861278981,0.0845069877786252,0.173000456310174,0.188922247652087,0.165130391174227,0.154492164925464,0.172795743694451,0.0251823259784364,0.418915445900797,0.077535946930192,0.0868197438834653,0.419840657928553,0.160581343136948,0.17037164474098,0.167388589759257,0.171332061995308,0.0486245276889671,0.0945305954965891,0.18082755075816,0.113855860453044,0.283063479825238,0.0722187077912086,0.0860674656773068,0.0911111491049599,0.0514968626579357,0.0496845560703722,0.053993058523825,0.0503513481167399,0.0386910359212843,0.0563182820701328,0.0547453367299834,0.0566944211732121,0.0548992118176067,0.0351006172100737,0.0692779838944075,0.0678076219460069,0.0411872317871737,0.0711073877139291,0.0447947477303425],[0.426638756361119,0.375856692124321,0.39557703065019,0.365163161918216,0.350077950199752,0.371793547653768,0.296371363469984,0.38874830471462,0.311105897619592,0.283856219200686,0.344542060283765,0.378249247411802,0.338674083589336,0.320664605525365,0.37841030853882,0.260597693028317,0.432926291805259,0.270919244687431,0.350285374565345,0.267928005046415,0.298253737841684,0.310374735422419,0.361117788312255,0.298446315539332,0.275564484453129,0.310582728404914,0.248411457006014,0.364304757107211,0.274273897331335,0.237432634703394,0.252050348452234,0.337850216556066,0.301678471031883,0.253929018372854,0.356639904214452,0.253904068916662,0.357141296513613,0.271674283284211,0.250105870559464,0.235765414264546,0.330840788154031,0.378382825970478,0.208927347401322,0.254377941114637,0.278600967668498,0.251705311520527,0.248368469721009,0.265586740729418,0.318233728463452,0.243284917767229,0.246836877505341,0.205584004112808,0.218099577784439,0.230196139832575,0.225134492049203,0.209790808554006,0.34310380045756,0.270015620142231,0.0638121129286844,0.113628167961199,0.296050139252187,0.227436940849478,0.194780748098703,0.210318997821749,0.196715347802453,0.154500950095883,0.126330128594291,0.153083390614879,0.221450828040824,0.310842586219361,0.0313571190965127,0.0927341455968009,0.0922315421570674,0.0663308906003415,0.0477481395379595,0.0549672677895614,0.0476286933915873,0.0749089302346135,0.079015882093858,0.0486091931711159,0.0401918352385096,0.0400527268225424,0.0312946500493845,0.0355021997439422,0.036320400958046,0.00822895622221465,0.042158388440205,0.0497915633625194],[0.927013860187514,0.92015894143184,0.910741238532558,0.921559604664104,0.931030678560155,0.632840425821521,0.928213731316083,0.904530351500083,0.582979104606411,0.56962439033169,0.921522179879785,0.635670789864471,0.905488425978658,0.906197218850376,0.900012366450471,0.645243726097885,0.56741481736053,0.588992255483952,0.65767739126001,0.88696706293547,0.634389528698617,0.554785135177056,0.543816481652047,0.607489506623189,0.663041841760571,0.553704145334919,0.793300638173931,0.90264056260841,0.541314974771531,0.592601463815656,0.641128530163951,0.911506331297208,0.548217293509644,0.622368082271561,0.90355958513813,0.568388157226722,0.89018364178949,0.646199459968966,0.553704579051475,0.588371388366258,0.900386614293664,0.552381328989479,0.58041435975174,0.607970276626592,0.469202673810151,0.569651328973167,0.568623274772301,0.452568032666374,0.587758135316385,0.579116174192763,0.407824563163119,0.618061287153884,0.601103863254158,0.611790916030101,0.527889343530104,0.610068338084622,0.538666308109377,0.883610873364293,0.238042829155509,0.374677021156052,0.904420680610382,0.56611917625763,0.56978618737907,0.51368988045912,0.583484646729561,0.232279164172318,0.400417455461547,0.423779707956509,0.449333487843968,0.643931164431485,0.202288487613208,0.367436457129132,0.381405410162642,0.254156485291974,0.27129691171334,0.28100381463496,0.27159155811474,0.234866625290269,0.29920379464961,0.237986063426901,0.277645102351579,0.284432714001388,0.20737045046796,0.324323656328985,0.316746311648617,0.198317966921495,0.325618560339714,0.249753620969583],[210,170,180,570,1499,259,180,160,350,326.666666666667,219,319,520,230,170,256,2541,240,1679,180,1342,160,420,289,1619,669,170,229,370,479,1020.66666666667,250,399,250,131,219,180,292.333333333333,232.666666666667,193.333333333333,170,190,236.666666666667,809,2771,156.666666666667,649.333333333333,180,1019,363,1137,246.666666666667,369.333333333333,223,166.666666666667,563,269,300,350,329,219,259.333333333333,330,186.333333333333,222.333333333333,530,1679,340,1063.33333333333,170,259,1150,339,140,180,191,180,249,379,140,229,320,749,249,360,199,260,209],[37.3,77.8,210.6,1243.7,186.1,920.7,361.2,105.2,97,121.1,423,568.5,132.3,277.9,234.4,658.966666666667,2503.7,145.7,190.8,77.6,1307.5,766.9,249.9,538.3,187.433333333333,600,46.3,214.9,111.8,788.9,1004.86666666667,338.2,402,763.3,386.1,104.4,29.1,563.366666666667,164.633333333333,119.066666666667,245.2,154.5,90,268.7,233.9,451.766666666667,313.966666666667,21.7,263.2,340.033333333333,1288.2,504.3,495.133333333333,391.1,184.866666666667,324.933333333333,328.1,93.8,76.1,695,96.8,379.366666666667,100,27.2,153.433333333333,818.7,185.4,542.2,212.733333333333,188.3,88,463.4,698.6,354,95.4,205.2,106.3,216,358.3,353.8,259.1,94.4,468.1,248.9,573.8,30.8,471.7,490.9],[0.45966796875,0.45927734375,2.05078125,0.82724609375,0.5259765625,0.5783203125,0.55634765625,0.41572265625,0.6171875,0.901204427083333,0.55947265625,0.580078125,0.53916015625,0.48466796875,0.56279296875,0.70947265625,15.8203125,0.57275390625,0.751171875,0.40517578125,0.95263671875,0.733203125,1.26953125,0.82802734375,0.741959635416667,0.94892578125,0.400390625,0.5810546875,0.5904296875,0.7564453125,0.9513671875,0.39365234375,0.7685546875,0.7884765625,0.53603515625,0.55,0.394921875,0.710970052083333,0.90126953125,0.588411458333333,0.39482421875,0.532421875,0.59970703125,0.8291015625,15.8203125,0.727994791666667,2.34375,0.46015625,2.63671875,0.810416666666667,6.51891276041667,0.70478515625,0.642350260416667,0.780208333333333,0.62724609375,0.781608072916667,1.26953125,0.417578125,0.9744140625,0.99375,0.412890625,0.66279296875,0.595638020833333,0.544303385416667,0.580794270833333,2.83203125,0.94873046875,0.90439453125,6.47470703125,0.77177734375,0.975,1.07421875,0.993359375,0.88798828125,0.7767578125,0.90126953125,0.7767578125,2.83203125,0.776953125,0.94892578125,0.7794921875,0.77890625,2.34375,0.9765625,0.9765625,0.77783203125,0.8412109375,0.825]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>continuity<\/th>\n      <th>density preservation<\/th>\n      <th>Distance correlation<\/th>\n      <th>Distance correlation (spectral)<\/th>\n      <th>local continuity meta criterion<\/th>\n      <th>global property<\/th>\n      <th>local property<\/th>\n      <th>co-KNN size<\/th>\n      <th>co-KNN AUC<\/th>\n      <th>trustworthiness<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":14,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":13,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":15,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":9,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":10,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":11,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":12,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8,9,10,11,12,13,14,15]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8,9,10,11,12,13,14,15]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render","options.columnDefs.7.render","options.columnDefs.8.render","options.columnDefs.9.render","options.columnDefs.10.render","options.columnDefs.11.render","options.columnDefs.12.render","options.columnDefs.13.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **densMAP (logCP10k)**<sup><a href="/bibliography#narayan2021assessing" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lmcinnes/umap).

<!-- -->

-   **densMAP (logCP10k, 1kHVG)**<sup><a href="/bibliography#narayan2021assessing" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lmcinnes/umap).

<!-- -->

-   **densMAP PCA (logCP10k)**<sup><a href="/bibliography#narayan2021assessing" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lmcinnes/umap).

<!-- -->

-   **densMAP PCA (logCP10k, 1kHVG)**<sup><a href="/bibliography#narayan2021assessing" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lmcinnes/umap).

<!-- -->

-   **NeuralEE (CPU) (Default)**<sup><a href="/bibliography#xiong2020neuralee" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/HiBearME/NeuralEE).

<!-- -->

-   **NeuralEE (CPU) (logCP10k, 1kHVG)**<sup><a href="/bibliography#xiong2020neuralee" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/HiBearME/NeuralEE).

<!-- -->

-   **Principle Component Analysis (PCA) (logCP10k)**<sup><a href="/bibliography#pearson1901pca" target="_blank">11</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html).

<!-- -->

-   **Principle Component Analysis (PCA) (logCP10k, 1kHVG)**<sup><a href="/bibliography#pearson1901pca" target="_blank">11</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html).

<!-- -->

-   **PHATE (default)**<sup><a href="/bibliography#moon2019visualizing" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/PHATE/).

<!-- -->

-   **PHATE (logCP10k, 1kHVG)**<sup><a href="/bibliography#moon2019visualizing" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/PHATE/).

<!-- -->

-   **PHATE (logCP10k)**<sup><a href="/bibliography#moon2019visualizing" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/PHATE/).

<!-- -->

-   **PHATE (gamma=0)**<sup><a href="/bibliography#moon2019visualizing" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/PHATE/).

<!-- -->

-   **PyMDE Preserve Distances (logCP10k)**<sup><a href="/bibliography#agrawal2021mde" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://pymde.org/).

<!-- -->

-   **PyMDE Preserve Distances (logCP10k, 1kHVG)**<sup><a href="/bibliography#agrawal2021mde" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://pymde.org/).

<!-- -->

-   **PyMDE Preserve Neighbors (logCP10k)**<sup><a href="/bibliography#agrawal2021mde" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://pymde.org/).

<!-- -->

-   **PyMDE Preserve Neighbors (logCP10k, 1kHVG)**<sup><a href="/bibliography#agrawal2021mde" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://pymde.org/).

<!-- -->

-   **Random Features**<sup><a href="/bibliography#openproblems" target="_blank">15</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **True Features**<sup><a href="/bibliography#openproblems" target="_blank">15</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **True Features (logCP10k)**<sup><a href="/bibliography#openproblems" target="_blank">15</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **True Features (logCP10k, 1kHVG)**<sup><a href="/bibliography#openproblems" target="_blank">15</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k)**<sup><a href="/bibliography#vandermaaten2008visualizing" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE).

<!-- -->

-   **t-Distributed Stochastic Neighbor Embedding (t-SNE) (logCP10k, 1kHVG)**<sup><a href="/bibliography#vandermaaten2008visualizing" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE).

<!-- -->

-   **UMAP (logCP10k)**<sup><a href="/bibliography#mcinnes2018umap" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lmcinnes/umap).

<!-- -->

-   **UMAP (logCP10k, 1kHVG)**<sup><a href="/bibliography#mcinnes2018umap" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lmcinnes/umap).

<!-- -->

-   **UMAP PCA (logCP10k)**<sup><a href="/bibliography#mcinnes2018umap" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lmcinnes/umap).

<!-- -->

-   **UMAP PCA (logCP10k, 1kHVG)**<sup><a href="/bibliography#mcinnes2018umap" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lmcinnes/umap).

</details>
<details>
<summary>
Baseline methods
</summary>

-   **Random Features**: Missing 'method_description'.

<!-- -->

-   **True Features**: Missing 'method_description'.

<!-- -->

-   **True Features (logCP10k)**: Missing 'method_description'.

<!-- -->

-   **True Features (logCP10k, 1kHVG)**: Missing 'method_description'.

</details>
<details>
<summary>
Datasets
</summary>

-   **Mouse hematopoietic stem cell differentiation**<sup><a href="/bibliography#nestorowa2016single" target="_blank">14</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Mouse myeloid lineage differentiation**<sup><a href="/bibliography#olsson2016single" target="_blank">12</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **5k Peripheral blood mononuclear cells**<sup><a href="/bibliography#10x2019pbmc" target="_blank">13</a></sup>: Missing 'dataset_description'.

</details>
<details>
<summary>
Download raw data
</summary>

<a href="data/task_info.json" class="btn btn-secondary">Task info</a>
<a href="data/method_info.json" class="btn btn-secondary">Method info</a>
<a href="data/metric_info.json" class="btn btn-secondary">Metric info</a>
<a href="data/dataset_info.json" class="btn btn-secondary">Dataset info</a>
<a href="data/results.json" class="btn btn-secondary">Results</a>
<a href="data/quality_control.json" class="btn btn-secondary">Quality control</a>

</details>
<details>
<summary>
Quality control results
</summary>
<table class="table lightable-paper" style='margin-left: auto; margin-right: auto; font-family: "Arial Narrow", arial, helvetica, sans-serif; margin-left: auto; margin-right: auto;'>
 <thead>
  <tr>
   <th style="text-align:left;"> Category </th>
   <th style="text-align:left;"> Name </th>
   <th style="text-align:right;"> Value </th>
   <th style="text-align:left;"> Condition </th>
   <th style="text-align:left;"> Severity </th>
  </tr>
 </thead>
<tbody>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: dimensionality_reduction
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: dimensionality_reduction
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: dimensionality_reduction
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCP10k performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCP10k
  Metric id: distance_correlation_spectral
  Best score: 2.0573274891573483%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCP10k performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCP10k
  Metric id: distance_correlation_spectral
  Best score: 2.0573274891573483%
"> Best score umap_logCP10k distance_correlation_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCP10k performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCP10k
  Metric id: distance_correlation_spectral
  Best score: 2.0573274891573483%
"> 2.057327 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCP10k performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCP10k
  Metric id: distance_correlation_spectral
  Best score: 2.0573274891573483%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCP10k performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCP10k
  Metric id: distance_correlation_spectral
  Best score: 2.0573274891573483%
"> ✗ </td>
  </tr>
</tbody>
</table>

</details>
<details>
<summary>
Visualization of raw results
</summary>

<img src="index.markdown_strict_files/figure-markdown_strict/raw_results-1.png" width="960" />

</details>
