---
title: "Multimodal Data Integration"
summary: "Alignment of cellular profiles from two different modalities"
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
<link href="index_files/libs/dt-ext-buttons-1.11.3/css/buttons.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/dataTables.buttons.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.html5.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.colVis.min.js"></script>
<script src="index_files/libs/dt-ext-buttons-1.11.3/js/buttons.print.min.js"></script>
<link href="index_files/libs/dt-ext-responsive-1.11.3/css/responsive.dataTables.min.css" rel="stylesheet" />
<script src="index_files/libs/dt-ext-responsive-1.11.3/js/dataTables.responsive.min.js"></script>
<link href="index_files/libs/crosstalk-1.2.0/css/crosstalk.min.css" rel="stylesheet" />
<script src="index_files/libs/crosstalk-1.2.0/js/crosstalk.min.js"></script>
<script src="index_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="index_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


## Description

Missing 'task_description'

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="691" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true"><strong>Overview of the results per method</strong>. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Scaled scores

<div id="htmlwidget-2c0ab8c12e52d4d468b5" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-2c0ab8c12e52d4d468b5">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons","Responsive"],"data":[["Procrustes <sup><a href=\"/bibliography#gower1975generalized\" target=\"_blank\">1<\/a><\/sup>","Mutual Nearest Neighbors (log scran) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">2<\/a><\/sup>","Procrustes <sup><a href=\"/bibliography#gower1975generalized\" target=\"_blank\">1<\/a><\/sup>","Procrustes <sup><a href=\"/bibliography#gower1975generalized\" target=\"_blank\">1<\/a><\/sup>","Mutual Nearest Neighbors (log scran) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">2<\/a><\/sup>","Mutual Nearest Neighbors (log CPM) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">2<\/a><\/sup>","Mutual Nearest Neighbors (log CPM) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">2<\/a><\/sup>","Procrustes <sup><a href=\"/bibliography#gower1975generalized\" target=\"_blank\">1<\/a><\/sup>","Mutual Nearest Neighbors (log CPM) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">2<\/a><\/sup>","Mutual Nearest Neighbors (log scran) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">2<\/a><\/sup>","Harmonic Alignment (log scran) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">3<\/a><\/sup>","Mutual Nearest Neighbors (log CPM) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">2<\/a><\/sup>","Harmonic Alignment (log scran) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">3<\/a><\/sup>","Harmonic Alignment (sqrt CPM) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">3<\/a><\/sup>","Harmonic Alignment (log scran) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">3<\/a><\/sup>","Harmonic Alignment (sqrt CPM) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">3<\/a><\/sup>","Harmonic Alignment (sqrt CPM) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">3<\/a><\/sup>","Harmonic Alignment (log scran) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">3<\/a><\/sup>","Mutual Nearest Neighbors (log scran) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">2<\/a><\/sup>","Harmonic Alignment (sqrt CPM) <sup><a href=\"/bibliography#stanley2020harmonic\" target=\"_blank\">3<\/a><\/sup>"],["CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">4<\/a><\/sup>","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","Overall mean","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","Overall mean","CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">4<\/a><\/sup>","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","Overall mean","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">4<\/a><\/sup>","sciCAR Mouse Kidney <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","Overall mean","CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">4<\/a><\/sup>","Overall mean","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>","CITE-seq Cord Blood Mononuclear Cells <sup><a href=\"/bibliography#stoeckius2017simultaneous\" target=\"_blank\">4<\/a><\/sup>","sciCAR Cell Lines <sup><a href=\"/bibliography#cao2018joint\" target=\"_blank\">5<\/a><\/sup>"],[0.367371660099538,0.172964252031419,0.162837986597246,0.0738402342650184,0.0653706327887329,0.0622904826180733,0.0578544389346066,0.0473020654271813,0.0426085296479292,0.0374213892344664,0.0109700285290439,0.00768066739110755,0.0046471142447602,0.00401139972041642,0.00314853587622908,-0.00173450021106317,-0.00480976937010793,-0.00617153514511684,-0.0142737428996867,-0.016706207619677],[0.308171704906801,0.0802243802593182,0.135417673163572,0.0579895919310561,0.0369218501295169,0.0140308448143716,0.0366648883279408,0.0400917226528605,0.0151695187773746,0.0434258827880639,0.0247993159239327,-0.00518717681018846,0.011571461471132,0.0104405294544754,0.0152583183793965,-0.00114099213098423,-0.000711677681043749,0.0094041777431248,-0.0128847126588314,-0.0114345703666224],[0.426571615292276,0.26570412380352,0.19025830003092,0.0896908765989807,0.0938194154479489,0.110550120421775,0.0790439895412725,0.054512408201502,0.0700475405184837,0.0314168956808689,-0.00285925886584493,0.0205485115924036,-0.00227723298161164,-0.00241773001364254,-0.00896124662693835,-0.0023280082911421,-0.00890786105917211,-0.0217472480333585,-0.0156627731405421,-0.0219778448727317],[291,879,449.666666666667,499,982.666666666667,540,749,559,719.333333333333,1239,1993,869,2046,581,1926,890,593.666666666667,1739,830,310],[132.8,88.6,273.333333333333,369,86.3666666666667,43.5,83.3,318.2,71.6,92.8,655.5,88,395,941.1,458.566666666667,903.9,930.366666666667,325.2,77.7,946.1],[0.5666015625,3.22265625,0.684928385416667,0.65517578125,3.87369791666667,1.953125,1.85546875,0.8330078125,2.01822916666667,4.19921875,4.19921875,2.24609375,4.19921875,1.85546875,3.87369791666667,0.61318359375,1.112890625,3.22265625,4.19921875,0.87001953125]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>kNN Area Under the Curve<\/th>\n      <th>Mean squared error<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filters"}},"order":[],"autoWidth":false,"orderClasses":false,"responsive":true}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render"],"jsHooks":[]}</script>

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

-   **Harmonic Alignment (log scran)**<sup><a href="/bibliography#stanley2020harmonic" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/harmonic-alignment).

<!-- -->

-   **Harmonic Alignment (sqrt CPM)**<sup><a href="/bibliography#stanley2020harmonic" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/KrishnaswamyLab/harmonic-alignment).

<!-- -->

-   **Mutual Nearest Neighbors (log CPM)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/LTLA/batchelor).

<!-- -->

-   **Mutual Nearest Neighbors (log scran)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/LTLA/batchelor).

<!-- -->

-   **Procrustes**<sup><a href="/bibliography#gower1975generalized" target="_blank">1</a></sup>: Missing 'method_description'. Links: [Docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.procrustes.html).

<!-- -->

-   **Random Features**<sup><a href="/bibliography#openproblems" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **True Features**<sup><a href="/bibliography#openproblems" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **kNN Area Under the Curve** <sup><a href="/bibliography#stanley2020harmonic" target="_blank">3</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Mean squared error** <sup><a href="/bibliography#lance2022multimodal" target="_blank">7</a></sup>: Missing 'metric_description'.

</details>
<details>
<summary>
Dataset descriptions
</summary>

-   **CITE-seq Cord Blood Mononuclear Cells** <sup><a href="/bibliography#stoeckius2017simultaneous" target="_blank">4</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **sciCAR Cell Lines** <sup><a href="/bibliography#cao2018joint" target="_blank">5</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **sciCAR Mouse Kidney** <sup><a href="/bibliography#cao2018joint" target="_blank">5</a></sup>: Missing 'dataset_description'.

</details>
<details>
<summary>
Baseline descriptions
</summary>

-   **Random Features**: Missing 'method_description'.

<!-- -->

-   **True Features**: Missing 'method_description'.

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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: multimodal_data_integration
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: multimodal_data_integration
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: multimodal_data_integration
  Field: dataset_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: multimodal_data_integration
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: multimodal_data_integration
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: multimodal_data_integration
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: multimodal_data_integration
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: multimodal_data_integration
  Field: method_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: multimodal_data_integration
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: multimodal_data_integration
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: multimodal_data_integration
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: multimodal_data_integration
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: multimodal_data_integration
  Field: metric_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: multimodal_data_integration
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: multimodal_data_integration
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: multimodal_data_integration
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: multimodal_data_integration
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: multimodal_data_integration
  Field: task_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: multimodal_data_integration
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: multimodal_data_integration
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
