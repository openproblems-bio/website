---
title: "Label Projection"
summary: "Automated cell type annotation from rich, labeled reference data"
bibliography: "../../../static/bibliography/main.bib"
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
<script src="index_files/libs/pdfmake-1.11.3/pdfmake.js"></script>
<script src="index_files/libs/pdfmake-1.11.3/vfs_fonts.js"></script>
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

A major challenge for integrating single cell datasets is creating matching
cell type annotations for each cell. One of the most common strategies for
annotating cell types is referred to as
["cluster-then-annotate"](https://www.nature.com/articles/s41576-018-0088-9)
whereby cells are aggregated into clusters based on feature similarity and
then manually characterized based on differential gene expression or previously
identified marker genes. Recently, methods have emerged to build on this
strategy and annotate cells using
[known marker genes](https://www.nature.com/articles/s41592-019-0535-3).
However, these strategies pose a difficulty for integrating atlas-scale
datasets as the particular annotations may not match.
To ensure that the cell type labels in newly generated datasets match
existing reference datasets, some methods align cells to a previously
annotated [reference dataset](https://academic.oup.com/bioinformatics/article/35/22/4688/54802990)
and then *project* labels from the reference to the new dataset.
Here, we compare methods for annotation based on a reference dataset.
The datasets consist of two or more samples of single cell profiles that
have been manually annotated with matching labels. These datasets are then
split into training and test batches, and the task of each method is to
train a cell type classifer on the training set and project those labels
onto the test set.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="849" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true"><strong>Overview of the results per method</strong>. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Scaled scores

<div id="htmlwidget-8c94642ef75ad87e56e5" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-8c94642ef75ad87e56e5">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"data":[["<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#hao2021integrated\">Seurat reference mapping (SCTransform)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log CPM)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log scran)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#chen2016xgboost\">XGBoost (log CPM)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log scran)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (All genes)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log scran)<\/a>","<a href=\"/bibliography#hosmer2013applied\">Logistic regression (log CPM)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (All genes)<\/a>","<a href=\"/bibliography#cover1967nearest\">K-neighbors classifier (log CPM)<\/a>","<a href=\"/bibliography#hinton1989connectionist\">Multilayer perceptron (log scran)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>","<a href=\"/bibliography#lotfollahi2020query\">scArches+scANVI (Seurat v3 2000 HVG)<\/a>"],["<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","Overall mean","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","Overall mean","Overall mean","Overall mean","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","Overall mean","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (random split with label noise)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung (random split)<\/a>","Overall mean","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","Overall mean","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (random split)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#wagner2018single\">Zebrafish (by labels)<\/a>","<a href=\"/bibliography#hammarlund2018cengen\">CeNGEN (by batch)<\/a>"],[0.965913223867859,0.964367658208494,0.952684431975701,0.949401985677482,0.94111394085715,0.937799420489216,0.935014571833863,0.918854890981803,0.917745492497836,0.916912331513187,0.916036851987011,0.914778127384466,0.913146828604532,0.912418360648578,0.909768069079503,0.908671259183812,0.905366330951764,0.904023251313062,0.902696987319708,0.887535552868791,0.869303703323414,0.868968991800271,0.868179726346856,0.867370577614868,0.863675419179572,0.860219940099454,0.859186292574894,0.856889586011393,0.850828760062989,0.848889748944719,0.846645398807489,0.842814653126717,0.841223053419662,0.837609638402293,0.831109016281076,0.826822477714613,0.826304447299033,0.82351838283067,0.822655018155538,0.818810483822028,0.817753139584553,0.813508766098913,0.811521849254177,0.809137979032701,0.806542652154889,0.805831809773773,0.80550679178431,0.804154701906834,0.802987186227854,0.792190736943857,0.791499838948647,0.790214529377982,0.789299881372633,0.789154860550447,0.788932619211351,0.78878564650847,0.788759827231079,0.786290010885416,0.784826905584305,0.768938299553903,0.767587915116776,0.763818514828551,0.75619755136542,0.754589992370959,0.751409974086843,0.75041949719107,0.749029475612855,0.740563326474389,0.73747514152221,0.733567365777393,0.727494041561931,0.72178631756959,0.718865762454304,0.713113520319071,0.712185383489651,0.708790893287109,0.707378032185632,0.705699726127694,0.703411186558517,0.6850460644249,0.682284222950217,0.667292547863825,0.656036152726739,0.648000015775864,0.639520730607527,0.62867490222002,0.625227821176347,0.617885838441241,0.616440305568029,0.591174978494509,0.580598828854538,0.577395896317353,0.503452784789425,0.48310573518444,0.482349835999205,0.470887830624252,0.44899748504789,0.433069702403012,0.413738536734609,0.327154548556212,0.231837469391237,0.229989284480065,0.222102887147083,0.218996488052941,0.218176607000321,0.216710070740612,0.212625744305163,0.211466086993719,0.207888870146616,0.201364074335551,0.189215733377095,0.186119812298362,0.169618686783017,0.167494928999152,0.135001249507792,0.116697293908652,0.0252947494614596],[0.98085189527159,0.981242672919109,0.971082454083626,0.958843537414966,0.957405236420477,0.948639455782313,0.976553341148886,0.977334896443923,0.921070086225956,0.968085106382979,0.973220836390316,0.923469387755102,0.917090426707937,0.948299319727891,0.975421863536317,0.921291178421402,0.951210564930301,0.914658412558037,0.931613911684252,0.901613973026752,0.91734693877551,0.92108843537415,0.970691676436108,0.947245017584994,0.886376311920093,0.915994130594277,0.932501834189288,0.864912668582799,0.871774070881712,0.861817377846562,0.851868229051514,0.946598639455782,0.946938775510204,0.941836734693878,0.92926924579914,0.956232903477921,0.95487894350697,0.840795010900979,0.955245781364637,0.84895806925924,0.924149659863946,0.820311311666582,0.812956002653106,0.846596750976763,0.835927597221518,0.936394557823129,0.81858743598844,0.82989403234802,0.844540407156076,0.882611885546588,0.944509574052364,0.8299403660292,0.822567881482815,0.830829656925145,0.942039618488628,0.825584343152664,0.942039618488628,0.93747557639703,0.82685585029817,0.816985399958873,0.798726617802033,0.875757575757576,0.798887360246999,0.789028563207897,0.798803002322049,0.792720542874769,0.732312925170068,0.824284666177549,0.86,0.774624717252725,0.781821920625129,0.846060606060606,0.776681061073412,0.828484848484848,0.771987148376414,0.827878787878788,0.787414965986395,0.763410162265515,0.737559017824841,0.844572186601813,0.771515151515152,0.815151515151515,0.779765576804442,0.806765421180632,0.780606060606061,0.752121212121212,0.771093176815847,0.749126053876208,0.736803440346569,0.692714721717294,0.758567322573513,0.763873535264205,0.620299437035903,0.643030303030303,0.652334837499366,0.588042135679114,0.604770717663993,0.59392587334584,0.576598807320584,0.324398395721925,0.20548128342246,0.224732620320856,0.212700534759358,0.361608274603255,0.264848484848485,0.200868983957219,0.356639456472139,0.197927807486631,0.185093582887701,0.186096256684492,0.179946524064171,0.171590909090909,0.238787878787879,0.153208556149733,0.126604278074866,0.10701871657754,0.0490909090909091],[0.980783340058218,0.981066216005203,0.970870629779693,0.959355430636882,0.957145683535011,0.949097193225118,0.975873869431004,0.97774740740176,0.920608492599314,0.966794074526136,0.971709078024912,0.922320264949836,0.916466164507716,0.947392722225706,0.973706370619367,0.920844871516578,0.950364530792719,0.913978653371327,0.930588755235247,0.899968431184312,0.917119547102182,0.929877878018095,0.968024526405955,0.946240748494488,0.887999688242358,0.912736017678177,0.930165331696699,0.863050446099575,0.871879974667731,0.856441725329835,0.850565067965224,0.94470603710352,0.945218582858966,0.940155646823416,0.919653168847016,0.947126922576469,0.943990124231654,0.844207137628025,0.94430296741423,0.84965807210055,0.923367219141477,0.833920157618959,0.811011246370827,0.843264787101034,0.835306081072921,0.932992359295876,0.824342871495219,0.829749092310531,0.84313074446121,0.889863210233122,0.932663312161785,0.830790582041301,0.823579311041343,0.83678794131349,0.92864607606263,0.828527271909688,0.928965825216308,0.925226085815563,0.824479419633134,0.817322725720008,0.804517784940449,0.871616767220357,0.806476617368587,0.797045127450614,0.803229378320793,0.787384207077639,0.723213369996084,0.83962010640151,0.85887163829416,0.768556892973069,0.781868916058832,0.840716806859159,0.77578064625904,0.839579130680956,0.775426500006558,0.833396554433438,0.791108882538936,0.764683242116146,0.742985332536283,0.803706166026946,0.801379965769543,0.820227648514651,0.730018253846317,0.757986397912772,0.796772145891578,0.78436385599821,0.732399857725049,0.688228064751829,0.706402303330782,0.663523737976572,0.69123886037014,0.695646628004714,0.57307978049712,0.610704335421216,0.558395978086367,0.537623120457844,0.490880841879358,0.500777287931684,0.450848666991207,0.385628743371263,0.227646056801774,0.264000744000303,0.268687295060529,0.235388009333949,0.222767717124201,0.248118965029247,0.224704999784204,0.233094721981495,0.199767723379851,0.193687245386856,0.179562105845883,0.186690180013882,0.18548884177828,0.177661496842993,0.146195843310862,0.0867273536668642,0.00840364365364271],[0.936104436273767,0.930794085701171,0.916100212063782,0.9300069889806,0.908790902615961,0.915661612460219,0.852616504921698,0.801482369099725,0.911557898668238,0.815857813630446,0.803180641545805,0.89854472944846,0.905883894597943,0.841563039992137,0.780175973082826,0.883877727613455,0.814523897132272,0.883432688009823,0.845888295039625,0.861024254395308,0.77344462409255,0.755940662008569,0.665822976198504,0.708625966765123,0.816650257376265,0.751929672025907,0.714891711838694,0.842705643351804,0.808832234639525,0.82841014365776,0.837502899405729,0.63713928282085,0.631511801889815,0.630836533689586,0.644404634197073,0.57710760708945,0.580044274158474,0.785552999963008,0.568416305687746,0.757815310106293,0.605742539748237,0.7862948290112,0.810598298738597,0.737552399020305,0.748394278170227,0.548108512202315,0.773590067869272,0.75282098106195,0.721290407066275,0.60409711505186,0.497326630631793,0.709912640063445,0.721752451593742,0.699846983412707,0.496112163082794,0.712245324463058,0.495274037988301,0.496168370443655,0.703145446821611,0.672506772982826,0.699519342607847,0.544081201507722,0.663228676480674,0.677696286454367,0.652197541617685,0.671153741620802,0.791562131672414,0.557785206844106,0.493553786272469,0.657520487106385,0.618791288001833,0.478581539789005,0.604135580030459,0.471276581791408,0.589142502085982,0.465097337549101,0.543610248031565,0.589005774001422,0.629689209314428,0.406859840645941,0.473957551565957,0.366498479925308,0.458324627529458,0.379248228234189,0.341183985324944,0.349539638540638,0.372190428988144,0.416303396695685,0.406115173026737,0.417286475789661,0.29199030361996,0.272667525683141,0.316979136835253,0.1955825671018,0.236318692411882,0.286998235735799,0.251340895600319,0.204505945931513,0.213768135892035,0.271436506575449,0.262385067949479,0.201234489119036,0.184920831621363,0.0599931802216195,0.166913619028278,0.201142263235371,0.0565327766591444,0.20337573151303,0.238805304172296,0.224308720935306,0.208138570221231,0.200078347790296,0.0845793397828931,0.17161473400473,0.132203627137647,0.156345811481553,0.0183896956398271],[1510,740,509,1289,2170,749,911,2021,2422,639,1100,1029,2153,1180,589,395,2288,1248,530,689,1509,2492,17171,1549,1071,559,1529,1268,17557,1548,2841,25867,27567,34156,1689,3571,3300,1051,17900,1301,1689,3957,508,871,3076,26507,4917,2031,2098,2761,1890,1205,931.5,1209.75,20090,338,32207,14731,747,362,1079.875,1751,1895.25,2368,6483.75,1836,620,783,21856,1357,1877,2030,308,2945,2394.5,1101,1489,2430.25,429.875,43239,4125,9031,31286,22598,6597,308,1579,28830,20627.75,20143.125,20262,3399,24253.625,32000,20600,19209,4594,13338,12223,866,15934,491,917,38610,4324,1206,41330,1866,13656,20920,1777,557,38023,268,1556,31139,12606],[866,352.5,1421.9,774.5,225.6,244.3,124,895.3,1292.4,1124.1,123.7,319,190.6,122.6,282.9,1909,251.1,448.2,226.8,137.8,292.3,1319.4,1264.4,98.4,2152.7,183.4,98.1,476.5,2442.7,97.1,549.1,1701.4,1672.7,1614,132.9,1618.9,1427.3,1543.6,1366,2462.6,135,551.9,258.2,129.7,116.6,1551.1,934.6,124.6,156.9,1763.9,1421.9,1128.5,767.8125,126.45,2620.4,807.2,1839.9,1564.3,383.1,3236.2,916.425,1739.5,2113.4,534.1875,1594.7,334,137.9,2587.8,2757.7,565,105.1,122.2,302,1004.2,255.0125,1768,102.9,103.625,334.2125,1993.5,605.5,2570.3,1467.1,1582.6,108.1,333.6,123.4,2873.2,1894.3125,1619.2625,1589.7,2408.5,1864.2625,2695.2,1537.2,1783.025,1601,1248.5,1568.8,127,1505,2500.8,451.6,2826.2,1469.9,344.3,1626.7,143.9,1780,2410.7,102.7,539.3,1625.7,424.6,1157.7,2206.7,1608.4],[2.1484375,2.1484375,2.5390625,2.24609375,8.69140625,2.24609375,415.625,8.49609375,5.46875,2.5390625,401.7578125,2.63671875,5.37109375,446.58203125,2.1484375,1.26953125,8.69140625,1.26953125,2.1484375,504.199218749023,8.69140625,8.69140625,3.41796875,8.69140625,2.05078125,2.34375,8.49609375,1.46484375,6.93359375,5.46875,5.46875,4.4921875,6.4453125,5.56640625,8.49609375,4.296875,3.02734375,1.953125,4.39453125,1.66015625,8.69140625,6.93359375,2.05078125,500.390625,6.93359375,5.76171875,6.93359375,976.5625,5.17578125,8.69140625,3.90625,5.17578125,1.91650390625,596.984863281128,5.56640625,2.734375,4.78515625,5.46875,1.5625,1.5625,2.1240234375,2.05078125,1.806640625,6.97021484375,6.94580078125,1.85546875,2.24609375,2.1484375,6.93359375,5.17578125,5.17578125,1074.21875,2.44140625,6.93359375,6.93359375,1.85546875,8.49609375,6.92138671875,2.30712890625,8.49609375,6.93359375,1.5625,3.3203125,3.61328125,6.93359375,2.34375,8.69140625,4.78515625,5.79833984375,4.99267578125,5.46875,8.49609375,7.2265625,11.328125,9.765625,5.48095703125,3.7109375,4.296875,5.6640625,456.54296875,4.58984375,1.85546875,5.17578125,12.890625,4.39453125,2.1484375,5.2734375,5.17578125,3.7109375,6.54296875,5.17578125,1.85546875,12.59765625,2.1484375,5.17578125,6.8359375,5.078125],["<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/satijalab/seurat\">v4.1.1<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://xgboost.readthedocs.io/en/stable/index.html\">v1.6.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>"]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>Accuracy<\/th>\n      <th>F1 score<\/th>\n      <th>Macro F1 score<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n      <th>Library<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bfrtip","paging":false,"columnDefs":[{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8,9]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8]}],"buttons":["searchPanes",{"extend":"collection","buttons":["csv","excel","pdf"],"text":"Download"}],"language":{"searchPanes":{"collapse":"Filter Rows"}},"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render"],"jsHooks":[]}</script>
<!--### CeNGEN (by batch)-->

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
Method descriptions
</summary>

-   **[K-neighbors classifier (log CPM)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)**: Missing 'method_description'. [\[cover1967nearest\]](/bibliography#cover1967nearest)

<!-- -->

-   **[K-neighbors classifier (log scran)](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)**: Missing 'method_description'. [\[cover1967nearest\]](/bibliography#cover1967nearest)

<!-- -->

-   **[Logistic regression (log CPM)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)**: Missing 'method_description'. [\[hosmer2013applied\]](/bibliography#hosmer2013applied)

<!-- -->

-   **[Logistic regression (log scran)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html)**: Missing 'method_description'. [\[hosmer2013applied\]](/bibliography#hosmer2013applied)

<!-- -->

-   **[Majority Vote](https://github.com/openproblems-bio/openproblems)**: Baseline method using majority voting. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[Multilayer perceptron (log CPM)](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)**: Missing 'method_description'. [\[hinton1989connectionist\]](/bibliography#hinton1989connectionist)

<!-- -->

-   **[Multilayer perceptron (log scran)](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)**: Missing 'method_description'. [\[hinton1989connectionist\]](/bibliography#hinton1989connectionist)

<!-- -->

-   **[Random Labels](https://github.com/openproblems-bio/openproblems)**: Baseline method which generates random labels. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[scANVI (All genes)](https://github.com/YosefLab/scvi-tools)**: Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models. [\[xu2021probabilistic\]](/bibliography#xu2021probabilistic)

<!-- -->

-   **[scANVI (Seurat v3 2000 HVG)](https://github.com/YosefLab/scvi-tools)**: Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models. [\[xu2021probabilistic\]](/bibliography#xu2021probabilistic)

<!-- -->

-   **[scArches+scANVI (All genes)](https://github.com/YosefLab/scvi-tools)**: Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models. [\[lotfollahi2020query\]](/bibliography#lotfollahi2020query)

<!-- -->

-   **[scArches+scANVI (Seurat v3 2000 HVG)](https://github.com/YosefLab/scvi-tools)**: Probabilistic harmonization and annotation of single-cell transcriptomics data with deep generative models. [\[lotfollahi2020query\]](/bibliography#lotfollahi2020query)

<!-- -->

-   **[Seurat reference mapping (SCTransform)](https://github.com/satijalab/seurat)**: The Seurat v3 anchoring procedure is designed to integrate diverse single-cell datasets across technologies and modalities. [\[hao2021integrated\]](/bibliography#hao2021integrated)

<!-- -->

-   **[True Labels](https://github.com/openproblems-bio/openproblems)**: Positive control method by returning the true labels. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[XGBoost (log CPM)](https://xgboost.readthedocs.io/en/stable/index.html)**: Missing 'method_description'. [\[chen2016xgboost\]](/bibliography#chen2016xgboost)

<!-- -->

-   **[XGBoost (log scran)](https://xgboost.readthedocs.io/en/stable/index.html)**: Missing 'method_description'. [\[chen2016xgboost\]](/bibliography#chen2016xgboost)

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **Accuracy**: The percentage of correctly predicted labels. [\[grandini2020metrics\]](/bibliography#grandini2020metrics)

<!-- -->

-   **F1 score**: Calculates the F1 score for each label, and find their average weighted by support (the number of true instances for each label). This alters 'macro' to account for label imbalance; it can result in an F-score that is not between precision and recall. [\[grandini2020metrics\]](/bibliography#grandini2020metrics)

<!-- -->

-   **Macro F1 score**: Calculates the F1 score for each label, and find their unweighted mean. This does not take label imbalance into account. [\[grandini2020metrics\]](/bibliography#grandini2020metrics)

</details>
<details>
<summary>
Dataset descriptions
</summary>

-   **CeNGEN (by batch)**: 100k FACS-isolated C. elegans neurons from 17 experiments sequenced on 10x Genomics. Split into train/test by experimental batch. [\[hammarlund2018cengen\]](/bibliography#hammarlund2018cengen)

<!-- -->

-   **CeNGEN (random split)**: 100k FACS-isolated C. elegans neurons from 17 experiments sequenced on 10x Genomics. Split into train/test randomly. [\[hammarlund2018cengen\]](/bibliography#hammarlund2018cengen)

<!-- -->

-   **Pancreas (by batch)**: Human pancreatic islet scRNA-seq data from 6 datasets across technologies (CEL-seq, CEL-seq2, Smart-seq2, inDrop, Fluidigm C1, and SMARTER-seq). Split into train/test by experimental batch. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Pancreas (random split)**: Human pancreatic islet scRNA-seq data from 6 datasets across technologies (CEL-seq, CEL-seq2, Smart-seq2, inDrop, Fluidigm C1, and SMARTER-seq). Split into train/test randomly. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Pancreas (random split with label noise)**: Human pancreatic islet scRNA-seq data from 6 datasets across technologies (CEL-seq, CEL-seq2, Smart-seq2, inDrop, Fluidigm C1, and SMARTER-seq). Split into train/test randomly with 20% label noise. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Tabula Muris Senis Lung (random split)**: All lung cells from Tabula Muris Senis, a 500k cell-atlas from 18 organs and tissues across the mouse lifespan. Split into train/test randomly. [\[tabula2020single\]](/bibliography#tabula2020single)

<!-- -->

-   **Zebrafish (by labels)**: 90k cells from zebrafish embryos throughout the first day of development, with and without a knockout of chordin, an important developmental gene. Split into train/test by laboratory. [\[wagner2018single\]](/bibliography#wagner2018single)

<!-- -->

-   **Zebrafish (random split)**: 90k cells from zebrafish embryos throughout the first day of development, with and without a knockout of chordin, an important developmental gene. Split into train/test randomly. [\[wagner2018single\]](/bibliography#wagner2018single)

</details>
<details>
<summary>
Baseline descriptions
</summary>

-   **Majority Vote**: Baseline method using majority voting.

<!-- -->

-   **Random Labels**: Baseline method which generates random labels.

<!-- -->

-   **True Labels**: Positive control method by returning the true labels.

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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: label_projection
  dataset id: zebrafish_labs
  Percentage missing: 100%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: label_projection
  dataset id: zebrafish_labs
  Percentage missing: 100%
"> Dataset 'zebrafish_labs' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: label_projection
  dataset id: zebrafish_labs
  Percentage missing: 100%
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: label_projection
  dataset id: zebrafish_labs
  Percentage missing: 100%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: label_projection
  dataset id: zebrafish_labs
  Percentage missing: 100%
"> ✗✗✗ </td>
  </tr>
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
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: label_projection
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: label_projection
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: label_projection
  Field: task_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: label_projection
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: label_projection
  Field: task_description
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
