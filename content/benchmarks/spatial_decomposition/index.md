---
title: "Spatial Decomposition"
summary: "Calling cell-type compositions for spot-based spatial transcriptomics data"
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
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="771" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true"><strong>Overview of the results per method</strong>. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Scaled scores

<div id="htmlwidget-9a8aeed7b8a10c10c9c7" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-9a8aeed7b8a10c10c9c7">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"data":[["<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location, amortised (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=1, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=200, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference NB without batch info)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location, amortised (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location, amortised (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=200, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=1, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference NB without batch info)<\/a>","<a href=\"/bibliography#lawson1995solving\">Non-Negative Least Squares<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference NB without batch info)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=200, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=1, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=1, reference hard-coded)<\/a>","<a href=\"/bibliography#cable2021robust\">RCTD<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference NB without batch info)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=200, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location, amortised (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=1, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=200, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference NB without batch info)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location, amortised (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=1, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=200, reference hard-coded)<\/a>","<a href=\"/bibliography#cable2021robust\">RCTD<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location, amortised (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference NB without batch info)<\/a>","<a href=\"/bibliography#lawson1995solving\">Non-Negative Least Squares<\/a>","<a href=\"/bibliography#cable2021robust\">RCTD<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=1, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=200, reference hard-coded)<\/a>","<a href=\"/bibliography#cable2021robust\">RCTD<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=1, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference NB without batch info)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=200, reference hard-coded)<\/a>","<a href=\"/bibliography#cichocki2009fast\">Non-Negative Matrix Factorization (NMF)<\/a>","<a href=\"/bibliography#cable2021robust\">RCTD<\/a>","<a href=\"/bibliography#lawson1995solving\">Non-Negative Least Squares<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location (detection_alpha=20, reference NB without batch info)<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location, amortised (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#cable2021robust\">RCTD<\/a>","<a href=\"/bibliography#kleshchevnikov2022cell2location\">Cell2location, amortised (detection_alpha=20, reference hard-coded)<\/a>","<a href=\"/bibliography#cable2021robust\">RCTD<\/a>","<a href=\"/bibliography#lawson1995solving\">Non-Negative Least Squares<\/a>","<a href=\"/bibliography#andersson2020single\">Stereoscope<\/a>","<a href=\"/bibliography#andersson2020single\">Stereoscope<\/a>","<a href=\"/bibliography#lawson1995solving\">Non-Negative Least Squares<\/a>","<a href=\"/bibliography#cable2021robust\">RCTD<\/a>","<a href=\"/bibliography#andersson2020single\">Stereoscope<\/a>","<a href=\"/bibliography#cichocki2009fast\">Non-Negative Matrix Factorization (NMF)<\/a>","<a href=\"/bibliography#cichocki2009fast\">Non-Negative Matrix Factorization (NMF)<\/a>","<a href=\"/bibliography#andersson2020single\">Stereoscope<\/a>","<a href=\"/bibliography#andersson2020single\">Stereoscope<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#lawson1995solving\">Non-Negative Least Squares<\/a>","<a href=\"/bibliography#andersson2020single\">Stereoscope<\/a>","<a href=\"/bibliography#lawson1995solving\">Non-Negative Least Squares<\/a>","<a href=\"/bibliography#rodriques2019slide\">NMF-reg<\/a>","<a href=\"/bibliography#andersson2020single\">Stereoscope<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#lawson1995solving\">Non-Negative Least Squares<\/a>","<a href=\"/bibliography#rodriques2019slide\">NMF-reg<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#cichocki2009fast\">Non-Negative Matrix Factorization (NMF)<\/a>","<a href=\"/bibliography#rodriques2019slide\">NMF-reg<\/a>","<a href=\"/bibliography#rodriques2019slide\">NMF-reg<\/a>","<a href=\"/bibliography#cichocki2009fast\">Non-Negative Matrix Factorization (NMF)<\/a>","<a href=\"/bibliography#andersson2020single\">Stereoscope<\/a>","<a href=\"/bibliography#cichocki2009fast\">Non-Negative Matrix Factorization (NMF)<\/a>","<a href=\"/bibliography#cichocki2009fast\">Non-Negative Matrix Factorization (NMF)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#stuart2019comprehensive\">SeuratV3<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#rodriques2019slide\">NMF-reg<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#cichocki2009fast\">Non-Negative Matrix Factorization (NMF)<\/a>","<a href=\"/bibliography#rodriques2019slide\">NMF-reg<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#stuart2019comprehensive\">SeuratV3<\/a>","<a href=\"/bibliography#biancalani2021deep\">Tangram<\/a>","<a href=\"/bibliography#biancalani2021deep\">Tangram<\/a>","<a href=\"/bibliography#biancalani2021deep\">Tangram<\/a>","<a href=\"/bibliography#biancalani2021deep\">Tangram<\/a>","<a href=\"/bibliography#biancalani2021deep\">Tangram<\/a>","<a href=\"/bibliography#rodriques2019slide\">NMF-reg<\/a>","<a href=\"/bibliography#stuart2019comprehensive\">SeuratV3<\/a>","<a href=\"/bibliography#biancalani2021deep\">Tangram<\/a>","<a href=\"/bibliography#stuart2019comprehensive\">SeuratV3<\/a>","<a href=\"/bibliography#biancalani2021deep\">Tangram<\/a>","<a href=\"/bibliography#stuart2019comprehensive\">SeuratV3<\/a>","<a href=\"/bibliography#stuart2019comprehensive\">SeuratV3<\/a>","<a href=\"/bibliography#rodriques2019slide\">NMF-reg<\/a>","<a href=\"/bibliography#stuart2019comprehensive\">SeuratV3<\/a>","<a href=\"/bibliography#biancalani2021deep\">Tangram<\/a>","<a href=\"/bibliography#stuart2019comprehensive\">SeuratV3<\/a>"],["<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=0.5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=5)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=0.5)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=5)<\/a>","Overall mean","<a href=\"/bibliography#tabula2020single\">Tabula muris senis (alpha=1)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (alpha=1)<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>","<a href=\"/bibliography#lopez2022destvi\">DestVI<\/a>"],[0.938232060408914,0.927220297993309,0.926978646239252,0.92624004172418,0.925860479954771,0.901607874896548,0.90134173418126,0.898405810246326,0.89840133097297,0.898395883259656,0.898216489533274,0.898151642195188,0.897541745967031,0.896193262791384,0.895396904177043,0.894989992837817,0.874000482377635,0.873236485988656,0.873229294215011,0.872656606420696,0.867235908600057,0.864027945032441,0.850721062885752,0.849661043139753,0.84720099801196,0.843151808214128,0.839446825076579,0.836552318492547,0.835271637593787,0.833320175487664,0.828056264461866,0.826269928733954,0.82355715440992,0.812098546717623,0.781324334724555,0.770154030497462,0.766418056561014,0.762496562531573,0.759603172076405,0.753976086495897,0.751466109645112,0.747481288209473,0.747311583316874,0.745487142219161,0.741199784047366,0.738827482484862,0.736176205209414,0.734407812131851,0.733763838319651,0.710240420151086,0.698097064159063,0.697114209461223,0.684052907394539,0.669182788429334,0.668143456367599,0.661544432833675,0.631603504784515,0.625764961097994,0.607607900504665,0.577822503498685,0.559044206738948,0.538727680128474,0.533121857292658,0.520668873859482,0.507876729268587,0.500472703263322,0.49530162777347,0.494958105161932,0.48981372715305,0.470129487635342,0.460519567868247,0.441261081565901,0.407414607765938,0.396577767831607,0.34867419752015,0.334677241432612,0.318572306165349,0.315855399631147,0.297648327573047,0.294967543701427,0.188573148718442,0.150988144777334,0.144811658921822,0.131064395743278,0.126865663822845,0.105054296155784,-0.00913341534232281,-0.106597991494845,-0.137431272137131,-0.17225993457808,-0.18864207538972,-0.193585022720961,-0.210571310016285,-0.236084552590094,-0.241376886431896,-0.245313149251227,-0.272927369393957,-0.298659398070576,-0.369344406789293,-0.582764449171099,-0.629882697609147,-0.702320781830095,-0.942813022400626,-2.57535685697605],[0.938232060408914,0.927220297993309,0.926978646239252,0.92624004172418,0.925860479954771,0.901607874896548,0.90134173418126,0.898405810246326,0.89840133097297,0.898395883259656,0.898216489533274,0.898151642195188,0.897541745967031,0.896193262791384,0.895396904177043,0.894989992837817,0.874000482377635,0.873236485988656,0.873229294215011,0.872656606420696,0.867235908600057,0.864027945032441,0.850721062885752,0.849661043139753,0.84720099801196,0.843151808214128,0.839446825076579,0.836552318492547,0.835271637593787,0.833320175487664,0.828056264461866,0.826269928733954,0.82355715440992,0.812098546717623,0.781324334724555,0.770154030497462,0.766418056561014,0.762496562531573,0.759603172076405,0.753976086495897,0.751466109645112,0.747481288209473,0.747311583316874,0.745487142219161,0.741199784047366,0.738827482484862,0.736176205209414,0.734407812131851,0.733763838319651,0.710240420151086,0.698097064159063,0.697114209461223,0.684052907394539,0.669182788429334,0.668143456367599,0.661544432833675,0.631603504784515,0.625764961097994,0.607607900504665,0.577822503498685,0.559044206738948,0.538727680128474,0.533121857292658,0.520668873859482,0.507876729268587,0.500472703263322,0.49530162777347,0.494958105161932,0.48981372715305,0.470129487635342,0.460519567868247,0.441261081565901,0.407414607765938,0.396577767831607,0.34867419752015,0.334677241432612,0.318572306165349,0.315855399631147,0.297648327573047,0.294967543701427,0.188573148718442,0.150988144777334,0.144811658921822,0.131064395743278,0.126865663822845,0.105054296155784,-0.00913341534232281,-0.106597991494845,-0.137431272137131,-0.17225993457808,-0.18864207538972,-0.193585022720961,-0.210571310016285,-0.236084552590094,-0.241376886431896,-0.245313149251227,-0.272927369393957,-0.298659398070576,-0.369344406789293,-0.582764449171099,-0.629882697609147,-0.702320781830095,-0.942813022400626,-2.57535685697605],[27260,24193,24945,4316,31740,15649,31170,24719,16749,11958,24307,320,10908,8841,4881,22372,7701,700,24327,27400,22661,13431,15736.5714285714,21646.1428571429,17112.7142857143,24436,25624.7142857143,15928,26349,23792,677,27581,26119,80,958,23772,23811,26544,1289.71428571429,3480,24180,26982,12876,330,3949,79,26669,58845,687,5437,1008,389,3817,369,242.714285714286,1049,3599,429,390,4802,4058.57142857143,25920,399,379,370,150,615,8760,62,159,24093,301.285714285714,350,470,599,14829,90,171,1299,12006.2857142857,1008,5963,489.428571428571,1449,100,869,16560,988,395,169,685,1149,1082,559,949,159,769,1369.85714285714,727,836.714285714286,869,727,5950,689],[1735.7,1410.2,1410.7,1048.7,1494.4,2093.1,1849.5,1793.5,1904.6,1274.3,1142.9,55.9,1290.6,941.2,838.6,1227.1,916.1,66.1,1140.9,1429.5,1432.7,1239.2,1169.17142857143,1385.85714285714,1270.5,1393.84285714286,1527.22857142857,962.4,1435.1,1448,84.5,1616.6,1504.1,112.1,93.8,1445,1451.5,1416.2,87.7714285714286,948.6,1128.9,1493,915.8,162.5,100.4,124.4,1691,1582.3,84.6,574.2,90.7,20.8,1460.7,1359.5,59.4285714285714,94.3,1676.6,1089.1,553.6,1576,1639.85714285714,1650.8,24.7,1265.1,17,1310.7,1593.5,1373.9,61.1,1447.3,1652.1,712.314285714286,2005.3,246.5,573.9,2547.6,1055.3,320.3,1258.5,1620.25714285714,116.7,1599.5,1027.25714285714,1233.8,1231.5,508.5,2573.2,120.5,1048.8,364,1198.5,1518.6,1538.7,1162,127.2,627.9,93.8,1143.17142857143,113,114.485714285714,510.5,114.1,1705.7,116.1],[14.2578125,4.4921875,5.859375,5.859375,3.125,40.72265625,14.94140625,5.078125,4.98046875,3.515625,3.125,0.6466796875,3.515625,1.171875,1.46484375,4.1015625,5.859375,2.34375,3.125,1.85546875,5.56640625,14.94140625,3.36216517857143,2.34375,3.11104910714286,4.24107142857143,18.1501116071429,1.26953125,1.26953125,1.26953125,2.34375,15.234375,6.0546875,0.40244140625,4.98046875,1.3671875,1.26953125,1.26953125,3.69698660714286,1.5625,1.3671875,5.37109375,1.26953125,0.64658203125,3.90625,0.37236328125,5.37109375,14.35546875,2.34375,12.59765625,4.98046875,0.829296875,1.3671875,1.171875,0.504366629464286,4.98046875,1.46484375,0.82802734375,0.82822265625,1.3671875,1.32533482142857,2.1484375,0.2263671875,1.171875,0.828515625,1.3671875,1.26953125,2.05078125,0.22490234375,1.3671875,2.05078125,0.813309151785714,1.46484375,2.24609375,0.8275390625,1.46484375,0.647265625,1.26953125,1.66015625,2.37165178571429,212.79296875,1.953125,2.41350446428571,1.66015625,0.64599609375,3.61328125,5.078125,191.40625,1.3671875,0.9765625,0.9765625,1.3671875,1.3671875,3.61328125,184.27734375,0.9765625,99.70703125,1.45089285714286,93.75,170.186941964286,3.22265625,101.66015625,3.125,307.71484375],["<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html\">v1.9.3<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/dmcable/spacexr\">v2.0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/dmcable/spacexr\">v2.0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html\">v1.9.3<\/a>","<a href=\"https://github.com/dmcable/spacexr\">v2.0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/dmcable/spacexr\">v2.0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html\">v1.0.2<\/a>","<a href=\"https://github.com/dmcable/spacexr\">v2.0.1<\/a>","<a href=\"https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html\">v1.9.3<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/dmcable/spacexr\">v2.0.1<\/a>","<a href=\"https://github.com/BayraktarLab/cell2location\">v0.1<\/a>","<a href=\"https://github.com/dmcable/spacexr\">v2.0.1<\/a>","<a href=\"https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html\">v1.9.3<\/a>","<a href=\"https://github.com/scverse/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/scverse/scvi-tools\">v0.19.0<\/a>","<a href=\"https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html\">v1.9.3<\/a>","<a href=\"https://github.com/dmcable/spacexr\">v2.0.1<\/a>","<a href=\"https://github.com/scverse/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html\">v1.0.2<\/a>","<a href=\"https://github.com/scverse/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/scverse/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html\">v1.9.3<\/a>","<a href=\"https://github.com/scverse/scvi-tools\">v0.19.0<\/a>","<a href=\"https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html\">v1.9.3<\/a>","<a href=\"https://github.com/tudaga/NMFreg_tutorial\">v1.0.2<\/a>","<a href=\"https://github.com/scverse/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html\">v1.9.3<\/a>","<a href=\"https://github.com/tudaga/NMFreg_tutorial\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html\">v1.0.2<\/a>","<a href=\"https://github.com/tudaga/NMFreg_tutorial\">v1.0.2<\/a>","<a href=\"https://github.com/tudaga/NMFreg_tutorial\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html\">v1.0.2<\/a>","<a href=\"https://github.com/scverse/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html\">v1.0.2<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html\">v4.1.1<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/tudaga/NMFreg_tutorial\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html\">v1.0.2<\/a>","<a href=\"https://github.com/tudaga/NMFreg_tutorial\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html\">v4.1.1<\/a>","<a href=\"https://github.com/broadinstitute/Tangram\">v1.0.3<\/a>","<a href=\"https://github.com/broadinstitute/Tangram\">v1.0.3<\/a>","<a href=\"https://github.com/broadinstitute/Tangram\">v1.0.3<\/a>","<a href=\"https://github.com/broadinstitute/Tangram\">v1.0.3<\/a>","<a href=\"https://github.com/broadinstitute/Tangram\">v1.0.3<\/a>","<a href=\"https://github.com/tudaga/NMFreg_tutorial\">v1.0.2<\/a>","<a href=\"https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html\">v4.1.1<\/a>","<a href=\"https://github.com/broadinstitute/Tangram\">v1.0.3<\/a>","<a href=\"https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html\">v4.1.1<\/a>","<a href=\"https://github.com/broadinstitute/Tangram\">v1.0.3<\/a>","<a href=\"https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html\">v4.1.1<\/a>","<a href=\"https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html\">v4.1.1<\/a>","<a href=\"https://github.com/tudaga/NMFreg_tutorial\">v1.0.2<\/a>","<a href=\"https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html\">v4.1.1<\/a>","<a href=\"https://github.com/broadinstitute/Tangram\">v1.0.3<\/a>","<a href=\"https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html\">v4.1.1<\/a>"]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>r2<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n      <th>Library<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bfrtip","paging":false,"columnDefs":[{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6]}],"buttons":["searchPanes",{"extend":"collection","buttons":["csv","excel","pdf"],"text":"Download"}],"language":{"searchPanes":{"collapse":"Filter Rows"}},"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render"],"jsHooks":[]}</script>
<!--### DestVI-->

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

-   **[Cell2location, amortised (detection_alpha=20, reference hard-coded)](https://github.com/BayraktarLab/cell2location)**: Missing 'method_description'. [\[kleshchevnikov2022cell2location\]](/bibliography#kleshchevnikov2022cell2location)

<!-- -->

-   **[Cell2location (detection_alpha=1, reference hard-coded)](https://github.com/BayraktarLab/cell2location)**: Missing 'method_description'. [\[kleshchevnikov2022cell2location\]](/bibliography#kleshchevnikov2022cell2location)

<!-- -->

-   **[Cell2location (detection_alpha=20, reference hard-coded)](https://github.com/BayraktarLab/cell2location)**: Missing 'method_description'. [\[kleshchevnikov2022cell2location\]](/bibliography#kleshchevnikov2022cell2location)

<!-- -->

-   **[Cell2location (detection_alpha=200, reference hard-coded)](https://github.com/BayraktarLab/cell2location)**: Missing 'method_description'. [\[kleshchevnikov2022cell2location\]](/bibliography#kleshchevnikov2022cell2location)

<!-- -->

-   **[Cell2location (detection_alpha=20, reference NB without batch info)](https://github.com/BayraktarLab/cell2location)**: Missing 'method_description'. [\[kleshchevnikov2022cell2location\]](/bibliography#kleshchevnikov2022cell2location)

<!-- -->

-   **[DestVI](https://github.com/YosefLab/scvi-tools)**: Missing 'method_description'. [\[lopez2022destvi\]](/bibliography#lopez2022destvi)

<!-- -->

-   **[Non-Negative Matrix Factorization (NMF)](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html)**: Missing 'method_description'. [\[cichocki2009fast\]](/bibliography#cichocki2009fast)

<!-- -->

-   **[NMF-reg](https://github.com/tudaga/NMFreg_tutorial)**: Missing 'method_description'. [\[rodriques2019slide\]](/bibliography#rodriques2019slide)

<!-- -->

-   **[Non-Negative Least Squares](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html)**: Missing 'method_description'. [\[lawson1995solving\]](/bibliography#lawson1995solving)

<!-- -->

-   **[Random Proportions](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[RCTD](https://github.com/dmcable/spacexr)**: Missing 'method_description'. [\[cable2021robust\]](/bibliography#cable2021robust)

<!-- -->

-   **[SeuratV3](https://satijalab.org/seurat/archive/v3.2/spatial_vignette.html)**: Missing 'method_description'. [\[stuart2019comprehensive\]](/bibliography#stuart2019comprehensive)

<!-- -->

-   **[Stereoscope](https://github.com/scverse/scvi-tools)**: Missing 'method_description'. [\[andersson2020single\]](/bibliography#andersson2020single)

<!-- -->

-   **[Tangram](https://github.com/broadinstitute/Tangram)**: Missing 'method_description'. [\[biancalani2021deep\]](/bibliography#biancalani2021deep)

<!-- -->

-   **[True Proportions](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **r2**: Missing 'metric_description'. [\[miles2005rsquared\]](/bibliography#miles2005rsquared)

</details>
<details>
<summary>
Dataset descriptions
</summary>

-   **DestVI**: Missing 'dataset_description'. [\[lopez2022destvi\]](/bibliography#lopez2022destvi)

<!-- -->

-   **Pancreas (alpha=0.5)**: Missing 'dataset_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Pancreas (alpha=1)**: Missing 'dataset_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Pancreas (alpha=5)**: Missing 'dataset_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Tabula muris senis (alpha=0.5)**: Missing 'dataset_description'. [\[tabula2020single\]](/bibliography#tabula2020single)

<!-- -->

-   **Tabula muris senis (alpha=1)**: Missing 'dataset_description'. [\[tabula2020single\]](/bibliography#tabula2020single)

<!-- -->

-   **Tabula muris senis (alpha=5)**: Missing 'dataset_description'. [\[tabula2020single\]](/bibliography#tabula2020single)

</details>
<details>
<summary>
Baseline descriptions
</summary>

-   **Random Proportions**: Missing 'method_description'.

<!-- -->

-   **True Proportions**: Missing 'method_description'.

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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: spatial_decomposition
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: spatial_decomposition
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: spatial_decomposition
  Field: task_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: spatial_decomposition
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: spatial_decomposition
  Field: task_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.5753568569760525%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.5753568569760525%
"> Worst score seuratv3 r2 </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.5753568569760525%
"> -2.575357 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.5753568569760525%
"> worst_score &gt;= -1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method seuratv3 performs much worse than baselines.
  Task id: spatial_decomposition
  Method id: seuratv3
  Metric id: r2
  Worst score: -2.5753568569760525%
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
