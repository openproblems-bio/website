---
title: "Label Projection"
summary: "Automated cell type annotation from rich, labeled reference data"
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

A major challenge for integrating single cell datasets is creating matching cell type
annotations for each cell. One of the most common strategies for annotating cell types
is referred to as
["cluster-then-annotate"](https://openproblems.bio/bibliography#kiselev2019challenges) whereby
cells are aggregated into clusters based on feature similarity and then manually
characterized based on differential gene expression or previously identified marker
genes. Recently, methods have emerged to build on this strategy and annotate cells
using [known marker genes](https://openproblems.bio/bibliography#pliner2019supervised). However,
these strategies pose a difficulty for integrating atlas-scale datasets as the
particular annotations may not match.

To ensure that the cell type labels in newly generated datasets match existing reference
datasets, some methods align cells to a previously annotated [reference
dataset](https://openproblems.bio/bibliography#hou2019scmatch) and then
*project* labels from the reference to the new dataset.

Here, we compare methods for annotation based on a reference dataset. The datasets
consist of two or more samples of single cell profiles that have been manually annotated
with matching labels. These datasets are then split into training and test batches, and
the task of each method is to train a cell type classifer on the training set and
project those labels onto the test set.

## The metrics

Metrics for label projection aim to characterize how well each classifer correctly
assigns cell type labels to cells in the test set.

-   **Accuracy**: Average number of correctly applied labels.
-   **F1 score**: The [F1
    score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html)
    is a weighted average of the precision and recall over all class labels, where an F1
    score reaches its best value at 1 and worst score at 0, where each class contributes
    to the score relative to its frequency in the dataset.
-   **Macro F1 score**: The macro F1 score is an unweighted F1 score, where each class
    contributes equally, regardless of its frequency.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="849" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **Accuracy**<sup><a href="/bibliography#grandini2020metrics" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **F1 score**<sup><a href="/bibliography#grandini2020metrics" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Macro F1 score**<sup><a href="/bibliography#grandini2020metrics" target="_blank">1</a></sup>: Missing 'metric_description'.

## Results

<div id="htmlwidget-5a579169d80fd7fa8f07" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-5a579169d80fd7fa8f07">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Seurat reference mapping (SCTransform) <sup><a href=\"/bibliography#hao2021integrated\" target=\"_blank\">5<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Logistic regression (log CP10k) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","XGBoost (log scran) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","scANVI (All genes) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","XGBoost (log CP10k) <sup><a href=\"/bibliography#chen2016xgboost\" target=\"_blank\">4<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Logistic regression (log scran) <sup><a href=\"/bibliography#hosmer2013applied\" target=\"_blank\">3<\/a><\/sup>","scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","Multilayer perceptron (log scran) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","Multilayer perceptron (log CP10k) <sup><a href=\"/bibliography#hinton1989connectionist\" target=\"_blank\">2<\/a><\/sup>","K-neighbors classifier (log scran) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","scArches+scANVI (All genes) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","K-neighbors classifier (log CP10k) <sup><a href=\"/bibliography#cover1967nearest\" target=\"_blank\">6<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>","scArches+scANVI (Seurat v3 2000 HVG) <sup><a href=\"/bibliography#lotfollahi2020query\" target=\"_blank\">8<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>","Majority Vote <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">9<\/a><\/sup>"],["Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Overall mean","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Overall mean","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Overall mean","Overall mean","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Overall mean","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Overall mean","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Overall mean","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Overall mean","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","Overall mean","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","Tabula Muris Senis Lung (random split) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">11<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split with label noise) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Pancreas (random split) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">10<\/a><\/sup>","Overall mean","Zebrafish (random split) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>","CeNGEN (random split) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","CeNGEN (split by batch) <sup><a href=\"/bibliography#hammarlund2018cengen\" target=\"_blank\">12<\/a><\/sup>","Zebrafish (by laboratory) <sup><a href=\"/bibliography#wagner2018single\" target=\"_blank\">13<\/a><\/sup>"],[0.974373042677011,0.97289228787297,0.964886518076461,0.963227311940558,0.95791203942717,0.953664816490993,0.946055860010145,0.945245930292962,0.942644978746387,0.942545986695154,0.928714354510521,0.92196612423108,0.914867839956244,0.912351964598167,0.909902041087709,0.90909329885746,0.908492374698738,0.907810800613457,0.906415623200319,0.901685270093357,0.892825368964343,0.889370955817881,0.872142314825596,0.869233615355009,0.867061954271647,0.862199937771499,0.860422736585763,0.860365951983742,0.85949075936233,0.859392170235186,0.851701960593688,0.847304128848976,0.844833103162193,0.842465605853038,0.840864765582191,0.834497206941566,0.831504534282077,0.826925795760488,0.826725508484994,0.82611419300005,0.826011695084746,0.825588494861634,0.821067894206783,0.814056817420187,0.813507989923897,0.812324520527553,0.808311221059536,0.806335955561305,0.805069635984812,0.802627305704937,0.80177711746386,0.800716645709593,0.797184173714225,0.794671725098979,0.794587125225665,0.791686895760608,0.790955772222092,0.789919111087252,0.787042243201294,0.782791088774366,0.781645436671715,0.768187752521328,0.765659477197835,0.758065077650161,0.749745642421024,0.74762858193592,0.743862557498557,0.740058838965668,0.73677067628464,0.733131861728891,0.729808201701315,0.72177520832932,0.716255949285561,0.713688641628456,0.713103129692412,0.709439798567596,0.706745946489651,0.706157272920973,0.692137515251614,0.688015419822649,0.683564623297602,0.679773563849451,0.675399284645835,0.666365517491462,0.645994927818621,0.638280370444211,0.629024668853838,0.620562573863926,0.619812907310703,0.602039259637009,0.579186826875997,0.568825972222537,0.51231929494778,0.491258099406067,0.482973855325193,0.47504353308811,0.46385536576753,0.450818049193041,0.44963303658032,0.327492068284597,0.253723351608773,0.240959428957771,0.23040397380931,0.222494643252647,0.220537985083889,0.217136713612852,0.216495800247503,0.215575604108763,0.211758050040133,0.201772411194742,0.188235638401954,0.178404950250018,0.17642158207247,0.168814464943999,0.11715309494378,0.115733626849713,0.042802496835218,0.0415234825106306,0.0413764600756233,0.0364405712715895,0.0357099087728189,0.0174441370882248,0.0075102918741125,0.00736156224520809,-0.00251693376564711,-0.0291312606031247],[0.983708301008534,0.982156710628394,0.97685009487666,0.969743987587277,0.977988614800759,0.976726144297905,0.973622963537626,0.95159106296547,0.954615981380916,0.963925523661753,0.967362428842505,0.957345971563981,0.923832092078538,0.948544346648612,0.923908248786943,0.922143802382003,0.946869070208729,0.916409351565946,0.917291574768416,0.94573055028463,0.902293780326423,0.971916508538899,0.93805010155721,0.917738659444821,0.968968192397207,0.886237233289514,0.933586337760911,0.871636524040582,0.860829289810322,0.939487975174554,0.963187855787476,0.874051976944079,0.856638729598588,0.94685172647258,0.947190250507786,0.847816497573886,0.938388625592417,0.914990512333966,0.95733126454616,0.842501769643038,0.855091515825665,0.852057842046719,0.844955991875423,0.824906461725149,0.93366951124903,0.920108327691266,0.839771463241986,0.948007590132827,0.946869070208729,0.832682943328456,0.830872686823743,0.818535746789362,0.837351945854484,0.830141667471772,0.947245927075252,0.833544839255499,0.83248730964467,0.943366951124903,0.830795262267343,0.936018957345972,0.82339255499154,0.796491941510696,0.815036983090721,0.876969696969697,0.786859142417557,0.786936977082523,0.785532994923858,0.864848484848485,0.771945240270811,0.795262267343486,0.780456852791878,0.846060606060606,0.800270819228165,0.759940778341794,0.828484848484848,0.773745326240316,0.825454545454545,0.764156148490544,0.764705882352941,0.815757575757576,0.8429642699603,0.768484848484849,0.826666666666667,0.780456852791878,0.788614800759013,0.778787878787879,0.749153976311337,0.73965912555863,0.796868107631231,0.696824045573506,0.76621085134539,0.758932509925011,0.630269095744029,0.664526241278188,0.643030303030303,0.594137557874739,0.604906937394247,0.618212154919608,0.607656514382403,0.324398395721925,0.40904034786126,0.227272727272727,0.372383456365659,0.212700534759358,0.196323529411765,0.200868983957219,0.258787878787879,0.202540106951872,0.203342245989305,0.186096256684492,0.19692513368984,0.173930481283422,0.169251336898396,0.236969696969697,0.10701871657754,0.105213903743316,0.147772386413763,0.0696969696969697,0.185849695328368,0.187096774193548,0.178820791311094,0.101798802884633,0.0958121827411168,0.038477095762969,0.0109090909090909,-0.0303475935828877],[0.983621983444297,0.982069003544071,0.976239723661077,0.969625980315972,0.977327285393632,0.976585400834072,0.972621826717593,0.951625279981562,0.95408771270643,0.963475034285752,0.967126529605769,0.957434748561684,0.922657322676978,0.947620988831743,0.923814468803493,0.921822913048189,0.945707825294691,0.916420005473353,0.916767898745426,0.944995986714874,0.900696342630589,0.968280921651426,0.939601813468938,0.917479171102703,0.965782484549544,0.886727642521141,0.932685670709312,0.86750265388644,0.858415895689347,0.937993948677025,0.956598495780767,0.874400338908412,0.854845074711089,0.944945961421574,0.945456283205643,0.846189992208092,0.936597185144855,0.91950490601948,0.948447281007484,0.845330535427799,0.854709001498318,0.855103118586933,0.843680484868981,0.836908756665904,0.92540513027562,0.918719814091791,0.839551398980277,0.935144433762563,0.933930250093371,0.837728344571366,0.830397987020907,0.824302265618688,0.833815193797134,0.836129555723201,0.93488481143136,0.831345006870058,0.829001949987645,0.930755300058086,0.829735978049522,0.930631098135666,0.822965205458517,0.802470666789794,0.81756487238515,0.872662133527237,0.794836887741711,0.793370408418656,0.780329161006079,0.86406624819638,0.772943518268666,0.789106854467333,0.779950205618204,0.840334887794726,0.803251269629074,0.753664773164194,0.839194483769267,0.777101558437851,0.830972593601492,0.766033844412263,0.798451701328349,0.832784331966552,0.804078540483692,0.796527147775645,0.83333033176958,0.734451804630952,0.7545973908727,0.796168551339748,0.691881804520831,0.709768366330637,0.741749331351868,0.669192926884502,0.698180820635735,0.685307360005032,0.584594053343847,0.571403635644035,0.609770907147512,0.544485627271892,0.501351297710835,0.527072019919698,0.492201364700332,0.386221933599286,0.281929383438386,0.275868641719884,0.259056066869687,0.269393395070123,0.213349513771024,0.248878136973172,0.213955600886401,0.225590329630994,0.236541322205663,0.194465759748664,0.212809824800902,0.185839758395274,0.171167056458022,0.180077137000024,0.0876091403772303,0.104661922569065,-0.00500958891308588,0.0193914659317516,-0.0282302667517107,-0.0372103134056665,-0.0368476907622295,-0.0270278474326343,-0.0397466011178601,-0.0107701557301961,-0.0175731945018003,-0.0408349682785255],[0.955788843578202,0.954451149446445,0.941569735691645,0.950311967918424,0.918420218087118,0.907682904341001,0.891922789775216,0.932521447931854,0.919231242151815,0.900237402137957,0.851654105083289,0.851117652567576,0.898114105113216,0.840890558314147,0.88198340567269,0.883313181142189,0.832900228592795,0.890603044801073,0.885187396087116,0.814329273280568,0.875485983936017,0.727915437263318,0.738775029450641,0.772483015517503,0.666435185868191,0.813634937503841,0.714996201287067,0.841958678024204,0.859227092587321,0.700694586853979,0.63531953021282,0.793460070694437,0.823015505176902,0.635599129664961,0.629947763033146,0.809485131042721,0.61952779210896,0.646281968928019,0.574397979901338,0.790510273929313,0.768234567930256,0.769604523951249,0.774567205875944,0.780355233869508,0.581449328247042,0.598145419799601,0.745610800956346,0.535855842788524,0.534409587652337,0.737470629214988,0.744060678546931,0.75931192472073,0.720385381491058,0.717743952101962,0.501630637170383,0.710170841156268,0.71137805703396,0.495635082078767,0.700595489287017,0.481723210841461,0.698578549565087,0.705600649263495,0.664376576117633,0.52456340245355,0.667540897103805,0.66257836030658,0.665725516565733,0.491261783852138,0.665423270314444,0.615026463375853,0.629017546693864,0.478930131132629,0.545245758999444,0.62746037337938,0.471630056823121,0.577472511024622,0.463810700412916,0.588281825860113,0.51325496207355,0.41550435174382,0.403651059448814,0.474308695287859,0.366200855501257,0.484187895051555,0.394772591824149,0.339884681205008,0.446038225729348,0.412260229702512,0.320821282949009,0.440100806453018,0.273168808646866,0.262238046737567,0.322094735755462,0.237844421295978,0.196120355797764,0.2865074141177,0.285307862197508,0.207169972739817,0.249041230658225,0.271855875532581,0.0702003235266739,0.219736917880702,0.0597723981925838,0.185389999928459,0.251940912068879,0.201663019908165,0.176743921068231,0.218596375743423,0.195390581925433,0.22475521715107,0.154971956715121,0.175444611071359,0.188846352860992,0.0893965608622756,0.156831427876571,0.13732505423676,-0.0143553069950229,0.0354820119031704,-0.0334900483497876,-0.0405647469731134,-0.0348433742304076,-0.022438544187324,-0.0335347060009192,-0.00562225329714864,-0.000886697704231952,-0.016211219947961],[1207,600,479,1108,2619,1670,2519,887,580,1739,1188,719,1078,2359,3442,549,580,1757,2118,1689,2259,7089,1921,1119,15260,1419,929,979,519,969,11580,8410,2019,12869,12306,1769,8689,2102,4168,1981,980,679,580,4652,1817,1787,3612,32000,4452,785.5,6710,3912,2769,3669.125,2819,2127,600,8808,2341,2671,2407,1575.75,3738,1479,3466.25,3903.375,1431,8136,558.125,499,1089,7909,969,2243,13240,2562,2062,1639.625,1279,529,10267,4320,21488,14917,1777,3560,13237,13236.375,13288,12806.75,10749,8246,13488,17265,20118,10358.875,9717,15807,10960,2209,13897,439,11459,2019,13366,1739,15788,9489,1898,11020,1882,1222,1010,17058,25471,499,110,14290,199,189,228,188.875,298,188,189,110],[518.4,469.6,334.2,316.9,108.4,1000,120.8,704.8,264.8,291.5,382.8,374.3,294.1,125.4,777.9,1254.1,256.8,709,293.3,253.3,113.5,2362.7,936,328.4,643.9,1695.9,120.1,119,353.1,122.2,2716.1,1629.7,276.3,2440,2380.4,315.2,2612.9,1016.7,1512.3,1952.8,5600.1,426.1,298.1,565.7,130.6,131.2,104.7,2074.1,1723.8,813.675,124.3,785.4,116.8,119.2625,1223,188.2,409.2,2670.8,621.5,1358.5,792.4,912.5875,996.8625,1402.2,486.95,1883.4,1678.7,1580,317.0125,279.9,119.5,119.1,118.7,587.5,1068.4,274.5125,2167.5,116.5375,1422.7,292.3,2406.3,603.4,3727.5,1769,120.5,106.4,2704.2,2501.05,2788.3,1958.075,2319.6,2723.5,2611.3375,2577.3,2504.5,2004.5625,2713.4,1926.2,2383.7,125.8,2733.4,569.9,2411.1,265.9,2765.7,231.6,1772.9,2593.6,163.2,2403.2,413.1,1592.3,121.7,2769,2185.6,365,37.3,2431.2,19.9,22.4,11.8,22.1625,8.8,15.2,21.2,40.7],[2.1484375,2.1484375,2.1484375,2.5390625,19.62890625,8.30078125,166.6015625,2.24609375,2.24609375,8.30078125,2.5390625,2.24609375,2.63671875,435.05859375,5.17578125,1.26953125,2.24609375,1.26953125,5.2734375,8.30078125,135.44921875,5.46875,8.10546875,8.30078125,2.24609375,1.85546875,8.30078125,5.17578125,2.05078125,8.30078125,4.4921875,6.640625,1.46484375,4.39453125,6.73828125,5.46875,5.6640625,8.30078125,4.296875,1.953125,1.66015625,2.734375,2.24609375,6.640625,8.10546875,8.30078125,6.640625,5.6640625,4.4921875,1.85546875,880.859375,6.640625,108.59375,380.7373046875,3.61328125,4.8828125,1.5625,5.46875,4.8828125,3.90625,1.5625,2.1240234375,6.6162109375,1.7578125,6.84814453125,1.806640625,1.85546875,6.640625,2.4169921875,2.05078125,4.8828125,836.328125,8.10546875,5.37109375,6.640625,6.62841796875,1.85546875,6.6162109375,2.1484375,2.5390625,9.08203125,6.640625,1.5625,7.2265625,8.30078125,6.640625,4.98046875,5.859375,3.7109375,8.3251953125,9.08203125,5.95703125,7.80029296875,9.765625,11.328125,7.91015625,6.0546875,9.1796875,7.03125,463.37890625,12.79296875,1.85546875,10.7421875,5.76171875,3.90625,2.1484375,20.01953125,5.46875,4.8828125,6.640625,4.8828125,1.85546875,4.8828125,15.33203125,6.93359375,3.22265625,0.21923828125,17.48046875,0.67197265625,1.46484375,0.2294921875,0.62410888671875,0.9984375,0.22646484375,0.9666015625,0.2158203125]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>Accuracy<\/th>\n      <th>F1 score<\/th>\n      <th>Macro F1 score<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **K-neighbors classifier (log CP10k)**<sup><a href="/bibliography#cover1967nearest" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).

<!-- -->

-   **K-neighbors classifier (log scran)**<sup><a href="/bibliography#cover1967nearest" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).

<!-- -->

-   **Logistic regression (log CP10k)**<sup><a href="/bibliography#hosmer2013applied" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html).

<!-- -->

-   **Logistic regression (log scran)**<sup><a href="/bibliography#hosmer2013applied" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html).

<!-- -->

-   **Majority Vote**<sup><a href="/bibliography#openproblems" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Multilayer perceptron (log CP10k)**<sup><a href="/bibliography#hinton1989connectionist" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html).

<!-- -->

-   **Multilayer perceptron (log scran)**<sup><a href="/bibliography#hinton1989connectionist" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html).

<!-- -->

-   **Random Labels**<sup><a href="/bibliography#openproblems" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **scANVI (All genes)**<sup><a href="/bibliography#xu2021probabilistic" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scANVI (Seurat v3 2000 HVG)**<sup><a href="/bibliography#xu2021probabilistic" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scArches+scANVI (All genes)**<sup><a href="/bibliography#lotfollahi2020query" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scArches+scANVI (Seurat v3 2000 HVG)**<sup><a href="/bibliography#lotfollahi2020query" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **Seurat reference mapping (SCTransform)**<sup><a href="/bibliography#hao2021integrated" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/satijalab/seurat).

<!-- -->

-   **True Labels**<sup><a href="/bibliography#openproblems" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **XGBoost (log CP10k)**<sup><a href="/bibliography#chen2016xgboost" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://xgboost.readthedocs.io/en/stable/index.html).

<!-- -->

-   **XGBoost (log scran)**<sup><a href="/bibliography#chen2016xgboost" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://xgboost.readthedocs.io/en/stable/index.html).

</details>
<details>
<summary>
Baseline methods
</summary>

-   **Random Labels**: Missing 'method_description'.

<!-- -->

-   **True Labels**: Missing 'method_description'.

</details>
<details>
<summary>
Datasets
</summary>

-   **CeNGEN (split by batch)**<sup><a href="/bibliography#hammarlund2018cengen" target="_blank">12</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **CeNGEN (random split)**<sup><a href="/bibliography#hammarlund2018cengen" target="_blank">12</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Pancreas (by batch)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">10</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Pancreas (random split)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">10</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Pancreas (random split with label noise)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">10</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Tabula Muris Senis Lung (random split)**<sup><a href="/bibliography#tabula2020single" target="_blank">11</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Zebrafish (by laboratory)**<sup><a href="/bibliography#wagner2018single" target="_blank">13</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Zebrafish (random split)**<sup><a href="/bibliography#wagner2018single" target="_blank">13</a></sup>: Missing 'dataset_description'.

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
  Task id: label_projection
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: label_projection
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: label_projection
  Field: dataset_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: label_projection
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: label_projection
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: label_projection
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: label_projection
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: label_projection
  Field: method_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: label_projection
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: label_projection
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: label_projection
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: label_projection
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: label_projection
  Field: metric_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: label_projection
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: label_projection
  Field: metric_description
"> ✗✗ </td>
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
