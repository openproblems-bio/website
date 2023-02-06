---
title: "Cell-Cell Communication Inference (Ligand-Target)"
summary: "Detect interactions between ligands and target cell types"
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

The growing availability of single-cell data has sparked an increased
interest in the inference of cell-cell communication (CCC),
with an ever-growing number of computational tools developed for this purpose.

Different tools propose distinct preprocessing steps with diverse
scoring functions, that are challenging to compare and evaluate.
Furthermore, each tool typically comes with its own set of prior knowledge.
To harmonize these, [Dimitrov et
al, 2022](https://openproblems.bio/bibliography#dimitrov2022comparison) recently
developed the [LIANA](https://github.com/saezlab/liana) framework, which was used
as a foundation for this task.

The challenges in evaluating the tools are further exacerbated by the
lack of a gold standard to benchmark the performance of CCC methods. In an
attempt to address this, Dimitrov et al use alternative data modalities, including
the spatial proximity of cell types and
downstream cytokine activities, to generate an inferred ground truth. However,
these modalities are only approximations of biological reality and come
with their own assumptions and limitations. In time, the inclusion of more
datasets with known ground truth interactions will become available, from
which the limitations and advantages of the different CCC methods will
be better understood.

**This subtask evaluates the methods' ability to predict interactions,
the corresponding of cytokines of which, are inferred to be active in
the target cell types. This subtask focuses
on the prediction of interactions from steady-state, or single-context,
single-cell data.**

## The metrics

Metrics for cell-cell communication aim to characterize how good are
the different scoring methods at prioritizing assumed truth predictions.

-   **Odds ratio**: The odds ratio represents the ratio of true and false
    positives within a set of prioritized interactions (top ranked hits) versus
    the same ratio for the remainder of the interactions. Thus, in this
    scenario odds ratios quantify the strength of association between the
    ability of methods to prioritize interactions and those interactions
    assigned to the positive class.

-   **AUPRC**: a single number *\[0-1\]* that summarizes the area under the curve where
    x is the recall and y is the precision.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="638" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **Precision-recall AUC**<sup><a href="/bibliography#davis2006prauc" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Odds Ratio**<sup><a href="/bibliography#bland2000odds" target="_blank">2</a></sup>: Missing 'metric_description'.

## Results

<div id="htmlwidget-b416cc9d94e58af250c1" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-b416cc9d94e58af250c1">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["CellPhoneDB (max) <sup><a href=\"/bibliography#efremova2020cellphonedb\" target=\"_blank\">3<\/a><\/sup>","CellPhoneDB (max) <sup><a href=\"/bibliography#efremova2020cellphonedb\" target=\"_blank\">3<\/a><\/sup>","Specificity Rank Aggregate (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Specificity Rank Aggregate (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","SingleCellSignalR (max) <sup><a href=\"/bibliography#cabello2020singlecellsignalr\" target=\"_blank\">5<\/a><\/sup>","SingleCellSignalR (max) <sup><a href=\"/bibliography#cabello2020singlecellsignalr\" target=\"_blank\">5<\/a><\/sup>","Magnitude Rank Aggregate (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Magnitude Rank Aggregate (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Log2FC (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Log2FC (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Log2FC (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Log2FC (max) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Connectome (max) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">6<\/a><\/sup>","Connectome (max) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">6<\/a><\/sup>","Connectome (sum) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">6<\/a><\/sup>","Connectome (sum) <sup><a href=\"/bibliography#raredon2022computation\" target=\"_blank\">6<\/a><\/sup>","Magnitude Rank Aggregate (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Magnitude Rank Aggregate (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","NATMI (sum) <sup><a href=\"/bibliography#hou2020predicting\" target=\"_blank\">7<\/a><\/sup>","NATMI (sum) <sup><a href=\"/bibliography#hou2020predicting\" target=\"_blank\">7<\/a><\/sup>","CellPhoneDB (sum) <sup><a href=\"/bibliography#efremova2020cellphonedb\" target=\"_blank\">3<\/a><\/sup>","CellPhoneDB (sum) <sup><a href=\"/bibliography#efremova2020cellphonedb\" target=\"_blank\">3<\/a><\/sup>","Specificity Rank Aggregate (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","Specificity Rank Aggregate (sum) <sup><a href=\"/bibliography#dimitrov2022comparison\" target=\"_blank\">4<\/a><\/sup>","NATMI (max) <sup><a href=\"/bibliography#hou2020predicting\" target=\"_blank\">7<\/a><\/sup>","NATMI (max) <sup><a href=\"/bibliography#hou2020predicting\" target=\"_blank\">7<\/a><\/sup>","SingleCellSignalR (sum) <sup><a href=\"/bibliography#cabello2020singlecellsignalr\" target=\"_blank\">5<\/a><\/sup>","SingleCellSignalR (sum) <sup><a href=\"/bibliography#cabello2020singlecellsignalr\" target=\"_blank\">5<\/a><\/sup>"],["Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>","Overall mean","Triple negative breast cancer atlas <sup><a href=\"/bibliography#wu2021single\" target=\"_blank\">8<\/a><\/sup>"],[0.181947354825972,0.181947354825972,0.166961286294659,0.166961286294659,0.16199097459451,0.16199097459451,0.159631286867536,0.159631286867536,0.158037961735781,0.158037961735781,0.147660182178998,0.147660182178998,0.13110877839703,0.13110877839703,0.0893851775910153,0.0893851775910153,0.0853392663676304,0.0853392663676304,0.056765109896185,0.056765109896185,0.0389083777130128,0.0389083777130128,0.0379538738090739,0.0379538738090739,-0.0809134970386472,-0.0809134970386472,-0.100978878493915,-0.100978878493915],[-0.0124189357287479,-0.0124189357287479,-0.000943470860715021,-0.000943470860715021,-0.0108840942610139,-0.0108840942610139,-0.0156034697149609,-0.0156034697149609,-0.0187901199784721,-0.0187901199784721,0.0034392161413225,0.0034392161413225,-0.0296635914226129,-0.0296635914226129,-0.0224023459764655,-0.0224023459764655,-0.0304941684232352,-0.0304941684232352,-0.0398590273331123,-0.0398590273331123,-0.0261324159167904,-0.0261324159167904,-0.0280414237246682,-0.0280414237246682,-0.0509787745102767,-0.0509787745102767,-0.0330565706931787,-0.0330565706931787],[0.376313645380692,0.376313645380692,0.334866043450033,0.334866043450033,0.334866043450033,0.334866043450033,0.334866043450033,0.334866043450033,0.334866043450033,0.334866043450033,0.291881148216674,0.291881148216674,0.291881148216674,0.291881148216674,0.201172701158496,0.201172701158496,0.201172701158496,0.201172701158496,0.153389247125482,0.153389247125482,0.103949171342816,0.103949171342816,0.103949171342816,0.103949171342816,-0.110848219567018,-0.110848219567018,-0.168901186294652,-0.168901186294652],[13679,13679,13040,13040,2068,2068,14029,14029,1960,1960,2049,2049,2508,2508,2247,2247,9569,9569,2119,2119,4969,4969,14760,14760,1969,1969,1870,1870],[100.2,100.2,101,101,99.7,99.7,100.1,100.1,101.2,101.2,100.1,100.1,91.3,91.3,98.7,98.7,100.1,100.1,98.8,98.8,100.3,100.3,100.1,100.1,100.1,100.1,99.4,99.4],[93.359375,93.359375,95.8984375,95.8984375,20.41015625,20.41015625,95.8984375,95.8984375,20.41015625,20.41015625,20.41015625,20.41015625,20.41015625,20.41015625,20.41015625,20.41015625,95.8984375,95.8984375,20.41015625,20.41015625,93.359375,93.359375,95.8984375,95.8984375,20.41015625,20.41015625,20.41015625,20.41015625]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>Precision-recall AUC<\/th>\n      <th>Odds Ratio<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **CellPhoneDB (max)**<sup><a href="/bibliography#efremova2020cellphonedb" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **CellPhoneDB (sum)**<sup><a href="/bibliography#efremova2020cellphonedb" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Connectome (max)**<sup><a href="/bibliography#raredon2022computation" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Connectome (sum)**<sup><a href="/bibliography#raredon2022computation" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Log2FC (max)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Log2FC (sum)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Magnitude Rank Aggregate (max)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Magnitude Rank Aggregate (sum)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **NATMI (max)**<sup><a href="/bibliography#hou2020predicting" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **NATMI (sum)**<sup><a href="/bibliography#hou2020predicting" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Random Events**<sup><a href="/bibliography#openproblems" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **SingleCellSignalR (max)**<sup><a href="/bibliography#cabello2020singlecellsignalr" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **SingleCellSignalR (sum)**<sup><a href="/bibliography#cabello2020singlecellsignalr" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Specificity Rank Aggregate (max)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **Specificity Rank Aggregate (sum)**<sup><a href="/bibliography#dimitrov2022comparison" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/saezlab/liana).

<!-- -->

-   **True Events**<sup><a href="/bibliography#openproblems" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

</details>
<details>
<summary>
Baseline methods
</summary>

-   **Random Events**: Missing 'method_description'.

<!-- -->

-   **True Events**: Missing 'method_description'.

</details>
<details>
<summary>
Datasets
</summary>

-   **Triple negative breast cancer atlas**<sup><a href="/bibliography#wu2021single" target="_blank">8</a></sup>: Missing 'dataset_description'.

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
</tbody>
</table>

</details>
<details>
<summary>
Visualization of raw results
</summary>

<img src="index.markdown_strict_files/figure-markdown_strict/raw_results-1.png" width="960" />

</details>
