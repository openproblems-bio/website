---
title: "Multimodal Data Integration"
summary: "Alignment of cellular profiles from two different modalities"
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

Cellular function is regulated by the complex interplay of different types of biological
molecules (DNA, RNA, proteins, etc.), which determine the state of a cell. Several
recently described technologies allow for simultaneous measurement of different aspects
of cellular state. For example, [sci-CAR](https://openproblems.bio/bibliography#cao2018joint)
jointly profiles RNA expression and chromatin accessibility on the same cell and
[CITE-seq](https://openproblems.bio/bibliography#stoeckius2017simultaneous) measures
surface protein abundance and RNA expression from each cell. These technologies enable
us to better understand cellular function, however datasets are still rare and there are
tradeoffs that these measurements make for to profile multiple modalities.

Joint methods can be more expensive or lower throughput or more noisy than measuring a
single modality at a time. Therefore it is useful to develop methods that are capable
of integrating measurements of the same biological system but obtained using different
technologies on different cells.

Here the goal is to learn a latent space where cells profiled by different technologies in
different modalities are matched if they have the same state. We use jointly profiled
data as ground truth so that we can evaluate when the observations from the same cell
acquired using different modalities are similar. A perfect result has each of the paired
observations sharing the same coordinates in the latent space.

## The metrics

Metrics for matching modalities aim to characterize how well the aligned
datasets correspond to the ground truth.

-   **kNN AUC**: Let $f(i) ∈ F$ be the modality 1 (e.g., scRNA-seq) measurement of cell $i$,
    and $g(i) ∈ G$ be the modality 2 (e.g., scATAC-seq) measurement of cell $i$. kNN-AUC
    calculates the average percentage overlap of neighborhoods of $f(i)$ in $F$ with
    neighborhoods of $g(i)$ in $G$. Higher is better.
-   **MSE**: Mean squared error (MSE) is the average distance between each pair of matched
    observations of the same cell in the learned latent space. Lower is better.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="691" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **kNN Area Under the Curve**<sup><a href="/bibliography#stanley2020harmonic" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Mean squared error**<sup><a href="/bibliography#lance2022multimodal" target="_blank">2</a></sup>: Missing 'metric_description'.

## Results

<div id="htmlwidget-d49fb3a9fbc04f2dff3c" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-d49fb3a9fbc04f2dff3c">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["Procrustes superimposition <sup><a href=\"/bibliography#gower1975generalized\" target=\"_blank\">3<\/a><\/sup>","Mutual Nearest Neighbors (log CP10k) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Procrustes superimposition <sup><a href=\"/bibliography#gower1975generalized\" target=\"_blank\">3<\/a><\/sup>","Mutual Nearest Neighbors (log scran) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Procrustes superimposition <sup><a href=\"/bibliography#gower1975generalized\" target=\"_blank\">3<\/a><\/sup>","Procrustes superimposition <sup><a href=\"/bibliography#gower1975generalized\" target=\"_blank\">3<\/a><\/sup>","Mutual Nearest Neighbors (log scran) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Mutual Nearest Neighbors (log CP10k) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Harmonic Alignment (log scran) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">1<\/a><\/sup>","Harmonic Alignment (log scran) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">1<\/a><\/sup>","Harmonic Alignment (log scran) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">1<\/a><\/sup>","Harmonic Alignment (sqrt CP10k) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">1<\/a><\/sup>","Mutual Nearest Neighbors (log scran) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Mutual Nearest Neighbors (log CP10k) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Harmonic Alignment (log scran) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">1<\/a><\/sup>","Harmonic Alignment (sqrt CP10k) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">1<\/a><\/sup>","Harmonic Alignment (sqrt CP10k) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">1<\/a><\/sup>","Harmonic Alignment (sqrt CP10k) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">1<\/a><\/sup>","Mutual Nearest Neighbors (log scran) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Mutual Nearest Neighbors (log CP10k) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>"],["CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">5<\/a><\/sup>","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","Overall mean","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Overall mean","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","Overall mean","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">5<\/a><\/sup>","Overall mean","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">6<\/a><\/sup>","CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">5<\/a><\/sup>","CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">5<\/a><\/sup>","CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">5<\/a><\/sup>"],[0.431454967591797,0.230020905924535,0.206193148834619,0.168578643970363,0.116902511350938,0.0702219675611222,0.0484029276001487,0.0388217817762544,0.0129090430079686,0.0112786107756458,0.00846462090160734,0.00550498904636253,0.003209883078727,0.00238316292175918,0.00120620892120763,0.000787784690236678,0.000366534015057406,-0.0035081689907099,-0.0265797442486437,-0.115938723517531],[0.307563893878107,0.135711375043081,0.149426629618938,0.0653674346930334,0.0596984176240684,0.0810175773546387,0.0303540007286493,0.0507734365559639,0.0158740512835701,0.0255947410732199,0.0181140376457897,0.000658039313092922,0.0457117421668828,0.0622186508016053,0.0128733205805789,0.00287697341165797,0.00373756113452412,0.00423531978735687,-0.0200171746739683,-0.0456097161767947],[0.555346041305487,0.324330436805988,0.2629596680503,0.271789853247692,0.174106605077807,0.0594263577676057,0.0664518544716482,0.0268701269965449,0.00994403473236705,-0.00303751952192832,-0.00118479584257499,0.0103519387796321,-0.0392919760094288,-0.0574523249580869,-0.0104609027381637,-0.00130140403118462,-0.00300449310440931,-0.0112516577687767,-0.0331423138233191,-0.186267730858267],[270,669,346,799,329,439,909,662.333333333333,759,1059,902.333333333333,986,1129,739,889,1316.66666666667,1887,1077,799,579],[135.3,84.5,413.333333333333,88.4,522.8,581.9,93.1,81.6333333333333,311.1,433.4,398.1,1221.8,92.9,87.5,449.8,988.3,713.6,1029.5,98,72.9],[0.475,1.85546875,0.693424479166667,3.22265625,0.6685546875,0.93671875,3.80859375,2.05078125,3.22265625,4.1015625,3.80859375,0.98974609375,4.1015625,2.34375,4.1015625,0.990787760416667,1.3671875,0.6154296875,4.1015625,1.953125]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>kNN Area Under the Curve<\/th>\n      <th>Mean squared error<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **Harmonic Alignment (log scran)**<sup><a href="/bibliography#stanley2020harmonic" target="_blank">1</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/harmonic-alignment).

<!-- -->

-   **Harmonic Alignment (sqrt CP10k)**<sup><a href="/bibliography#stanley2020harmonic" target="_blank">1</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/harmonic-alignment).

<!-- -->

-   **Mutual Nearest Neighbors (log CP10k)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/LTLA/batchelor).

<!-- -->

-   **Mutual Nearest Neighbors (log scran)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/LTLA/batchelor).

<!-- -->

-   **Procrustes superimposition**<sup><a href="/bibliography#gower1975generalized" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.procrustes.html).

<!-- -->

-   **Random Features**<sup><a href="/bibliography#openproblems" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **True Features**<sup><a href="/bibliography#openproblems" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

</details>
<details>
<summary>
Baseline methods
</summary>

-   **Random Features**: Missing 'method_description'.

<!-- -->

-   **True Features**: Missing 'method_description'.

</details>
<details>
<summary>
Datasets
</summary>

-   **CITE-seq Cord Blood Mononuclear Cells**<sup><a href="/bibliography#stoeckius2017simultaneous" target="_blank">5</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **sciCAR Cell Lines**<sup><a href="/bibliography#cao2018joint" target="_blank">6</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **sciCAR Mouse Kidney**<sup><a href="/bibliography#cao2018joint" target="_blank">6</a></sup>: Missing 'dataset_description'.

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
  Task id: matching_modalities
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: matching_modalities
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: matching_modalities
  Field: dataset_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: matching_modalities
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: matching_modalities
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: matching_modalities
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: matching_modalities
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: matching_modalities
  Field: method_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: matching_modalities
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: matching_modalities
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: matching_modalities
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: matching_modalities
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: matching_modalities
  Field: metric_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: matching_modalities
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: matching_modalities
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
