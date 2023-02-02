---
title: "Cell-Cell Communication Inference (Source-Target)"
summary: "Detect interactions between source and target cell types"
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

<div id="htmlwidget-9cbda48cfcbfbd246d46" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-9cbda48cfcbfbd246d46">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons","Responsive"],"data":[["<a href=\"/bibliography#efremova2020cellphonedb\">CellPhoneDB (max)<\/a>","<a href=\"/bibliography#efremova2020cellphonedb\">CellPhoneDB (max)<\/a>","<a href=\"/bibliography#cabello2020singlecellsignalr\">SingleCellSignalR (max)<\/a>","<a href=\"/bibliography#cabello2020singlecellsignalr\">SingleCellSignalR (max)<\/a>","<a href=\"/bibliography#dimitrov2022comparison\">Magnitude Rank Aggregate (max)<\/a>","<a href=\"/bibliography#dimitrov2022comparison\">Magnitude Rank Aggregate (max)<\/a>","<a href=\"/bibliography#raredon2022computation\">Log2FC (sum)<\/a>","<a href=\"/bibliography#raredon2022computation\">Log2FC (sum)<\/a>","<a href=\"/bibliography#hou2020predicting\">NATMI (max)<\/a>","<a href=\"/bibliography#hou2020predicting\">NATMI (max)<\/a>","<a href=\"/bibliography#raredon2022computation\">Log2FC (max)<\/a>","<a href=\"/bibliography#raredon2022computation\">Log2FC (max)<\/a>","<a href=\"/bibliography#dimitrov2022comparison\">Specificity Rank Aggregate (max)<\/a>","<a href=\"/bibliography#dimitrov2022comparison\">Specificity Rank Aggregate (max)<\/a>","<a href=\"/bibliography#hou2020predicting\">NATMI (sum)<\/a>","<a href=\"/bibliography#hou2020predicting\">NATMI (sum)<\/a>","<a href=\"/bibliography#raredon2022computation\">Connectome (sum)<\/a>","<a href=\"/bibliography#raredon2022computation\">Connectome (sum)<\/a>","<a href=\"/bibliography#raredon2022computation\">Connectome (max)<\/a>","<a href=\"/bibliography#raredon2022computation\">Connectome (max)<\/a>","<a href=\"/bibliography#dimitrov2022comparison\">Specificity Rank Aggregate (sum)<\/a>","<a href=\"/bibliography#dimitrov2022comparison\">Specificity Rank Aggregate (sum)<\/a>","<a href=\"/bibliography#efremova2020cellphonedb\">CellPhoneDB (sum)<\/a>","<a href=\"/bibliography#efremova2020cellphonedb\">CellPhoneDB (sum)<\/a>","<a href=\"/bibliography#dimitrov2022comparison\">Magnitude Rank Aggregate (sum)<\/a>","<a href=\"/bibliography#dimitrov2022comparison\">Magnitude Rank Aggregate (sum)<\/a>","<a href=\"/bibliography#cabello2020singlecellsignalr\">SingleCellSignalR (sum)<\/a>","<a href=\"/bibliography#cabello2020singlecellsignalr\">SingleCellSignalR (sum)<\/a>"],["Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>","Overall mean","<a href=\"/bibliography#tasic2016adult\">Mouse brain atlas<\/a>"],[0.374816111051117,0.374816111051117,0.338490447626045,0.338490447626045,0.336319588677802,0.336319588677802,0.310385730940304,0.310385730940304,0.29157215619934,0.29157215619934,0.289967766345615,0.289967766345615,0.22953446422155,0.22953446422155,0.216983759599155,0.216983759599155,0.216948925161255,0.216948925161255,0.0117035790839415,0.0117035790839415,-0.00280439341683836,-0.00280439341683836,-0.192553419193474,-0.192553419193474,-0.193274231147795,-0.193274231147795,-0.193937164593368,-0.193937164593368],[0.0470797547170948,0.0470797547170948,0.0461528697743829,0.0461528697743829,0.0418111518778968,0.0418111518778968,0.0827714618806079,0.0827714618806079,0.045144312398679,0.045144312398679,0.0419355326912306,0.0419355326912306,0.0443832620558401,0.0443832620558401,0.0192818528110501,0.0192818528110501,0.0192121839352504,0.0192121839352504,0.0234071581678829,0.0234071581678829,-0.00560878683367672,-0.00560878683367672,-0.00510683838694755,-0.00510683838694755,-0.00654846229558964,-0.00654846229558964,-0.00787432918673636,-0.00787432918673636],[0.702552467385139,0.702552467385139,0.630828025477707,0.630828025477707,0.630828025477707,0.630828025477707,0.538,0.538,0.538,0.538,0.538,0.538,0.414685666387259,0.414685666387259,0.414685666387259,0.414685666387259,0.414685666387259,0.414685666387259,0,0,0,0,-0.38,-0.38,-0.38,-0.38,-0.38,-0.38],[7210,7210,1143,1143,29358,29358,1080,1080,1791,1791,860,860,34190,34190,1818,1818,1139,1139,1121,1121,39438,39438,34240,34240,8390,8390,686,686],[100.1,100.1,96.5,96.5,99.6,99.6,96.6,96.6,99,99,99.8,99.8,100.1,100.1,98.8,98.8,93.8,93.8,97.7,97.7,100.1,100.1,100.1,100.1,100,100,93.9,93.9],[115.8203125,115.8203125,19.921875,19.921875,116.2109375,116.2109375,19.921875,19.921875,19.921875,19.921875,19.921875,19.921875,116.30859375,116.30859375,19.921875,19.921875,19.921875,19.921875,19.921875,19.921875,116.11328125,116.11328125,115.8203125,115.8203125,116.2109375,116.2109375,19.921875,19.921875],["<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>","<a href=\"https://github.com/saezlab/liana\">v0.1.9<\/a>"]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>Precision-recall AUC<\/th>\n      <th>Odds Ratio<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n      <th>Library<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filters"}},"order":[],"autoWidth":false,"orderClasses":false,"responsive":true}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render"],"jsHooks":[]}</script>

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

-   **[CellPhoneDB (max)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[efremova2020cellphonedb\]](/bibliography#efremova2020cellphonedb)

<!-- -->

-   **[CellPhoneDB (sum)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[efremova2020cellphonedb\]](/bibliography#efremova2020cellphonedb)

<!-- -->

-   **[Connectome (max)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[raredon2022computation\]](/bibliography#raredon2022computation)

<!-- -->

-   **[Connectome (sum)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[raredon2022computation\]](/bibliography#raredon2022computation)

<!-- -->

-   **[Log2FC (max)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[raredon2022computation\]](/bibliography#raredon2022computation)

<!-- -->

-   **[Log2FC (sum)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[raredon2022computation\]](/bibliography#raredon2022computation)

<!-- -->

-   **[Magnitude Rank Aggregate (max)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[dimitrov2022comparison\]](/bibliography#dimitrov2022comparison)

<!-- -->

-   **[Magnitude Rank Aggregate (sum)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[dimitrov2022comparison\]](/bibliography#dimitrov2022comparison)

<!-- -->

-   **[NATMI (max)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[hou2020predicting\]](/bibliography#hou2020predicting)

<!-- -->

-   **[NATMI (sum)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[hou2020predicting\]](/bibliography#hou2020predicting)

<!-- -->

-   **[Random Events](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[SingleCellSignalR (max)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[cabello2020singlecellsignalr\]](/bibliography#cabello2020singlecellsignalr)

<!-- -->

-   **[SingleCellSignalR (sum)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[cabello2020singlecellsignalr\]](/bibliography#cabello2020singlecellsignalr)

<!-- -->

-   **[Specificity Rank Aggregate (max)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[dimitrov2022comparison\]](/bibliography#dimitrov2022comparison)

<!-- -->

-   **[Specificity Rank Aggregate (sum)](https://github.com/saezlab/liana)**: Missing 'method_description'. [\[dimitrov2022comparison\]](/bibliography#dimitrov2022comparison)

<!-- -->

-   **[True Events](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **Precision-recall AUC**: Missing 'metric_description'. [\[davis2006prauc\]](/bibliography#davis2006prauc)

<!-- -->

-   **Odds Ratio**: Missing 'metric_description'. [\[bland2000odds\]](/bibliography#bland2000odds)

</details>
<details>
<summary>
Dataset descriptions
</summary>

-   **Mouse brain atlas**: Missing 'dataset_description'. [\[tasic2016adult\]](/bibliography#tasic2016adult)

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
  Task id: cell_cell_communication_source_target
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: dataset_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: method_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: metric_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: task_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_source_target
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: cell_cell_communication_source_target
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
