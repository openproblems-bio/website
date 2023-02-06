---
title: "Spatial Decomposition"
summary: "Calling cell-type compositions for spot-based spatial transcriptomics data"
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

Spatial decomposition (also often referred to as Spatial deconvolution) is
applicable to spatial transcriptomics data where the transcription profile of
each capture location (spot, voxel, bead, etc.) do not share a bijective
relationship with the cells in the tissue, i.e., multiple cells may contribute
to the same capture location. The task of spatial decomposition then refers to
estimating the composition of cell types/states that are present at each capture
location. The cell type/states estimates are presented as proportion values,
representing the proportion of the cells at each capture location that belong to
a given cell type.

We distinguish between *reference-based* decomposition and *de novo*
decomposition, where the former leverage external data (e.g., scRNA-seq or
scNuc-seq) to guide the inference process, while the latter only work with the
spatial data. We require that all datasets have an associated reference single
cell data set, but methods are free to ignore this information.

## Metrics

### R2

R2 pronounced as "R squared", also known as the "coefficient of determination". R2
reports the fraction of the true proportion values' (`adata.obsm["proportions_true"]`)
variance that can be explained by the predicted proportion values
(`adata.obsm["proportion_pred"]`). The **best score**, and upper bound, is 1.0. There is
no fixed lower bound for the metric. The *uniform/non-weighted average* across all cell
types/states is used to summarize performance. See the
[sklearn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)
documentation for details on the implementation and the
[wikipedia](https://en.wikipedia.org/wiki/Coefficient_of_determination) site for more
general information regarding the metric.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="770" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **r2**<sup><a href="/bibliography#miles2005rsquared" target="_blank">1</a></sup>: Missing 'metric_description'.

## Results

<div id="htmlwidget-02ec1e4da3233c4d52be" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-02ec1e4da3233c4d52be">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["Cell2location, amortised (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=1, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=200, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference NB without batch info) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location, amortised (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference NB without batch info) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Non-Negative Least Squares <sup><a href=\"/bibliography#lawson1995solving\" target=\"_blank\">3<\/a><\/sup>","Cell2location, amortised (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=200, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=1, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=1, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference NB without batch info) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=200, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference NB without batch info) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=1, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=200, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location, amortised (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=1, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=200, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference NB without batch info) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location, amortised (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=1, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=200, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference NB without batch info) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location, amortised (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Non-Negative Least Squares <sup><a href=\"/bibliography#lawson1995solving\" target=\"_blank\">3<\/a><\/sup>","Cell2location (detection_alpha=1, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=1, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=200, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=200, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference NB without batch info) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location (detection_alpha=20, reference NB without batch info) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Cell2location, amortised (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Non-Negative Matrix Factorization (NMF) <sup><a href=\"/bibliography#cichocki2009fast\" target=\"_blank\">4<\/a><\/sup>","Non-Negative Least Squares <sup><a href=\"/bibliography#lawson1995solving\" target=\"_blank\">3<\/a><\/sup>","Cell2location, amortised (detection_alpha=20, reference hard-coded) <sup><a href=\"/bibliography#kleshchevnikov2022cell2location\" target=\"_blank\">2<\/a><\/sup>","Non-Negative Least Squares <sup><a href=\"/bibliography#lawson1995solving\" target=\"_blank\">3<\/a><\/sup>","RCTD <sup><a href=\"/bibliography#cable2021robust\" target=\"_blank\">5<\/a><\/sup>","RCTD <sup><a href=\"/bibliography#cable2021robust\" target=\"_blank\">5<\/a><\/sup>","Stereoscope <sup><a href=\"/bibliography#andersson2020single\" target=\"_blank\">6<\/a><\/sup>","Stereoscope <sup><a href=\"/bibliography#andersson2020single\" target=\"_blank\">6<\/a><\/sup>","Non-Negative Least Squares <sup><a href=\"/bibliography#lawson1995solving\" target=\"_blank\">3<\/a><\/sup>","RCTD <sup><a href=\"/bibliography#cable2021robust\" target=\"_blank\">5<\/a><\/sup>","Non-Negative Matrix Factorization (NMF) <sup><a href=\"/bibliography#cichocki2009fast\" target=\"_blank\">4<\/a><\/sup>","Stereoscope <sup><a href=\"/bibliography#andersson2020single\" target=\"_blank\">6<\/a><\/sup>","RCTD <sup><a href=\"/bibliography#cable2021robust\" target=\"_blank\">5<\/a><\/sup>","RCTD <sup><a href=\"/bibliography#cable2021robust\" target=\"_blank\">5<\/a><\/sup>","RCTD <sup><a href=\"/bibliography#cable2021robust\" target=\"_blank\">5<\/a><\/sup>","Stereoscope <sup><a href=\"/bibliography#andersson2020single\" target=\"_blank\">6<\/a><\/sup>","Non-Negative Least Squares <sup><a href=\"/bibliography#lawson1995solving\" target=\"_blank\">3<\/a><\/sup>","RCTD <sup><a href=\"/bibliography#cable2021robust\" target=\"_blank\">5<\/a><\/sup>","Stereoscope <sup><a href=\"/bibliography#andersson2020single\" target=\"_blank\">6<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Stereoscope <sup><a href=\"/bibliography#andersson2020single\" target=\"_blank\">6<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Stereoscope <sup><a href=\"/bibliography#andersson2020single\" target=\"_blank\">6<\/a><\/sup>","Non-Negative Least Squares <sup><a href=\"/bibliography#lawson1995solving\" target=\"_blank\">3<\/a><\/sup>","Non-Negative Least Squares <sup><a href=\"/bibliography#lawson1995solving\" target=\"_blank\">3<\/a><\/sup>","NMF-reg <sup><a href=\"/bibliography#rodriques2019slide\" target=\"_blank\">8<\/a><\/sup>","Non-Negative Matrix Factorization (NMF) <sup><a href=\"/bibliography#cichocki2009fast\" target=\"_blank\">4<\/a><\/sup>","Non-Negative Matrix Factorization (NMF) <sup><a href=\"/bibliography#cichocki2009fast\" target=\"_blank\">4<\/a><\/sup>","NMF-reg <sup><a href=\"/bibliography#rodriques2019slide\" target=\"_blank\">8<\/a><\/sup>","Non-Negative Matrix Factorization (NMF) <sup><a href=\"/bibliography#cichocki2009fast\" target=\"_blank\">4<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Non-Negative Matrix Factorization (NMF) <sup><a href=\"/bibliography#cichocki2009fast\" target=\"_blank\">4<\/a><\/sup>","NMF-reg <sup><a href=\"/bibliography#rodriques2019slide\" target=\"_blank\">8<\/a><\/sup>","NMF-reg <sup><a href=\"/bibliography#rodriques2019slide\" target=\"_blank\">8<\/a><\/sup>","Stereoscope <sup><a href=\"/bibliography#andersson2020single\" target=\"_blank\">6<\/a><\/sup>","Non-Negative Matrix Factorization (NMF) <sup><a href=\"/bibliography#cichocki2009fast\" target=\"_blank\">4<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Non-Negative Matrix Factorization (NMF) <sup><a href=\"/bibliography#cichocki2009fast\" target=\"_blank\">4<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","NMF-reg <sup><a href=\"/bibliography#rodriques2019slide\" target=\"_blank\">8<\/a><\/sup>","NMF-reg <sup><a href=\"/bibliography#rodriques2019slide\" target=\"_blank\">8<\/a><\/sup>","RCTD <sup><a href=\"/bibliography#cable2021robust\" target=\"_blank\">5<\/a><\/sup>","SeuratV3 <sup><a href=\"/bibliography#stuart2019comprehensive\" target=\"_blank\">9<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Tangram <sup><a href=\"/bibliography#biancalani2021deep\" target=\"_blank\">10<\/a><\/sup>","SeuratV3 <sup><a href=\"/bibliography#stuart2019comprehensive\" target=\"_blank\">9<\/a><\/sup>","Tangram <sup><a href=\"/bibliography#biancalani2021deep\" target=\"_blank\">10<\/a><\/sup>","SeuratV3 <sup><a href=\"/bibliography#stuart2019comprehensive\" target=\"_blank\">9<\/a><\/sup>","Tangram <sup><a href=\"/bibliography#biancalani2021deep\" target=\"_blank\">10<\/a><\/sup>","Tangram <sup><a href=\"/bibliography#biancalani2021deep\" target=\"_blank\">10<\/a><\/sup>","SeuratV3 <sup><a href=\"/bibliography#stuart2019comprehensive\" target=\"_blank\">9<\/a><\/sup>","Tangram <sup><a href=\"/bibliography#biancalani2021deep\" target=\"_blank\">10<\/a><\/sup>","Tangram <sup><a href=\"/bibliography#biancalani2021deep\" target=\"_blank\">10<\/a><\/sup>","Tangram <sup><a href=\"/bibliography#biancalani2021deep\" target=\"_blank\">10<\/a><\/sup>","NMF-reg <sup><a href=\"/bibliography#rodriques2019slide\" target=\"_blank\">8<\/a><\/sup>","SeuratV3 <sup><a href=\"/bibliography#stuart2019comprehensive\" target=\"_blank\">9<\/a><\/sup>","SeuratV3 <sup><a href=\"/bibliography#stuart2019comprehensive\" target=\"_blank\">9<\/a><\/sup>","NMF-reg <sup><a href=\"/bibliography#rodriques2019slide\" target=\"_blank\">8<\/a><\/sup>","SeuratV3 <sup><a href=\"/bibliography#stuart2019comprehensive\" target=\"_blank\">9<\/a><\/sup>","Tangram <sup><a href=\"/bibliography#biancalani2021deep\" target=\"_blank\">10<\/a><\/sup>","SeuratV3 <sup><a href=\"/bibliography#stuart2019comprehensive\" target=\"_blank\">9<\/a><\/sup>"],["Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Overall mean","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Overall mean","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Overall mean","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Overall mean","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Overall mean","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Pancreas (alpha=0.5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Tabula muris senis (alpha=0.5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Overall mean","Tabula muris senis (alpha=5) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=5) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","Overall mean","Tabula muris senis (alpha=1) <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">12<\/a><\/sup>","Pancreas (alpha=1) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">11<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>","DestVI <sup><a href=\"/bibliography#lopez2022destvi\" target=\"_blank\">7<\/a><\/sup>"],[0.937014753181216,0.926315934514481,0.925998728785761,0.925424958851603,0.925366057435579,0.905368769364386,0.902060537733502,0.900644825782535,0.900538495420019,0.89835106838777,0.898346586700853,0.898341634618655,0.897676650037383,0.89748742968948,0.896899296179059,0.896095139199156,0.873693388320901,0.873449741471309,0.873288735782773,0.870068918147605,0.8653424869397,0.855259503797447,0.854155001496613,0.852101194100165,0.848449201623164,0.843936323891122,0.840988385250572,0.838454124364698,0.835590112792873,0.826432929987882,0.824043836902177,0.80046200418048,0.776928776147552,0.773432610270897,0.773079278200995,0.772701054733434,0.770958608810269,0.76821955251188,0.757223750733913,0.75688031746089,0.744191085478717,0.743485154186232,0.739893409390207,0.731054839951638,0.715874507763851,0.701418274591183,0.6856455187046,0.684829064204727,0.673657771629452,0.672259522566452,0.6568413289203,0.634861659533817,0.631830371750329,0.620205349021131,0.590421242261145,0.584749921747156,0.577862614243482,0.565621343425103,0.561132589768342,0.559738040674922,0.545973594406287,0.520462965918669,0.513758608015946,0.495205241861399,0.493781743242768,0.48953882418022,0.479976984517995,0.472164946998563,0.47113094145035,0.462000258434543,0.460275037269433,0.442593901157234,0.442277501137284,0.411859050333294,0.396252626654112,0.334318255116397,0.315486762930206,0.29434769342732,0.229365528096917,0.20280059696647,0.183138441183802,0.181845877584225,0.134812953204957,0.0889238232119196,0.0886464931328759,0.0158438755227442,-0.00967716532272123,-0.100200794589274,-0.133213607214541,-0.138980894787534,-0.155725105071339,-0.175536210810183,-0.177104187980244,-0.192818527831023,-0.20939565097834,-0.210836466655828,-0.279083677554245,-0.288890028471463,-0.381562745017298,-0.576573739103164,-0.6064320422457,-0.6112567024809,-0.941531537078311,-2.57728336162979],[0.937014753181216,0.926315934514481,0.925998728785761,0.925424958851603,0.925366057435579,0.905368769364386,0.902060537733502,0.900644825782535,0.900538495420019,0.89835106838777,0.898346586700853,0.898341634618655,0.897676650037383,0.89748742968948,0.896899296179059,0.896095139199156,0.873693388320901,0.873449741471309,0.873288735782773,0.870068918147605,0.8653424869397,0.855259503797447,0.854155001496613,0.852101194100165,0.848449201623164,0.843936323891122,0.840988385250572,0.838454124364698,0.835590112792873,0.826432929987882,0.824043836902177,0.80046200418048,0.776928776147552,0.773432610270897,0.773079278200995,0.772701054733434,0.770958608810269,0.76821955251188,0.757223750733913,0.75688031746089,0.744191085478717,0.743485154186232,0.739893409390207,0.731054839951638,0.715874507763851,0.701418274591183,0.6856455187046,0.684829064204727,0.673657771629452,0.672259522566452,0.6568413289203,0.634861659533817,0.631830371750329,0.620205349021131,0.590421242261145,0.584749921747156,0.577862614243482,0.565621343425103,0.561132589768342,0.559738040674922,0.545973594406287,0.520462965918669,0.513758608015946,0.495205241861399,0.493781743242768,0.48953882418022,0.479976984517995,0.472164946998563,0.47113094145035,0.462000258434543,0.460275037269433,0.442593901157234,0.442277501137284,0.411859050333294,0.396252626654112,0.334318255116397,0.315486762930206,0.29434769342732,0.229365528096917,0.20280059696647,0.183138441183802,0.181845877584225,0.134812953204957,0.0889238232119196,0.0886464931328759,0.0158438755227442,-0.00967716532272123,-0.100200794589274,-0.133213607214541,-0.138980894787534,-0.155725105071339,-0.175536210810183,-0.177104187980244,-0.192818527831023,-0.20939565097834,-0.210836466655828,-0.279083677554245,-0.288890028471463,-0.381562745017298,-0.576573739103164,-0.6064320422457,-0.6112567024809,-0.941531537078311,-2.57728336162979],[14820,13438,7408,25019,12849,19360,10449,188,15909,9990,11149,12567,14349,11328,21558,8770,9050,21601,6357,10538,16979,17003.2857142857,15989.4285714286,12614.5714285714,10877.5714285714,16087.4285714286,25086,25075,10058,9769,16919,239,24895,13117,10006,24343,10108,13819,9819,12879,14249,260,218,14376,289,948,869,1849,878,501.857142857143,2761,328,2028,1328,859,969,1359,329,1493.42857142857,1518.57142857143,6760,998,11418,878,579,1671,288,939,586.714285714286,218,349,4320,270,228,1691,2640,1691,8763.42857142857,270,1899,17268,11261,603,508,2720,538,8418,429,1109,979,478,469,1552,809,399,419,802.428571428571,659,448,853.142857142857,629,348,1370,2242],[599.1,1374.6,1386.3,1416.2,1406.9,590.2,1496.3,120.4,1918,2068.3,2008.1,1840.5,1516.2,1910.7,459.6,1346.1,1512.6,1498,1450.8,1403.5,1840.7,1498.81428571429,1367.41428571429,1453.51428571429,1596.67142857143,1528.95714285714,1400.3,1406.6,1339.5,1631.9,1921.5,27.7,1512.4,1338,1338.1,1534.1,1327.7,1273.3,1642.3,1576,1888.9,176.6,27.1,1944.3,65.1,22.9,17.6,1144.7,928.3,55.7571428571429,15.6,482.5,1029.4,21.8,17.8,18.6,1365.3,24.8,19.2142857142857,1203.85714285714,2681.1,904.7,2610.1,939.7,51.3,73.9,1095.7,313.7,456.6,1983.5,398.6,1430,884.9,1789.2,1566.4,2114.9,591.9,1901.55714285714,348,1060.2,726.7,2222.5,1522.11428571429,1383.6,20.2,149.9,2580.3,336.3,112.9,320.2,161.4,565.5,684.7,141.1,685.2,639,752.628571428571,1908.6,158.1,142.814285714286,927.8,150.4,2037.5,125.9],[11.9140625,1.171875,1.26953125,3.7109375,3.125,11.9140625,3.125,0.64189453125,40.4296875,4.98046875,5.078125,4.98046875,4.19921875,4.98046875,1.26953125,1.3671875,3.125,1.953125,1.5625,4.78515625,17.1875,2.32979910714286,1.86941964285714,2.66462053571429,4.52008928571429,18.6104910714286,1.171875,1.3671875,1.3671875,6.0546875,15.91796875,0.6419921875,1.3671875,1.3671875,1.26953125,1.3671875,1.26953125,1.171875,5.95703125,5.2734375,16.6015625,0.64306640625,0.2314453125,16.30859375,0.469921875,4.19921875,2.34375,1.3671875,1.171875,0.380301339285714,4.19921875,0.824609375,1.3671875,4.19921875,2.34375,2.34375,1.3671875,0.22470703125,3.40401785714286,1.29743303571429,2.1484375,1.171875,2.05078125,1.171875,0.22529296875,0.22685546875,1.46484375,0.82451171875,0.810477120535714,1.3671875,0.82529296875,2.05078125,0.64345703125,1.46484375,2.24609375,1.46484375,1.26953125,2.34375,0.64287109375,1.66015625,1.5625,1.953125,2.42745535714286,3.61328125,4.19921875,124.0234375,4.98046875,0.9765625,243.359375,1.26953125,61.62109375,0.9765625,1.26953125,183.59375,1.26953125,0.9765625,1.40904017857143,3.22265625,62.3046875,146.023995535714,3.61328125,63.8671875,3.125,283.3984375]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>r2<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **Cell2location, amortised (detection_alpha=20, reference hard-coded)**<sup><a href="/bibliography#kleshchevnikov2022cell2location" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/BayraktarLab/cell2location).

<!-- -->

-   **Cell2location (detection_alpha=1, reference hard-coded)**<sup><a href="/bibliography#kleshchevnikov2022cell2location" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/BayraktarLab/cell2location).

<!-- -->

-   **Cell2location (detection_alpha=20, reference hard-coded)**<sup><a href="/bibliography#kleshchevnikov2022cell2location" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/BayraktarLab/cell2location).

<!-- -->

-   **Cell2location (detection_alpha=200, reference hard-coded)**<sup><a href="/bibliography#kleshchevnikov2022cell2location" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/BayraktarLab/cell2location).

<!-- -->

-   **Cell2location (detection_alpha=20, reference NB without batch info)**<sup><a href="/bibliography#kleshchevnikov2022cell2location" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/BayraktarLab/cell2location).

<!-- -->

-   **DestVI**<sup><a href="/bibliography#lopez2022destvi" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **Non-Negative Matrix Factorization (NMF)**<sup><a href="/bibliography#cichocki2009fast" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html).

<!-- -->

-   **NMF-reg**<sup><a href="/bibliography#rodriques2019slide" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/tudaga/NMFreg_tutorial).

<!-- -->

-   **Non-Negative Least Squares**<sup><a href="/bibliography#lawson1995solving" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html).

<!-- -->

-   **Random Proportions**<sup><a href="/bibliography#openproblems" target="_blank">13</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **RCTD**<sup><a href="/bibliography#cable2021robust" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/dmcable/spacexr).

<!-- -->

-   **SeuratV3**<sup><a href="/bibliography#stuart2019comprehensive" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html).

<!-- -->

-   **Stereoscope**<sup><a href="/bibliography#andersson2020single" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/scverse/scvi-tools).

<!-- -->

-   **Tangram**<sup><a href="/bibliography#biancalani2021deep" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/broadinstitute/Tangram).

<!-- -->

-   **True Proportions**<sup><a href="/bibliography#openproblems" target="_blank">13</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

</details>
<details>
<summary>
Baseline methods
</summary>

-   **Random Proportions**: Missing 'method_description'.

<!-- -->

-   **True Proportions**: Missing 'method_description'.

</details>
<details>
<summary>
Datasets
</summary>

-   **DestVI**<sup><a href="/bibliography#lopez2022destvi" target="_blank">7</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Pancreas (alpha=0.5)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">11</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Pancreas (alpha=1)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">11</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Pancreas (alpha=5)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">11</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Tabula muris senis (alpha=0.5)**<sup><a href="/bibliography#tabula2020single" target="_blank">12</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Tabula muris senis (alpha=1)**<sup><a href="/bibliography#tabula2020single" target="_blank">12</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Tabula muris senis (alpha=5)**<sup><a href="/bibliography#tabula2020single" target="_blank">12</a></sup>: Missing 'dataset_description'.

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
  Task id: spatial_decomposition
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: spatial_decomposition
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: spatial_decomposition
  Field: dataset_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: spatial_decomposition
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: spatial_decomposition
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: spatial_decomposition
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: spatial_decomposition
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: spatial_decomposition
  Field: method_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: spatial_decomposition
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: spatial_decomposition
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: spatial_decomposition
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: spatial_decomposition
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: spatial_decomposition
  Field: metric_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: spatial_decomposition
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: spatial_decomposition
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.577283361629789%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.577283361629789%
"> Worst score seuratv3 r2 </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.577283361629789%
"> -2.577283 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.577283361629789%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.577283361629789%
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
