---
title: "Batch integration feature"
summary: "Removing batch effects while preserving biological variation (feature output)"
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

Missing 'task_description'

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="638" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true"><strong>Overview of the results per method</strong>. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Scaled scores

<div id="htmlwidget-938d96a1dae939456cf3" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-938d96a1dae939456cf3">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"data":[["<a href=\"/bibliography#xiong2021online\">SCALEX (hvg)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/unscaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (full)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (hvg/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (hvg/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/scaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (hvg)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (full/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (full/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/scaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (hvg)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (hvg/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (hvg/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/unscaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (full)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (hvg/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (hvg/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (full/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (full/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/unscaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (full)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (full/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN feature (full/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/scaled)<\/a>"],["<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>"],[0.430289532293987,0.363028953229399,0.35924276169265,0.305648185861457,0.252053610030264,0.235634743875278,0.224498886414254,0.224276169265033,0.216703786191537,0.216258351893096,0.183151683570253,0.176169265033408,0.169042316258352,0.168976646956247,0.161692650334076,0.0957683741648107,0.0697104677060133,0.0697104677060133,-0.0250756593169046,-0.0481069042316258,-0.0632516703786192,-0.0639861651534804,-0.0650334075723831,-0.0654418667799029,-0.0662017337851227,-0.0670378619153675,-0.0797220994533657,-0.140838843488484,-0.143537639968533,-0.155859252005465,-0.1687773762514,-0.175740777651639,-0.212167693592043,-0.35538261997406,-0.356679636835279,-0.363977450971896,-0.364193620448766,-0.375702550799827,-0.440644676116498,-0.441476711951524,-0.454669501423637,-0.456117596195417,-0.457846952010376,-0.473411154345007,-0.476882528017779,-0.520103761348898,-0.554258538694336,-0.587116299178556,-0.797665369649806,-0.798097708603545,-0.816255944660614,-0.834846519671422,-0.846087332468656,-0.88672719412019],[0.430289532293987,0.363028953229399,0.35924276169265,0.305648185861457,0.252053610030264,0.235634743875278,0.224498886414254,0.224276169265033,0.216703786191537,0.216258351893096,0.183151683570253,0.176169265033408,0.169042316258352,0.168976646956247,0.161692650334076,0.0957683741648107,0.0697104677060133,0.0697104677060133,-0.0250756593169046,-0.0481069042316258,-0.0632516703786192,-0.0639861651534804,-0.0650334075723831,-0.0654418667799029,-0.0662017337851227,-0.0670378619153675,-0.0797220994533657,-0.140838843488484,-0.143537639968533,-0.155859252005465,-0.1687773762514,-0.175740777651639,-0.212167693592043,-0.35538261997406,-0.356679636835279,-0.363977450971896,-0.364193620448766,-0.375702550799827,-0.440644676116498,-0.441476711951524,-0.454669501423637,-0.456117596195417,-0.457846952010376,-0.473411154345007,-0.476882528017779,-0.520103761348898,-0.554258538694336,-0.587116299178556,-0.797665369649806,-0.798097708603545,-0.816255944660614,-0.834846519671422,-0.846087332468656,-0.88672719412019],[16989,1228,898,974,1050,31248,759,819,16010,2011,10409,1889,858,1389,619,1409,970,2081,1550,27557,5649,3829,4510,884.5,909.5,1550,1890.5,1639,954,999.5,13890,30753,1319.5,1010,1000,1536.5,745,1770,3660,20202.5,8764,1050,1389,1380,1495,1230,11770,30258,992,520,2810,12848,11879,1440],[2031.3,1366.7,161.3,145.2,129.1,1960.1,112.5,132.4,2199.3,1576.3,2111.25,401.3,151.8,854.45,847.6,211.4,112.8,198.2,342.2,2716.5,949,2191.2,1985.2,98.6,110.25,273.4,937.15,319.3,137.5,527.4,2547.85,1999.45,167.3,84.7,88.1,162.65,245.6,298,1840.1,2464.2,1049.8,123.2,237.3,207.2,206.25,123.2,2896.4,2038.8,127.1,378.4,1695,2211.9,1150.6,139.1],[18.26171875,40.13671875,4.6875,3.955078125,3.22265625,23.828125,7.91015625,8.69140625,368.06640625,90.13671875,18.896484375,8.88671875,5.56640625,38.037109375,7.421875,17.1875,22.55859375,28.90625,35.9375,586.81640625,38.18359375,19.53125,17.7734375,6.640625,6.982421875,19.62890625,87.548828125,6.8359375,4.541015625,6.103515625,345.263671875,23.92578125,15.380859375,5.37109375,5.2734375,26.318359375,19.921875,84.9609375,22.021484375,540.0390625,35.205078125,3.515625,4.78515625,4.78515625,17.578125,13.57421875,322.4609375,24.0234375,23.73046875,17.28515625,26.26953125,493.26171875,32.2265625,15.52734375],["<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>"]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>HVG conservation<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n      <th>Library<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bfrtip","paging":false,"columnDefs":[{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6]}],"buttons":["searchPanes",{"extend":"collection","buttons":["csv","excel","pdf"],"text":"Download"}],"language":{"searchPanes":{"collapse":"Filter Rows"}},"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render"],"jsHooks":[]}</script>
<!--### Immune (by batch)-->

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

-   **[Random Integration by Batch](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[Random Integration by Celltype](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[Combat (full/scaled)](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html)**: Missing 'method_description'. [\[hansen2012removing\]](/bibliography#hansen2012removing)

<!-- -->

-   **[Combat (full/unscaled)](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html)**: Missing 'method_description'. [\[hansen2012removing\]](/bibliography#hansen2012removing)

<!-- -->

-   **[Combat (hvg/scaled)](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html)**: Missing 'method_description'. [\[hansen2012removing\]](/bibliography#hansen2012removing)

<!-- -->

-   **[Combat (hvg/unscaled)](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html)**: Missing 'method_description'. [\[hansen2012removing\]](/bibliography#hansen2012removing)

<!-- -->

-   **[FastMNN feature (full/scaled)](https://doi.org/doi:10.18129/B9.bioc.batchelor)**: Missing 'method_description'. [\[lun2019fastmnn\]](/bibliography#lun2019fastmnn)

<!-- -->

-   **[FastMNN feature (full/unscaled)](https://doi.org/doi:10.18129/B9.bioc.batchelor)**: Missing 'method_description'. [\[lun2019fastmnn\]](/bibliography#lun2019fastmnn)

<!-- -->

-   **[FastMNN feature (hvg/scaled)](https://doi.org/doi:10.18129/B9.bioc.batchelor)**: Missing 'method_description'. [\[lun2019fastmnn\]](/bibliography#lun2019fastmnn)

<!-- -->

-   **[FastMNN feature (hvg/unscaled)](https://doi.org/doi:10.18129/B9.bioc.batchelor)**: Missing 'method_description'. [\[lun2019fastmnn\]](/bibliography#lun2019fastmnn)

<!-- -->

-   **[MNN (full/scaled)](https://github.com/chriscainx/mnnpy)**: Missing 'method_description'. [\[haghverdi2018batch\]](/bibliography#haghverdi2018batch)

<!-- -->

-   **[MNN (full/unscaled)](https://github.com/chriscainx/mnnpy)**: Missing 'method_description'. [\[haghverdi2018batch\]](/bibliography#haghverdi2018batch)

<!-- -->

-   **[MNN (hvg/scaled)](https://github.com/chriscainx/mnnpy)**: Missing 'method_description'. [\[haghverdi2018batch\]](/bibliography#haghverdi2018batch)

<!-- -->

-   **[MNN (hvg/unscaled)](https://github.com/chriscainx/mnnpy)**: Missing 'method_description'. [\[haghverdi2018batch\]](/bibliography#haghverdi2018batch)

<!-- -->

-   **[No Integration](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[Random Integration](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[SCALEX (full)](https://github.com/jsxlei/SCALEX)**: Missing 'method_description'. [\[xiong2021online\]](/bibliography#xiong2021online)

<!-- -->

-   **[SCALEX (hvg)](https://github.com/jsxlei/SCALEX)**: Missing 'method_description'. [\[xiong2021online\]](/bibliography#xiong2021online)

<!-- -->

-   **[Scanorama gene output (full/scaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama gene output (full/unscaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama gene output (hvg/scaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama gene output (hvg/unscaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **HVG conservation**: Missing 'metric_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

</details>
<details>
<summary>
Dataset descriptions
</summary>

-   **Immune (by batch)**: Missing 'dataset_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Pancreas (by batch)**: Missing 'dataset_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

</details>
<details>
<summary>
Baseline descriptions
</summary>

-   **Random Integration by Batch**: Missing 'method_description'.

<!-- -->

-   **Random Integration by Celltype**: Missing 'method_description'.

<!-- -->

-   **No Integration**: Missing 'method_description'.

<!-- -->

-   **Random Integration**: Missing 'method_description'.

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
  Task id: batch_integration_feature
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_feature
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_feature
  Field: dataset_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_feature
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_feature
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_feature
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_feature
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_feature
  Field: method_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_feature
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_feature
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_feature
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_feature
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_feature
  Field: metric_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_feature
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_feature
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_feature
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_feature
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_feature
  Field: task_description
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_feature
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_feature
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
