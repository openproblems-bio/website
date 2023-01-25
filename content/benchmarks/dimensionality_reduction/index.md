---
title: "Dimensionality reduction for visualisation"
summary: "Reduction of high-dimensional datasets to 2D for visualization & interpretation"
bibliography: "../../../static/bibliography/main.bib"
---

<script src="index_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="index_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


Missing 'task_description'

## Results

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="883" alt="Overview of the results per method. This figures shows the means of the scaled scores per method across all results (group Mean), per dataset (group Dataset) and per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the means of the scaled scores per method across all results (group Mean), per dataset (group Dataset) and per metric (group Metric).</figcaption>
</figure>

## Methods

-   **[densMAP](https://github.com/lmcinnes/umap)** (Narayan, Berger, and Cho 2021): Missing 'method_description'.

<!-- -->

-   **[densMAP PCA](https://github.com/lmcinnes/umap)** (Narayan, Berger, and Cho 2021): Missing 'method_description'.

<!-- -->

-   **[NeuralEE](https://github.com/HiBearME/NeuralEE)** (Xiong et al. 2020): Missing 'method_description'.

<!-- -->

-   **[Principle Component Analysis](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)** (Pearson 1901): Missing 'method_description'.

<!-- -->

-   **[PHATE](https://github.com/KrishnaswamyLab/PHATE/)** (Moon et al. 2019): Missing 'method_description'.

<!-- -->

-   **[t-Distributed Stochastic Neighbor Embedding](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html#sklearn.manifold.TSNE)** (van der Maaten and Hinton 2008): Missing 'method_description'.

<!-- -->

-   **[UMAP](https://github.com/lmcinnes/umap)** (McInnes, Healy, and Melville 2018): Missing 'method_description'.

<!-- -->

-   **[UMAP PCA](https://github.com/lmcinnes/umap)** (McInnes, Healy, and Melville 2018): Missing 'method_description'.

## Metrics

-   **continuity** (Zhang, Shang, and Zhang 2021): Missing 'metric_description'.

<!-- -->

-   **density preservation** (Narayan, Berger, and Cho 2021): Missing 'metric_description'.

<!-- -->

-   **local continuity meta criterion** (Zhang, Shang, and Zhang 2021): Missing 'metric_description'.

<!-- -->

-   **global property** (Zhang, Shang, and Zhang 2021): Missing 'metric_description'.

<!-- -->

-   **local property** (Zhang, Shang, and Zhang 2021): Missing 'metric_description'.

<!-- -->

-   **co-KNN size** (Zhang, Shang, and Zhang 2021): Missing 'metric_description'.

<!-- -->

-   **co-KNN AUC** (Zhang, Shang, and Zhang 2021): Missing 'metric_description'.

<!-- -->

-   **RMSE** (Kruskal 1964): Missing 'metric_description'.

<!-- -->

-   **RMSE (spectral)** (Coifman and Lafon 2006): Missing 'metric_description'.

<!-- -->

-   **trustworthiness** (Venna and Kaski 2001): Missing 'metric_description'.

## Datasets

-   **Mouse hematopoietic stem cell differentiation** (Nestorowa et al. 2016): Missing 'dataset_description'.

<!-- -->

-   **Mouse myeloid lineage differentiation** (Olsson et al. 2016): Missing 'dataset_description'.

<!-- -->

-   **5k Peripheral blood mononuclear cells** (10x Genomics 2019): Missing 'dataset_description'.

## Baselines

-   **Random Features**: Missing 'method_description'.

<!-- -->

-   **True Features**: Missing 'method_description'.

<!-- -->

-   **True Features**: Missing 'method_description'.

<!-- -->

-   **True Features**: Missing 'method_description'.

## Downloads

<a href="data/task_info.json" class="btn btn-secondary">Task info</a>
<a href="data/method_info.json" class="btn btn-secondary">Method info</a>
<a href="data/metric_info.json" class="btn btn-secondary">Metric info</a>
<a href="data/dataset_info.json" class="btn btn-secondary">Dataset info</a>
<a href="data/results.json" class="btn btn-secondary">Results</a>
<a href="data/quality_control.json" class="btn btn-secondary">Quality control</a>

## Details

<details>
<summary>
Overview per parameter set
</summary>

    Warning: Removed 10 rows containing missing values (geom_rect).

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary_defailed-1.png" width="856" alt="Overview of the results per method and parameter set. This figures shows the means of the scaled scores per method parameter set across all results (group Mean), per dataset (group Dataset) and per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method and parameter set. This figures shows the means of the scaled scores per method parameter set across all results (group Mean), per dataset (group Dataset) and per metric (group Metric).</figcaption>
</figure>

</details>
<details>
<summary>
Quality control
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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> Best score neuralee_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> 102.8381448 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: continuity
  Best score: 102.83814481509313%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> Best score densmap_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> 98.6632657 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: continuity
  Best score: 98.6632656844972%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> Best score densmap_pca_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> 87.2813554 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 87.28135544874854%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> Best score pca_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> 85.7174038 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: continuity
  Best score: 85.71740376798641%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> Best score tsne_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> 83.8734686 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: continuity
  Best score: 83.87346863100112%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> Best score phate_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> 81.2761984 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: continuity
  Best score: 81.27619835417812%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> Best score umap_logCPM_1kHVG continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> 77.0403697 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: continuity
  Best score: 77.04036966783967%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> Best score densmap_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> 52.3461423 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 52.346142282079846%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> Best score neuralee_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> 51.7158522 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 51.715852240502336%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> Best score densmap_pca_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> 41.0670482 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 41.067048200521015%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> Best score pca_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> 39.0098651 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 39.00986505038051%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> Best score phate_sqrt continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> 35.1551122 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: continuity
  Best score: 35.1551121696587%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> Best score tsne_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> 32.9413105 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 32.94131052664672%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> Best score phate_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> 28.4045796 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 28.40457957102999%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> Best score phate_default continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> 26.0457607 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: continuity
  Best score: 26.045760657186854%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> Best score umap_logCPM_1kHVG qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> 25.8299360 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn_auc
  Best score: 25.82993603860544%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> Worst score phate_default rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> -11.8804823 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: rmse_spectral
  Worst score: -11.880482343387474%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> Method 'densmap_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> Method 'densmap_pca_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: densmap_pca_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> Method 'pca_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pca_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> Method 'phate_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: phate_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> Method 'pymde_distances_log_cpm_hvg' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm_hvg
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> Method 'pymde_distances_log_cpm' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_distances_log_cpm
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> Method 'pymde_neighbors_log_cpm_hvg' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm_hvg
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> Method 'pymde_neighbors_log_cpm' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: pymde_neighbors_log_cpm
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> Method 'true_features_log_cpm_hvg' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm_hvg
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> Method 'true_features_log_cpm' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: true_features_log_cpm
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> Method 'tsne_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: tsne_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> Method 'umap_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> Method 'umap_pca_logCPM_1kHVG' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM_1kHVG
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> Method 'umap_pca_logCPM' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  method id: umap_pca_logCPM
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> Worst score phate_sqrt rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> -8.7447871 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: rmse_spectral
  Worst score: -8.744787098984089%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> Best score neuralee_default continuity </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> 17.1172070 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: continuity
  Best score: 17.117206954090772%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> Best score neuralee_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> 16.1329439 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qglobal
  Best score: 16.13294394290441%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> Best score densmap_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> 15.2842773 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 15.284277319217653%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> Best score pca_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> 14.6817450 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 14.681745025490805%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> Best score phate_sqrt qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> 12.3849662 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qnn_auc
  Best score: 12.384966210770889%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> Best score densmap_pca_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> 11.8975100 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qglobal
  Best score: 11.897509952339183%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> Raw data </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> Number of results </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> 36.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> len(results) == len(method_info) * len(metric_info) * len(dataset_info) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Number of results should be equal to #methods × #metrics × #datasets.
  Task id: dimensionality_reduction
  Number of results: 36
  Number of methods: 26
  Number of metrics: 10
  Number of datasets: 3
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> Dataset 'mouse_hspc_nestorowa2016' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: mouse_hspc_nestorowa2016
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> Dataset 'olsson_2016_mouse_blood' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: olsson_2016_mouse_blood
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> Dataset 'tenx_5k_pbmc' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  dataset id: tenx_5k_pbmc
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> Metric 'continuity' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: continuity
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> Metric 'density_preservation' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: density_preservation
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> Metric 'lcmc' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: lcmc
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> Metric 'qglobal' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qglobal
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> Metric 'qlocal' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qlocal
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> Metric 'qnn_auc' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn_auc
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> Metric 'qnn' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: qnn
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> Metric 'rmse_spectral' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse_spectral
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> Metric 'rmse' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: rmse
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> Metric 'trustworthiness' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> 0.5384615 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: dimensionality_reduction
  Metric id: trustworthiness
  Percentage missing: 54%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> Best score phate_default qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> 10.4105114 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qnn_auc
  Best score: 10.410511376236835%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> Worst score phate_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> -4.9434394 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.9434393781515835%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> Worst score umap_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> -4.8822042 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.882204229017713%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> Best score tsne_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> 9.3584944 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qglobal
  Best score: 9.358494435549117%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> Best score phate_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> 8.6129926 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qglobal
  Best score: 8.612992603118963%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> Worst score pca_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> -4.2484677 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.2484677198873175%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> Worst score densmap_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> -4.1542921 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -4.154292086061113%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> Worst score densmap_pca_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> -3.8957659 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.895765918017437%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> Best score umap_logCPM_1kHVG qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> 7.7857785 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qglobal
  Best score: 7.7857784598414765%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> Best score neuralee_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> 7.3113220 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.311321979503796%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> Best score densmap_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> 7.1429705 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 7.142970523509472%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> Worst score neuralee_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> -3.4783740 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.4783740440817237%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> Worst score tsne_logCPM_1kHVG rmse_spectral </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> -3.3737825 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: rmse_spectral
  Worst score: -3.3737825355811353%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> Best score pca_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> 6.6570521 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.65705207245835%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> Best score densmap_pca_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> 6.4519809 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qlocal
  Best score: 6.451980918195087%
"> ✗✗✗ </td>
  </tr>
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
"> 1.0000000 </td>
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
"> 1.0000000 </td>
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
"> 1.0000000 </td>
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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: dimensionality_reduction
  Field: task_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> Best score phate_sqrt qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> 5.9839245 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qglobal
  Best score: 5.983924465342125%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> Best score tsne_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> 5.8030592 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.803059232428761%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> Best score tsne_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> 5.7572254 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: lcmc
  Best score: 5.7572254335260125%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> Best score tsne_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> 5.7572254 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method tsne_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: tsne_logCPM_1kHVG
  Metric id: qnn
  Best score: 5.7572254335260125%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> Best score phate_default qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> 5.3156249 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qglobal
  Best score: 5.315624865380937%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> Best score umap_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> 5.2099841 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.209984053856216%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> Best score phate_logCPM_1kHVG qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> 5.2000884 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qlocal
  Best score: 5.200088407359667%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> Best score neuralee_default qnn_auc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> 4.9514392 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qnn_auc
  Best score: 4.951439188900353%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> Best score densmap_pca_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> 4.7894302 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.789430222956235%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> Best score densmap_pca_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> 4.7894302 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.789430222956235%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> Best score umap_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> 4.7704377 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 4.770437654830719%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> Best score umap_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> 4.7704377 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: qnn
  Best score: 4.770437654830719%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> Best score phate_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> 3.8464079 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.8464079273327836%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> Best score phate_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> 3.8464079 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.8464079273327836%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> Best score densmap_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> 3.6471167 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.6471166917533075%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> Best score neuralee_default qglobal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> 3.6255695 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qglobal
  Best score: 3.6255694895590502%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> Best score densmap_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> 3.5763832 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: lcmc
  Best score: 3.5763831544178375%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> Best score densmap_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> 3.5763832 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_logCPM_1kHVG
  Metric id: qnn
  Best score: 3.5763831544178375%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> Best score phate_sqrt qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> 3.5653850 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: qlocal
  Best score: 3.565385048719486%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> Best score phate_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> 3.5141856 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.514185589968861%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> Best score phate_default qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> 3.2908296 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: phate_default
  Metric id: qlocal
  Best score: 3.29082956597632%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> Best score neuralee_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> 3.2184358 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 3.21843575077129%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> Worst score umap_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> -1.3062806 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method umap_logCPM_1kHVG performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: umap_logCPM_1kHVG
  Metric id: density_preservation
  Worst score: -1.3062806408417627%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> Best score neuralee_default qlocal </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> 2.6075869 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_default performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_default
  Metric id: qlocal
  Best score: 2.6075869447062363%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> Best score pca_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> 2.5866639 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.5866639073535724%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> Best score neuralee_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> 2.4847234 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.484723369116433%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> Best score neuralee_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> 2.4847234 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method neuralee_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: neuralee_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.484723369116433%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> Worst score phate_sqrt density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> -1.2017508 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method phate_sqrt performs much worse than baselines.
  Task id: dimensionality_reduction
  Method id: phate_sqrt
  Metric id: density_preservation
  Worst score: -1.2017507573859036%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> Best score pca_logCPM_1kHVG lcmc </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> 2.3773741 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: lcmc
  Best score: 2.37737407101569%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> Best score pca_logCPM_1kHVG qnn </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> 2.3773741 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: pca_logCPM_1kHVG
  Metric id: qnn
  Best score: 2.37737407101569%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> Best score densmap_pca_logCPM_1kHVG density_preservation </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> 2.2777407 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method densmap_pca_logCPM_1kHVG performs a lot better than baselines.
  Task id: dimensionality_reduction
  Method id: densmap_pca_logCPM_1kHVG
  Metric id: density_preservation
  Best score: 2.277740691976449%
"> ✗ </td>
  </tr>
</tbody>
</table>

</details>
<details>
<summary>
Visualization of raw results
</summary>

<img src="index.markdown_strict_files/figure-markdown_strict/unnamed-chunk-10-1.png" width="960" />

</details>

## References

10x Genomics. 2019. "5k Peripheral Blood Mononuclear Cells (PBMCs) from a Healthy Donor with a Panel of TotalSeq-b Antibodies (V3 Chemistry)." <https://www.10xgenomics.com/resources/datasets/5-k-peripheral-blood-mononuclear-cells-pbm-cs-from-a-healthy-donor-with-cell-surface-proteins-v-3-chemistry-3-1-standard-3-1-0>.

Coifman, Ronald R., and Stéphane Lafon. 2006. "Diffusion Maps." *Applied and Computational Harmonic Analysis* 21 (1): 5--30. <https://doi.org/10.1016/j.acha.2006.04.006>.

Kruskal, J. B. 1964. "Multidimensional Scaling by Optimizing Goodness of Fit to a Nonmetric Hypothesis." *Psychometrika* 29 (1): 1--27. <https://doi.org/10.1007/bf02289565>.

McInnes, Leland, John Healy, and James Melville. 2018. "UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction." *arXiv*. <https://doi.org/10.48550/arxiv.1802.03426>.

Moon, Kevin R., David van Dijk, Zheng Wang, Scott Gigante, Daniel B. Burkhardt, William S. Chen, Kristina Yim, et al. 2019. "Visualizing Structure and Transitions in High-Dimensional Biological Data." *Nature Biotechnology* 37 (12): 1482--92. <https://doi.org/10.1038/s41587-019-0336-3>.

Narayan, Ashwin, Bonnie Berger, and Hyunghoon Cho. 2021. "Assessing Single-Cell Transcriptomic Variability Through Density-Preserving Data Visualization." *Nature Biotechnology* 39 (6): 765--74. <https://doi.org/10.1038/s41587-020-00801-7>.

Nestorowa, Sonia, Fiona K. Hamey, Blanca Pijuan Sala, Evangelia Diamanti, Mairi Shepherd, Elisa Laurenti, Nicola K. Wilson, David G. Kent, and Berthold Göttgens. 2016. "A Single-Cell Resolution Map of Mouse Hematopoietic Stem and Progenitor Cell Differentiation." *Blood* 128 (8): e20--31. <https://doi.org/10.1182/blood-2016-05-716480>.

Olsson, Andre, Meenakshi Venkatasubramanian, Viren K. Chaudhri, Bruce J. Aronow, Nathan Salomonis, Harinder Singh, and H. Leighton Grimes. 2016. "Single-Cell Analysis of Mixed-Lineage States Leading to a Binary Cell Fate Choice." *Nature* 537 (7622): 698--702. <https://doi.org/10.1038/nature19348>.

Pearson, Karl. 1901. "On Lines and Planes of Closest Fit to Systems of Points in Space." *The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science* 2 (11): 559--72. <https://doi.org/10.1080/14786440109462720>.

van der Maaten, Laurens, and Geoffrey Hinton. 2008. "Visualizing Data Using t-SNE." *Journal of Machine Learning Research* 9 (86): 2579--2605. <http://jmlr.org/papers/v9/vandermaaten08a.html>.

Venna, Jarkko, and Samuel Kaski. 2001. "Neighborhood Preservation in Nonlinear Projection Methods: An Experimental Study." In *Artificial Neural Networks ICANN 2001*, 485--91. Springer Berlin Heidelberg. [https://doi.org/10.1007/3-540-44668-0\\\_68](https://doi.org/10.1007/3-540-44668-0\_68).

Xiong, Jiankang, Fuzhou Gong, Lin Wan, and Liang Ma. 2020. "NeuralEE: A GPU-Accelerated Elastic Embedding Dimensionality Reduction Method for Visualizing Large-Scale <span class="nocase">scRNA</span>-Seq Data." *Frontiers in Genetics* 11. <https://doi.org/10.3389/fgene.2020.00786>.

Zhang, Yinsheng, Qian Shang, and Guoming Zhang. 2021. "<span class="nocase">pyDRMetrics</span> - a Python Toolkit for Dimensionality Reduction Quality Assessment." *Heliyon* 7 (2): e06199. <https://doi.org/10.1016/j.heliyon.2021.e06199>.
