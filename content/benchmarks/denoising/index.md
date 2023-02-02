---
title: "Denoising"
summary: "Removing noise in sparse single-cell RNA-sequencing count data"
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

<div id="htmlwidget-4975d6ad1870b5d1b19a" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-4975d6ad1870b5d1b19a">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons","Responsive"],"data":[["<a href=\"/bibliography#linderman2018zero\">ALRA<\/a>","<a href=\"/bibliography#linderman2018zero\">ALRA<\/a>","<a href=\"/bibliography#linderman2018zero\">ALRA<\/a>","<a href=\"/bibliography#linderman2018zero\">ALRA<\/a>","<a href=\"/bibliography#https://doi.org/10.1016/j.cell.2018.05.061\">MAGIC (approximate)<\/a>","<a href=\"/bibliography#https://doi.org/10.1016/j.cell.2018.05.061\">MAGIC<\/a>","<a href=\"/bibliography#https://doi.org/10.1016/j.cell.2018.05.061\">MAGIC (approximate)<\/a>","<a href=\"/bibliography#https://doi.org/10.1016/j.cell.2018.05.061\">MAGIC<\/a>","<a href=\"/bibliography#https://doi.org/10.1016/j.cell.2018.05.061\">MAGIC (approximate)<\/a>","<a href=\"/bibliography#https://doi.org/10.1016/j.cell.2018.05.061\">MAGIC<\/a>","<a href=\"/bibliography#https://doi.org/10.1016/j.cell.2018.05.061\">MAGIC (approximate)<\/a>","<a href=\"/bibliography#https://doi.org/10.1016/j.cell.2018.05.061\">MAGIC<\/a>","<a href=\"/bibliography#https://www.nature.com/articles/s41467-018-07931-2\">DCA<\/a>","<a href=\"/bibliography#openproblems\">KNN smoothing<\/a>","<a href=\"/bibliography#https://www.nature.com/articles/s41467-018-07931-2\">DCA<\/a>","<a href=\"/bibliography#https://www.nature.com/articles/s41467-018-07931-2\">DCA<\/a>","<a href=\"/bibliography#openproblems\">KNN smoothing<\/a>","<a href=\"/bibliography#openproblems\">KNN smoothing<\/a>","<a href=\"/bibliography#https://www.nature.com/articles/s41467-018-07931-2\">DCA<\/a>","<a href=\"/bibliography#openproblems\">KNN smoothing<\/a>","<a href=\"/bibliography#wagner2018knearest\">Iterative KNN smoothing<\/a>","<a href=\"/bibliography#wagner2018knearest\">Iterative KNN smoothing<\/a>","<a href=\"/bibliography#wagner2018knearest\">Iterative KNN smoothing<\/a>","<a href=\"/bibliography#wagner2018knearest\">Iterative KNN smoothing<\/a>"],["<a href=\"/bibliography#10x2018pbmc\">1k Peripheral blood mononuclear cells<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (inDrop)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung<\/a>","<a href=\"/bibliography#10x2018pbmc\">1k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#10x2018pbmc\">1k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (inDrop)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (inDrop)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung<\/a>","<a href=\"/bibliography#10x2018pbmc\">1k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#10x2018pbmc\">1k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung<\/a>","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (inDrop)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (inDrop)<\/a>","<a href=\"/bibliography#10x2018pbmc\">1k Peripheral blood mononuclear cells<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula Muris Senis Lung<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (inDrop)<\/a>"],[0.501363973563934,0.484760180546059,0.481765057016442,0.471151511057799,0.423398272165919,0.422343820701091,0.416198003714486,0.414839849650972,0.413539971014164,0.411741162878811,0.401023637162087,0.398039818284369,0.0800425088283952,0.0662707289151282,0.0627714825559103,0.0532909734019813,0.0493447398994811,0.0388499753711862,0.0170589288216383,0.000934457298949309,-4.60364459095676,-4.73169540563172,-4.81302798622217,-5.10374396207803],[0.0262419739615141,-0.00907527426962888,-0.012315382233739,-0.0411524145366617,0.304248727960455,0.303805069617678,0.2389887126279,0.239203260151013,0.280182064485013,0.279685469339885,0.297308752866686,0.296048078250963,0.196793954023976,0.161271320658182,0.173166780463236,0.161684424427903,0.12903510383671,0.124028649400453,0.115092538796496,0.0817795237064677,0.174265173801735,0.13822168432963,0.134437999956578,0.0908271417383699],[0.976485973166353,0.978595635361746,0.975845496266624,0.98345543665226,0.542547816371383,0.540882571784504,0.593407294801071,0.59047643915093,0.546897877543315,0.543796856417737,0.504738521457489,0.500031558317775,-0.0367089363671858,-0.0287298628279258,-0.0476238153514155,-0.0551024776239402,-0.0303456240377475,-0.0463286986580808,-0.0809746811532193,-0.0799106091085691,-9.38155435571526,-9.60161249559307,-9.76049397240092,-10.2983150658944],[329,3809,399,10699,199,199,199,199,299.333333333333,339.333333333333,500,620,249,378,2871,1119.66666666667,500,422,239,388,249,1328,612,259],[98,96.1333333333333,99.4,91,451.8,803.2,480.8,690.3,369.233333333333,544.766666666667,175.1,140.8,995.5,282.1,1944.2,1254.83333333333,168.7,254.2,824.8,311.8,409.2,376.8,585.666666666667,971],[2.44140625,14.8763020833333,3.7109375,38.4765625,0.41845703125,0.417578125,0.52685546875,0.9765625,2.85416666666667,3.13398437467448,7.6171875,8.00781249902344,1.7578125,0.419140625,7.71484375,3.87369791666667,8.00781249902344,2.98164062467448,2.1484375,0.51796875,1.07421875,27.44140625,10.0911458333333,1.7578125],["<a href=\"https://github.com/KlugerLab/ALRA\">v1.0.0<\/a>","<a href=\"https://github.com/KlugerLab/ALRA\">v1.0.0<\/a>","<a href=\"https://github.com/KlugerLab/ALRA\">v1.0.0<\/a>","<a href=\"https://github.com/KlugerLab/ALRA\">v1.0.0<\/a>","<a href=\"https://github.com/KrishnaswamyLab/MAGIC\">v3.0.0<\/a>","<a href=\"https://github.com/KrishnaswamyLab/MAGIC\">v3.0.0<\/a>","<a href=\"https://github.com/KrishnaswamyLab/MAGIC\">v3.0.0<\/a>","<a href=\"https://github.com/KrishnaswamyLab/MAGIC\">v3.0.0<\/a>","<a href=\"https://github.com/KrishnaswamyLab/MAGIC\">v3.0.0<\/a>","<a href=\"https://github.com/KrishnaswamyLab/MAGIC\">v3.0.0<\/a>","<a href=\"https://github.com/KrishnaswamyLab/MAGIC\">v3.0.0<\/a>","<a href=\"https://github.com/KrishnaswamyLab/MAGIC\">v3.0.0<\/a>","<a href=\"https://github.com/theislab/dca\">v0.3.4<\/a>","<a href=\"https://github.com/openproblems-bio/openproblems\">v3.0.0<\/a>","<a href=\"https://github.com/theislab/dca\">v0.3.4<\/a>","<a href=\"https://github.com/theislab/dca\">v0.3.4<\/a>","<a href=\"https://github.com/openproblems-bio/openproblems\">v3.0.0<\/a>","<a href=\"https://github.com/openproblems-bio/openproblems\">v3.0.0<\/a>","<a href=\"https://github.com/theislab/dca\">v0.3.4<\/a>","<a href=\"https://github.com/openproblems-bio/openproblems\">v3.0.0<\/a>","<a href=\"https://github.com/yanailab/knn-smoothing\">v2.0<\/a>","<a href=\"https://github.com/yanailab/knn-smoothing\">v2.0<\/a>","<a href=\"https://github.com/yanailab/knn-smoothing\">v2.0<\/a>","<a href=\"https://github.com/yanailab/knn-smoothing\">v2.0<\/a>"]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>Mean-squared error<\/th>\n      <th>Poisson loss<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n      <th>Library<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filters"}},"order":[],"autoWidth":false,"orderClasses":false,"responsive":true}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render"],"jsHooks":[]}</script>

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

-   **[ALRA](https://github.com/KlugerLab/ALRA)**: Missing 'method_description'. [\[linderman2018zero\]](/bibliography#linderman2018zero)

<!-- -->

-   **[DCA](https://github.com/theislab/dca)**: Missing 'method_description'. [\[https://www.nature.com/articles/s41467-018-07931-2\]](/bibliography#https://www.nature.com/articles/s41467-018-07931-2)

<!-- -->

-   **[KNN smoothing](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[Iterative KNN smoothing](https://github.com/yanailab/knn-smoothing)**: Missing 'method_description'. [\[wagner2018knearest\]](/bibliography#wagner2018knearest)

<!-- -->

-   **[MAGIC](https://github.com/KrishnaswamyLab/MAGIC)**: Missing 'method_description'. [\[https://doi.org/10.1016/j.cell.2018.05.061\]](/bibliography#https://doi.org/10.1016/j.cell.2018.05.061)

<!-- -->

-   **[MAGIC (approximate)](https://github.com/KrishnaswamyLab/MAGIC)**: Missing 'method_description'. [\[https://doi.org/10.1016/j.cell.2018.05.061\]](/bibliography#https://doi.org/10.1016/j.cell.2018.05.061)

<!-- -->

-   **[No denoising](https://github.com/czbiohub/molecular-cross-validation)**: Missing 'method_description'. [\[batson2019molecular\]](/bibliography#batson2019molecular)

<!-- -->

-   **[Perfect denoising](https://github.com/czbiohub/molecular-cross-validation)**: Missing 'method_description'. [\[batson2019molecular\]](/bibliography#batson2019molecular)

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **Mean-squared error**: Missing 'metric_description'. [\[batson2019molecular\]](/bibliography#batson2019molecular)

<!-- -->

-   **Poisson loss**: Missing 'metric_description'. [\[batson2019molecular\]](/bibliography#batson2019molecular)

</details>
<details>
<summary>
Dataset descriptions
</summary>

-   **Pancreas (inDrop)**: Missing 'dataset_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **1k Peripheral blood mononuclear cells**: Missing 'dataset_description'. [\[10x2018pbmc\]](/bibliography#10x2018pbmc)

<!-- -->

-   **Tabula Muris Senis Lung**: Missing 'dataset_description'. [\[tabula2020single\]](/bibliography#tabula2020single)

</details>
<details>
<summary>
Baseline descriptions
</summary>

-   **No denoising**: Missing 'method_description'.

<!-- -->

-   **Perfect denoising**: Missing 'method_description'.

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
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: denoising
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: denoising
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: denoising
  Field: task_description
"> 1.00000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: denoising
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: denoising
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
