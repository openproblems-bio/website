---
title: "Denoising"
summary: "Removing noise in sparse single-cell RNA-sequencing count data"
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

## The metrics

Metrics for data denoising aim to assess denoising accuracy by comparing the denoised
*training* set to the randomly sampled *test* set.

-   **MSE**: The mean squared error between the denoised counts of the training dataset
    and the true counts of the test dataset after reweighting by the train/test ratio.
-   **Poisson**: The Poisson log likelihood of observing the true counts of the test
    dataset given the distribution given in the denoised dataset.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="691" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **Mean-squared error**<sup><a href="/bibliography#batson2019molecular" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Poisson loss**<sup><a href="/bibliography#batson2019molecular" target="_blank">1</a></sup>: Missing 'metric_description'.

## Results

<div id="htmlwidget-6bd85f2f92d55bff03ea" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-6bd85f2f92d55bff03ea">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["MAGIC (approximate, reversed normalization) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (approximate, reversed normalization) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (reversed normalization) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (reversed normalization) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (approximate, reversed normalization) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (reversed normalization) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (reversed normalization) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (approximate, reversed normalization) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","ALRA (sqrt norm) <sup><a href=\"/bibliography#linderman2018zero\" target=\"_blank\">3<\/a><\/sup>","ALRA (sqrt norm) <sup><a href=\"/bibliography#linderman2018zero\" target=\"_blank\">3<\/a><\/sup>","ALRA (sqrt norm) <sup><a href=\"/bibliography#linderman2018zero\" target=\"_blank\">3<\/a><\/sup>","ALRA (sqrt norm) <sup><a href=\"/bibliography#linderman2018zero\" target=\"_blank\">3<\/a><\/sup>","MAGIC (approximate) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (approximate) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (approximate) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC (approximate) <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","MAGIC <sup><a href=\"/bibliography#van2018recovering\" target=\"_blank\">2<\/a><\/sup>","DCA <sup><a href=\"/bibliography#eraslan2019single\" target=\"_blank\">4<\/a><\/sup>","DCA <sup><a href=\"/bibliography#eraslan2019single\" target=\"_blank\">4<\/a><\/sup>","KNN smoothing <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">5<\/a><\/sup>","DCA <sup><a href=\"/bibliography#eraslan2019single\" target=\"_blank\">4<\/a><\/sup>","KNN smoothing <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">5<\/a><\/sup>","KNN smoothing <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">5<\/a><\/sup>","DCA <sup><a href=\"/bibliography#eraslan2019single\" target=\"_blank\">4<\/a><\/sup>","KNN smoothing <sup><a href=\"/bibliography#openproblems\" target=\"_blank\">5<\/a><\/sup>","ALRA (log norm) <sup><a href=\"/bibliography#linderman2018zero\" target=\"_blank\">3<\/a><\/sup>","ALRA (log norm) <sup><a href=\"/bibliography#linderman2018zero\" target=\"_blank\">3<\/a><\/sup>","ALRA (log norm) <sup><a href=\"/bibliography#linderman2018zero\" target=\"_blank\">3<\/a><\/sup>","ALRA (log norm) <sup><a href=\"/bibliography#linderman2018zero\" target=\"_blank\">3<\/a><\/sup>","Iterative KNN smoothing <sup><a href=\"/bibliography#wagner2018knearest\" target=\"_blank\">6<\/a><\/sup>","Iterative KNN smoothing <sup><a href=\"/bibliography#wagner2018knearest\" target=\"_blank\">6<\/a><\/sup>","Iterative KNN smoothing <sup><a href=\"/bibliography#wagner2018knearest\" target=\"_blank\">6<\/a><\/sup>","Iterative KNN smoothing <sup><a href=\"/bibliography#wagner2018knearest\" target=\"_blank\">6<\/a><\/sup>"],["Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Overall mean","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>","Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>","Overall mean","Overall mean","Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","Overall mean","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>","Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>","Overall mean","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","1k Peripheral blood mononuclear cells <sup><a href=\"/bibliography#10x2018pbmc\" target=\"_blank\">8<\/a><\/sup>","Tabula Muris Senis Lung <sup><a href=\"/bibliography#tabula2020single\" target=\"_blank\">7<\/a><\/sup>","Overall mean","Pancreas (inDrop) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">9<\/a><\/sup>"],[0.641359613576841,0.640628632838973,0.640503688148978,0.640341524713953,0.63016974314406,0.629875824370465,0.608782260248464,0.608520983016366,0.50221785259178,0.484987629983276,0.481521055577976,0.47122398178007,0.423453815370953,0.422191297239953,0.416228593267946,0.414644366056781,0.413566809093286,0.411636754298537,0.40101801864096,0.398074599598878,0.0794997451349686,0.0704060995037914,0.066251505432771,0.0573801570897161,0.0493985981006812,0.0388447204599018,0.0222346266303882,0.000884057846253117,-0.120691320361387,-0.128647144453114,-0.171948259410823,-0.266506313417968,-4.60364459095676,-4.73169540563172,-4.81302798622217,-5.10374396207803],[0.297979339109431,0.303821602552095,0.296270001627922,0.303248264004983,0.280601009575075,0.280014838050224,0.240526248517766,0.2400020870637,0.0279926198161686,-0.00863418664249268,-0.01286481159738,-0.0410303681462667,0.30431175977292,0.303682105917949,0.238975848964844,0.238999968333074,0.280198940093924,0.279583852481205,0.297309211544006,0.296069483192592,0.195235688051279,0.175855088239387,0.161303611545716,0.163154428880905,0.12908727838193,0.124031963236201,0.118372510352049,0.0817049997809567,-0.0689901526948267,-0.0883481957317906,-0.0668818896530103,-0.0433073205324135,0.174265173801735,0.13822168432963,0.134437999956578,0.0908271417383699],[0.98473988804425,0.977435663125851,0.984737374670034,0.977434785422924,0.979738476713044,0.979736810690707,0.977038271979162,0.977039878969032,0.976443085367392,0.978609446609044,0.975906922753333,0.983478331706406,0.542595870968985,0.540700488561957,0.593481337571048,0.590288763780488,0.546934678092649,0.54368965611587,0.504726825737914,0.500079716005164,-0.0362361977813421,-0.0350428892318047,-0.0288006006801738,-0.0483941147014733,-0.0302900821805678,-0.0463425223163973,-0.073903257091273,-0.0799368840884505,-0.172392488027947,-0.168946093174437,-0.277014629168635,-0.489705306303522,-9.38155435571526,-9.60161249559307,-9.76049397240092,-10.2983150658944],[2148,349,2392,179,958.666666666667,913.333333333333,169,379,359,2796.33333333333,379,7651,170,299,170,270,856.333333333333,916,2229,2179,439,2651,139,1209.66666666667,2109,799,539,149,3249,439,1345.66666666667,349,289,2062,877,280],[137.8,256.2,111.7,229.3,292.6,192.066666666667,235.2,483.8,82.5,93.9,98.3,100.9,267.7,288.8,214.4,635.2,201.3,350.266666666667,121.8,126.8,451.2,1750,229.5,894.9,128.2,331.733333333333,483.5,637.5,101,101,97.0666666666667,89.2,503.2,477.8,634.5,922.5],[7.6171875,0.416015625,8.00781249902344,0.7013671875,2.85397135416667,3.07919921842448,0.52841796875,0.5287109375,2.05078125,14.5833333333333,3.3203125,38.37890625,0.42109375,0.43154296875,0.7595703125,0.53154296875,1.23990885416667,2.99029947884115,2.5390625,8.00781249902344,2.63671875,6.73828125,0.69541015625,4.23177083333333,8.00781249902344,3.07360026009115,3.3203125,0.517578125,45.60546875,3.61328125,17.08984375,2.05078125,1.07421875,27.44140625,10.0911458333333,1.7578125]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>Mean-squared error<\/th>\n      <th>Poisson loss<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **ALRA (log norm)**<sup><a href="/bibliography#linderman2018zero" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KlugerLab/ALRA).

<!-- -->

-   **ALRA (sqrt norm)**<sup><a href="/bibliography#linderman2018zero" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KlugerLab/ALRA).

<!-- -->

-   **DCA**<sup><a href="/bibliography#eraslan2019single" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/theislab/dca).

<!-- -->

-   **KNN smoothing**<sup><a href="/bibliography#openproblems" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Iterative KNN smoothing**<sup><a href="/bibliography#wagner2018knearest" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/yanailab/knn-smoothing).

<!-- -->

-   **MAGIC**<sup><a href="/bibliography#van2018recovering" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/MAGIC).

<!-- -->

-   **MAGIC (approximate)**<sup><a href="/bibliography#van2018recovering" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/MAGIC).

<!-- -->

-   **MAGIC (approximate, reversed normalization)**<sup><a href="/bibliography#van2018recovering" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/MAGIC).

<!-- -->

-   **MAGIC (reversed normalization)**<sup><a href="/bibliography#van2018recovering" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/MAGIC).

<!-- -->

-   **No denoising**<sup><a href="/bibliography#batson2019molecular" target="_blank">1</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/czbiohub/molecular-cross-validation).

<!-- -->

-   **Perfect denoising**<sup><a href="/bibliography#batson2019molecular" target="_blank">1</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/czbiohub/molecular-cross-validation).

</details>
<details>
<summary>
Baseline methods
</summary>

-   **No denoising**: Missing 'method_description'.

<!-- -->

-   **Perfect denoising**: Missing 'method_description'.

</details>
<details>
<summary>
Datasets
</summary>

-   **Pancreas (inDrop)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">9</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **1k Peripheral blood mononuclear cells**<sup><a href="/bibliography#10x2018pbmc" target="_blank">8</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Tabula Muris Senis Lung**<sup><a href="/bibliography#tabula2020single" target="_blank">7</a></sup>: Missing 'dataset_description'.

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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method knn_smoothing performs much worse than baselines.
  Task id: denoising
  Method id: knn_smoothing
  Metric id: poisson
  Worst score: -10.298315065894421%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method knn_smoothing performs much worse than baselines.
  Task id: denoising
  Method id: knn_smoothing
  Metric id: poisson
  Worst score: -10.298315065894421%
"> Worst score knn_smoothing poisson </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method knn_smoothing performs much worse than baselines.
  Task id: denoising
  Method id: knn_smoothing
  Metric id: poisson
  Worst score: -10.298315065894421%
"> -10.29832 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method knn_smoothing performs much worse than baselines.
  Task id: denoising
  Method id: knn_smoothing
  Metric id: poisson
  Worst score: -10.298315065894421%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method knn_smoothing performs much worse than baselines.
  Task id: denoising
  Method id: knn_smoothing
  Metric id: poisson
  Worst score: -10.298315065894421%
"> ✗✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: denoising
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: denoising
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: denoising
  Field: dataset_description
"> 1.00000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: denoising
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: denoising
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: denoising
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: denoising
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: denoising
  Field: method_description
"> 1.00000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: denoising
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: denoising
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: denoising
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: denoising
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: denoising
  Field: metric_description
"> 1.00000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: denoising
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: denoising
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
