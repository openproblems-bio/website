---
title: "Cell-Cell Communication Inference (Ligand-Target)"
summary: "Detect interactions between ligands and target cell types"
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
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="638" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true"><strong>Overview of the results per method</strong>. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Scaled scores

<div id="htmlwidget-5fe70e26ec9c9e88a258" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-5fe70e26ec9c9e88a258">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons","Responsive"],"data":[["CellPhoneDB (max) <sup><a href=\"/bibliography#efremova2020cellphonedb\" target=\"_blank\">1<\/a><\/sup>","CellPhoneDB (max) <sup><a href=\"/bibliography#efremova2020cellphonedb\" target=\"_blank\">1<\/a><\/sup>","Magnitude Rank Aggregate (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">2<\/a><\/sup>","Magnitude Rank Aggregate (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">2<\/a><\/sup>","SingleCellSignalR (max) <sup><a href=\"/bibliography#cabello2020singlecellsignalr\" target=\"_blank\">3<\/a><\/sup>","SingleCellSignalR (max) <sup><a href=\"/bibliography#cabello2020singlecellsignalr\" target=\"_blank\">3<\/a><\/sup>","Specificity Rank Aggregate (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">2<\/a><\/sup>","Specificity Rank Aggregate (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">2<\/a><\/sup>","Connectome (max) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">4<\/a><\/sup>","Connectome (max) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">4<\/a><\/sup>","Log2FC (max) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">4<\/a><\/sup>","Log2FC (max) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">4<\/a><\/sup>","Log2FC (sum) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">4<\/a><\/sup>","Log2FC (sum) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">4<\/a><\/sup>","Connectome (sum) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">4<\/a><\/sup>","Connectome (sum) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">4<\/a><\/sup>","Specificity Rank Aggregate (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">2<\/a><\/sup>","Specificity Rank Aggregate (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">2<\/a><\/sup>","CellPhoneDB (sum) <sup><a href=\"/bibliography#efremova2020cellphonedb\" target=\"_blank\">1<\/a><\/sup>","CellPhoneDB (sum) <sup><a href=\"/bibliography#efremova2020cellphonedb\" target=\"_blank\">1<\/a><\/sup>","Magnitude Rank Aggregate (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">2<\/a><\/sup>","Magnitude Rank Aggregate (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">2<\/a><\/sup>","NATMI (sum) <sup><a href=\"/bibliography#hou2020predicting\" target=\"_blank\">5<\/a><\/sup>","NATMI (sum) <sup><a href=\"/bibliography#hou2020predicting\" target=\"_blank\">5<\/a><\/sup>","NATMI (max) <sup><a href=\"/bibliography#hou2020predicting\" target=\"_blank\">5<\/a><\/sup>","NATMI (max) <sup><a href=\"/bibliography#hou2020predicting\" target=\"_blank\">5<\/a><\/sup>","SingleCellSignalR (sum) <sup><a href=\"/bibliography#cabello2020singlecellsignalr\" target=\"_blank\">3<\/a><\/sup>","SingleCellSignalR (sum) <sup><a href=\"/bibliography#cabello2020singlecellsignalr\" target=\"_blank\">3<\/a><\/sup>"],["Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">6<\/a><\/sup>"],[0.180646303662517,0.180646303662517,0.179901755310703,0.179901755310703,0.160162350462888,0.160162350462888,0.155023802116964,0.155023802116964,0.132331954192469,0.132331954192469,0.088234614824436,0.088234614824436,0.0862397152035264,0.0862397152035264,0.0407149500670646,0.0407149500670646,0.0395269679025018,0.0395269679025018,0.0139825633143108,0.0139825633143108,0.011680166725544,0.011680166725544,0.00687849823391116,0.00687849823391116,-0.0799234254329129,-0.0799234254329129,-0.100692507596507,-0.100692507596507],[-0.015021038055658,-0.015021038055658,-0.0165101347592863,-0.0165101347592863,-0.0145413425242571,-0.0145413425242571,-0.0248184392161055,-0.0248184392161055,-0.0272172398317356,-0.0272172398317356,-0.0247034715096241,-0.0247034715096241,-0.0286932707514433,-0.0286932707514433,-0.0225192712086868,-0.0225192712086868,-0.0248952355378126,-0.0248952355378126,-0.0248619798359533,-0.0248619798359533,-0.029466773013487,-0.029466773013487,-0.0390701099967526,-0.0390701099967526,-0.0489986312988081,-0.0489986312988081,-0.0324838288983625,-0.0324838288983625],[0.376313645380692,0.376313645380692,0.376313645380692,0.376313645380692,0.334866043450033,0.334866043450033,0.334866043450033,0.334866043450033,0.291881148216674,0.291881148216674,0.201172701158496,0.201172701158496,0.201172701158496,0.201172701158496,0.103949171342816,0.103949171342816,0.103949171342816,0.103949171342816,0.0528271064645749,0.0528271064645749,0.0528271064645749,0.0528271064645749,0.0528271064645749,0.0528271064645749,-0.110848219567018,-0.110848219567018,-0.168901186294652,-0.168901186294652],[8499,8499,12320,12320,508,508,34526,34526,893,893,939,939,729,729,880,880,35709,35709,16940,16940,34350,34350,1265,1265,1260,1260,1062,1062],[102,102,100.3,100.3,101.3,101.3,101.2,101.2,98.7,98.7,95.8,95.8,100.6,100.6,97.9,97.9,100.8,100.8,101,101,101.5,101.5,100.9,100.9,97.6,97.6,93.6,93.6],[95.60546875,95.60546875,95.703125,95.703125,19.82421875,19.82421875,96.38671875,96.38671875,19.82421875,19.82421875,19.921875,19.921875,20.41015625,20.41015625,19.82421875,19.82421875,92.67578125,92.67578125,92.67578125,92.67578125,95.703125,95.703125,19.921875,19.921875,19.82421875,19.82421875,20.41015625,20.41015625]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>Precision-recall AUC<\/th>\n      <th>Odds Ratio<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filters"}},"order":[],"autoWidth":false,"orderClasses":false,"responsive":true}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render"],"jsHooks":[]}</script>

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

-   **CellPhoneDB (max)**<sup><a href="/bibliography#efremova2020cellphonedb" target="_blank">1</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **CellPhoneDB (sum)**<sup><a href="/bibliography#efremova2020cellphonedb" target="_blank">1</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Connectome (max)**<sup><a href="/bibliography#raredon2022computation" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Connectome (sum)**<sup><a href="/bibliography#raredon2022computation" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Log2FC (max)**<sup><a href="/bibliography#raredon2022computation" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Log2FC (sum)**<sup><a href="/bibliography#raredon2022computation" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Magnitude Rank Aggregate (max)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Magnitude Rank Aggregate (sum)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **NATMI (max)**<sup><a href="/bibliography#hou2020predicting" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **NATMI (sum)**<sup><a href="/bibliography#hou2020predicting" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Random Events**<sup><a href="/bibliography#openproblems" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **SingleCellSignalR (max)**<sup><a href="/bibliography#cabello2020singlecellsignalr" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **SingleCellSignalR (sum)**<sup><a href="/bibliography#cabello2020singlecellsignalr" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Specificity Rank Aggregate (max)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Specificity Rank Aggregate (sum)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **True Events**<sup><a href="/bibliography#openproblems" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **Precision-recall AUC** <sup><a href="/bibliography#davis2006prauc" target="_blank">8</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Odds Ratio** <sup><a href="/bibliography#bland2000odds" target="_blank">9</a></sup>: Missing 'metric_description'.

</details>
<details>
<summary>
Dataset descriptions
</summary>

-   **Triple negative breast cancer atlas** <sup><a href="/bibliography#wu2021single" target="_blank">6</a></sup>: Missing 'dataset_description'.

</details>
<details>
<summary>
Baseline descriptions
</summary>

-   **Random Events**: Missing 'method_description'.

<!-- -->

-   **True Events**: Missing 'method_description'.

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
  Task id: cell_cell_communication_ligand_target
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: dataset_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: method_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: metric_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: task_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_ligand_target
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_ligand_target
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
