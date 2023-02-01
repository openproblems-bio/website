---
title: "Batch integration embed"
summary: "Removing batch effects while preserving biological variation (embedding output)"
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

<div id="htmlwidget-18bbed02136a8447e906" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-18bbed02136a8447e906">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"data":[["<a href=\"/bibliography#korsunsky2019fast\">Harmony (hvg/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/scaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (full/scaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (hvg)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (full/unscaled)<\/a>","<a href=\"/bibliography#welch2019single\">Liger (full/unscaled)<\/a>","<a href=\"/bibliography#welch2019single\">Liger (hvg/unscaled)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (full/unscaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (hvg)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (full/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (hvg/scaled)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (full/unscaled)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (hvg/unscaled)<\/a>","<a href=\"/bibliography#lopez2018deep\">scVI (full/unscaled)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (hvg/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/scaled)<\/a>","<a href=\"/bibliography#lopez2018deep\">scVI (full/unscaled)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (hvg/unscaled)<\/a>","<a href=\"/bibliography#xu2021probabilistic\">scANVI (full/unscaled)<\/a>","<a href=\"/bibliography#lopez2018deep\">scVI (full/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (full/scaled)<\/a>","<a href=\"/bibliography#lopez2018deep\">scVI (hvg/unscaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (full)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/scaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (full)<\/a>","<a href=\"/bibliography#lopez2018deep\">scVI (hvg/unscaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (full)<\/a>","<a href=\"/bibliography#lopez2018deep\">scVI (hvg/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (full/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (hvg/unscaled)<\/a>","<a href=\"/bibliography#xiong2021online\">SCALEX (hvg)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (full/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/scaled)<\/a>","<a href=\"/bibliography#welch2019single\">Liger (full/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (hvg/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/scaled)<\/a>","<a href=\"/bibliography#welch2019single\">Liger (hvg/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (full/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (full/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (full/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (full/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (full/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (hvg/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (full/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (hvg/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (full/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (hvg/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (hvg/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (full/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (hvg/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (hvg/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (full/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (full/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/unscaled)<\/a>","<a href=\"/bibliography#welch2019single\">Liger (full/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (full/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (hvg/unscaled)<\/a>","<a href=\"/bibliography#korsunsky2019fast\">Harmony (hvg/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/unscaled)<\/a>","<a href=\"/bibliography#welch2019single\">Liger (hvg/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/scaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/unscaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (full/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/unscaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (hvg/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (full/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (hvg/unscaled)<\/a>","<a href=\"/bibliography#hansen2012removing\">Combat (hvg/unscaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (full/scaled)<\/a>","<a href=\"/bibliography#haghverdi2018batch\">MNN (hvg/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (hvg/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (hvg/scaled)<\/a>","<a href=\"/bibliography#lun2019fastmnn\">FastMNN embed (full/scaled)<\/a>","<a href=\"/bibliography#hie2019efficient\">Scanorama gene output (hvg/scaled)<\/a>"],["<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","Overall mean","Overall mean","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Immune (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","Overall mean","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>","<a href=\"/bibliography#luecken2022benchmarking\">Pancreas (by batch)<\/a>"],[0.830342082143962,0.818481492415369,0.780900014851688,0.721544094696514,0.695262222490631,0.674350034602808,0.640363530320094,0.634133829250519,0.633954219686547,0.630841692361462,0.629910706441419,0.619789791452365,0.615696081692362,0.613149832439094,0.610519954898054,0.607226865263309,0.607056473757805,0.603663524472297,0.601303898087524,0.597437943698178,0.596807094046539,0.593419752710605,0.591613372265102,0.590849547664429,0.590639145661571,0.583467405171567,0.582941062620936,0.576085262678706,0.57426875297677,0.570758930705878,0.570585925580242,0.566421162232292,0.556799203408421,0.554438739869072,0.540889994218273,0.538208823730244,0.532403561951609,0.527671172054387,0.518695568158626,0.518574981746516,0.514452349890501,0.514087342556715,0.513420777779509,0.512754213002302,0.511607154970338,0.507371020481316,0.503875800331133,0.500400508382689,0.499715435058483,0.496828449749993,0.494923026268744,0.494221198322976,0.493806615072112,0.493215705387948,0.489445544154798,0.486715975717414,0.469066653509971,0.467887118784029,0.465824655636025,0.465295410724695,0.464833501267166,0.46060034902436,0.457844780931357,0.457349749648992,0.452475094082026,0.439312450900809,0.439218159630915,0.439125532528027,0.436054117140394,0.433212932663923,0.431365600486338,0.431314288544008,0.425568366523619,0.409237500760768,0.405777339361165,0.405381451323684,0.403257307066734,0.396863869796751,0.378975034159637,0.377248184419719,0.374028435402145,0.362799928890224,0.362796798907774,0.354415288692692,0.353877298724743,0.345829587579965,0.344601091446909,0.343765712565923,0.342279531443126,0.324728193487132,0.296651587908081,0.276440308905478,0.269059824590412,0.192290061600859,0.185326382562686,0.155649771902152],[0.817024723263382,0.866909742410789,0.47452401217796,0.593263708636982,0.862364979640969,0.907529931898622,0.615841008076835,0.58912476611107,0.759573111334184,0.829342073906419,0.724667368001618,0.755421547781379,0.689812562032545,0.542396853430546,0.645228123721155,0.612402520272751,0.666011503375278,0.632610439153294,0.682408187114955,0.620052012730906,0.619992754585433,0.646342906309036,0.467635113092525,0.87480332994217,0.775594330246347,0.777322432757356,0.559275937450766,0.679841535572542,0.650916761809008,0.720018089016806,0.901494512535541,0.796319168171869,0.849305285273427,0.61010191629458,0.786929798029188,0.516064490577518,0.793849624376047,0.776611576457153,0.442240520826855,0.617485618174948,0.766293354885118,0.898099268969968,0.880878404544038,0.863657540118108,0.715368810031994,0.741153454725657,0.697167999708932,0.715869070452185,0.929934892406132,0.673961703549731,0.766800074298556,0.686204736216553,0.779672046346102,0.924763279483366,0.817731078144927,0.9195916665606,0.888299955624552,0.868346930850879,0.677557700350456,0.699422103981091,0.867526259469112,0.846752563313672,0.454748272714258,0.900462597700239,0.61628103234067,0.765671044101939,0.737821490804882,0.555004364330884,0.416287973078201,0.857498994572595,0.899996163207041,0.4587351006166,0.702555605220062,0.693818372299377,0.908967483772909,0.899529728713843,0.29535627554264,0.760832407994633,0.887388576428331,0.649444429615464,0.897930126682128,0.327441304451274,0.684278918081906,0.755993771887327,0.569144104689491,0.63454495625121,0.412605603071036,0.663957755714467,0.886892769591348,0.807272671900136,0.84414058651667,0.679553108762382,0.543275012838434,0.452005069425659,0.128043206433141,0.834873297454169],[2.57636572567016,2.67175413423402,2.84624473380869,2.35601917025574,0.834887837314588,1.30182163530936,1.35786858890336,1.10294848841754,0.95098282850757,0.73506505133665,0.594545675540861,1.52908837560418,0.841109879195853,0.881609065146573,0.965574200122554,0.865008743351928,1.74357211319992,0.84431597294247,0.848408421557283,0.731236929884136,0.723057745762386,1.59461798109076,0.867115042403498,0.757287920307357,1.64934241933852,0.667893390081874,0.809604148057879,0.578498859856391,0.752093253712259,0.580739697250494,0.137514533132544,0.635242265358712,0.995728699460183,1.24364118941017,0.57918079632583,0.971107484582301,0.31491014617281,0.733952367019481,0.903251561122935,0.574731190854654,0.888723937713132,0.60616623654856,0.764814544150131,0.923462851751701,0.566933718960127,0.38645492937036,1.30170687616571,0.355981572655357,0.334454453682327,0.652252995111942,0.602379690099591,0.492305759213077,1.18457006298094,0.560246391929404,0.848777807543825,0.786038330176481,0.800232830326475,0.256899942129659,0.346419637881698,0.833216791925773,0.576226427242851,0.352220024159227,1.24614063421745,0.906202829681479,0.165215033857642,0.714689219160287,0.0608648008137105,-0.0159895701664143,0.584346380261241,0.640899492591148,0.754808759807816,1.01328368824671,-0.00490431685608753,0.481811025538206,0.0648557951054838,0.603414689934153,0.703554633828332,0.376376937321667,-0.481928815200864,0.629801520419239,0.205815932080866,-0.152359253600056,0.626930704443017,0.0380646554830471,0.287772997730186,0.386454161995521,0.574673807121942,-0.396263563082535,0.346776069056248,0.341040245488576,0.0134624066210258,-0.437737692786339,-0.00485570015533979,-0.396165562306201,-0.152359261921824,-0.502489572003783],[0.663251890474017,0.369026289600275,0.45091185162956,0.527461278262548,0.356888986188047,0.325034295796254,0.423575778165513,0.514293178403545,0.23239775666668,0.22112932854322,0.512789204618928,0.505403376624209,0.343076426560841,0.471309639408174,0.233748080774813,0.343882273285101,0.291876899339057,0.332230615862767,0.216454907162028,0.453755096455002,0.430713150950721,0.43400120318647,0.466526734718717,0.0981908804787617,0.2090517226846,0.184892494634373,0.343016309158287,0.271594108789984,0.219505883597856,0.318059039475134,0.511180921776536,0.0853696708983927,0.301525970374051,0.233610325666217,0.390372704327288,0.303596728404076,0.318297898186414,0.327215315551289,0.360557102768861,0.325149035328528,0.26405792677529,0.274175136724371,0.213624840937664,0.153074545150957,0.123328874331339,0.258191365564825,0.323710646686708,0.28482873531585,0.420699892954371,0.275721457125482,0.210038453333158,0.125414874596293,0.185444248579084,0.305355726723801,0.135248171350466,0.190011560493231,0.142086155225457,0.37242440569741,0.0358827034548521,0.340541128110392,0.240619635387434,0.33915311554941,0.189850206559666,0.131351237858113,0.144499207319947,0.188703811072265,0.317832588584747,0.253115711185042,0.18361767864264,0.132841947048555,0.192080543983844,0.137159576738983,0.310979999123761,0.347554862774401,0.306982899740973,0.252809850109575,0.206821027134178,0.178134218194823,0.44332284102077,0.247679891299659,0.163287623420266,0.325263774860801,0.0490771557689262,0.167564625317381,0.221780666054643,0.25548648411094,0.324372328954422,0.363768632682696,0.0195923470995595,0.240316943663484,0.305509576039652,0.306401755370302,0.309913461958073,0.364340439805206,0.325034011222136,0.295189638747884],[0,0,0,0,0.999115030629539,0.811083319092704,0.945027501802242,0.933240984689415,0.920569869692177,0.998493370813719,0.918394476206077,0,0.907257911300629,0.798812714822855,0.936025116621954,0.856391268599603,0,0.922247431525944,0.913969822376352,0.893945952909081,0.908469746429935,0,0.823644325942928,0.999679237780285,0,0.999818832209168,0.877660953070251,0.999958426638051,0.931677580197573,0.928670860366357,0.737833272943568,0.9978717109979,0.153420987824245,0.214963411623645,0.514515720508234,0.94857980516422,0.809841073161251,0.312825641661695,0.904874057266294,0.838148323201644,0.111135562815157,0.191624606964657,0.178596810287025,0.165569013609393,0.938947244526638,0.859880242740493,0,0.465506074310385,0,0.28311871811498,0.322103969843716,0.881848873378933,2.54566659766631e-06,0.0086695122655691,0.178701865377046,0.0173390245311382,7.0924966909716e-07,0.203093189356773,0.888763724464859,0,5.27701146488323e-07,3.46152623879485e-07,0.0882538409673705,1.15518336628706e-06,0.766829617838126,0.0374242392731724,0.351274024606314,0.644895511211393,0.952132108526197,0,6.75845853719596e-07,2.45469761003791e-06,0.778708602059547,0,0,1.96508341152127e-07,0.876507129843173,0.224842371863467,0.2527653908893,0.0939722418150608,0,0.865213327310585,0,0.412260504453761,1.22734880501896e-06,0,0,0.6975369613786,0,1.27283329883316e-06,0.099690642662751,0,0,0,0,0],[0.394675572076878,0.337150526055593,0.132648146102164,0.259401304901277,0.339426508191759,0.19686336377047,0.189078082392577,0.257980177886259,0.321854332077644,0.308630414204542,0.232290809678538,0.320575324047197,0.28500238622279,0.303851896878175,0.253846904207843,0.322023492251542,0.168891493423439,0.234350781802185,0.340195087624908,0.248150440367936,0.214854659396528,0.257736159542172,0.257334040096225,0.250805356156892,0.300237293836763,0.250401843718733,0.254036784785468,0.249998331280574,0.250739529474711,0.221681851732572,0.346678451350689,0.277834320217325,0.255557864240707,0.239897773917177,0.0655898472061971,0.142834322904406,0.298095613738948,0.145062852768757,0.200668194466208,0.341513842078895,0.224535858331317,0.20549968856788,0.223600237909866,0.241700787251852,0.211072893786607,0.299094738414577,0.196871938328208,0.253259971684196,0.308961318914888,0.220988023167532,0.267349111208317,0.249512776127207,0.311279805869757,0.298268913004528,0.281438250732439,0.287576507094169,0.296217357436288,0.262567179311614,0.228754277235266,0.256071014183068,0.307137977812783,0.318058598189278,0.258859733812755,0.331806221225661,0.247604177468588,0.252052508755492,0.202078272417887,0.266454077701909,0.0965905634162349,0.205134840744714,0.364061944967837,0.282147191982371,0.407615832080041,0.246475076017516,0.284434740768801,0.396317668710014,0.143356211046157,0.266143206019514,0.269576494382521,0.249628992901794,0.265625129941367,0.48616432038732,0.263324061617932,0.280233903283536,0.279374430393789,0.29908363168422,0.341518119446147,0.516136925745504,0.246815519113933,0.353931134472838,0.240398251990832,0.276601668805207,0.407615841194363,0.516148050704507,0.486164300564085,0.396582463075919],[0.530734581379332,0.666048262191532,0.781071345391749,0.593119106122538,0.778889992978884,0.503767661749436,0.310790222580032,0.407215379995287,0.618347419841025,0.69238991536422,0.79677670460249,0.608250124657219,0.627917324841517,0.680918824948242,0.628697303940009,0.643652893818929,0.771986833209137,0.656225905547119,0.606386962689616,0.637487229842009,0.68375450715423,0.627820266135191,0.66742497733672,0.564330561321108,0.609609107863197,0.6204754376279,0.654052243202965,0.676620313934693,0.64067950906921,0.655384046393906,0.788813861742577,0.605889837749556,0.785256413277913,0.784417822302641,0.908751098912902,0.347070110748941,0.659427016074185,0.870359278867949,0.300581972500605,0.414421880840427,0.831967458822996,0.908959117564855,0.819009828848328,0.7290605401318,0.513991388185323,0.499451392071981,0.503797341097243,0.926957625878164,1.00424205239318,0.874927801430294,0.800866858829124,0.530040170405793,0.501870980990198,0.861990408921021,0.674776091780084,0.719738765448863,0.687562913197386,0.843991065357838,0.617569890429021,0.662521426147844,0.797490179989669,0.907417446781952,0.509215997316637,0.474274456245094,0.774421495667184,0.677333883041701,0.965437780557947,0.931273100905347,0.38334999891785,0.762902321026525,0.377245515105638,0.696557718981775,0.358454477514393,0.685765667935106,0.869423116778821,0.280216573966181,0.193948565005922,0.5748540773864,0.902725717437763,0.392962030467096,0.711511800288244,0.325076099931418,0.553169953534861,0.472374271731099,0.765190366131546,0.499408291437901,0.41443669008791,0.217457562956805,0.553600483797667,0.20580689256446,0.276708063617555,0.833823013281317,0.358410331706941,0.217412371975982,0.325076039078578,-0.0902571958612774],[2050,848,1149,1931,3790,880,29559,4280,25942,5415,1952,1740.5,27165.5,4498,55979,6807,964,38513.5,9116,28389,21048,1806.5,25098,28229,914,27314,24229.5,26399,23361,1906.5,1884,7040,739,4820,28350,23879.5,1777,18719.5,4094.5,839.5,9089,11450,7135.5,2821,1861,819,1200,12240,1197,3305.5,17749,1670,1839,1283,23258,1369,2630,993,840,1682,2149,1668,14477,659,919,5360,1791,998,18200,779,1033,2810,713.5,1431,848,1407,3909,8214.5,1247,13703,929,799,980,11069,2288.5,730,1119,608,1010,1543,12929,1767,674,618,1038,1247],[507.8,169.1,261.5,1034,2176,83.6,101.5,101.7,1558.3,1885.25,1135.7,722.3,1553.7,1389.4,2277.7,1728.3,362.05,2434.45,2067.2,1549.1,2591.2,1214.9,1379.8,2497,156.1,2278.6,1392.5,2060.2,1405.2,1168.05,1043.1,1594.5,412,1271.6,2672,100.95,1087.3,1974.75,102.4,81.35,1277.5,1305.5,1281.6,1257.7,1200.4,70.4,88.2,2649.1,217.4,1302.95,2227.4,1131.5,321.7,370.45,1805.7,523.5,1280.3,301.55,156.7,1395.8,797.55,314.8,1468.9,798.9,160.45,1839.4,1334.3,164.2,100.4,462.6,506.5,1416.6,69.1,936.8,214,214.1,103.1,1552.55,191.1,1246.9,181.75,79.1,143.1,1265.7,860.15,77.7,87.6,67.8,149.5,328.95,1024.9,303.7,73.1,68.5,87,336.2],[2.5390625,3.61328125,15.52734375,7.32421875,19.53125,6.93359375,15.13671875,4.78515625,5.6640625,18.9453125,2.44140625,2.734375,5.712890625,3.7109375,3.3203125,8.88671875,17.578125,3.515625,14.0625,5.76171875,3.7109375,8.0078125,3.22265625,23.73046875,4.6875,23.876953125,3.173828125,24.0234375,3.125,2.392578125,2.05078125,18.359375,8.69140625,38.18359375,492.578125,14.208984375,2.099609375,538.8671875,4.19921875,6.689453125,585.15625,26.3671875,22.0703125,17.7734375,2.34375,3.125,13.18359375,324.8046875,4.6875,34.228515625,346.337890625,2.1484375,8.7890625,6.005859375,367.87109375,7.32421875,74.4140625,6.787109375,17.1875,8.69140625,43.701171875,12.98828125,38.18359375,7.32421875,15.380859375,17.7734375,30.2734375,13.57421875,13.28125,19.62890625,6.0546875,132.2265625,3.076171875,2.9296875,3.22265625,4.78515625,3.61328125,22.021484375,4.8828125,34.27734375,3.955078125,6.4453125,5.76171875,26.26953125,104.345703125,4.1015625,12.20703125,3.02734375,4.6875,6.8359375,30.37109375,76.46484375,3.662109375,3.22265625,11.23046875,4.8828125],["<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/welch-lab/liger\">v0.5.0.9000<\/a>","<a href=\"https://github.com/welch-lab/liger\">v0.5.0.9000<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://github.com/YosefLab/scvi-tools\">v0.19.0<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/jsxlei/SCALEX\">v1.0.2<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/welch-lab/liger\">v0.5.0.9000<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/welch-lab/liger\">v0.5.0.9000<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/welch-lab/liger\">v0.5.0.9000<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/lilab-bcb/harmony-pytorch\">v0.1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/welch-lab/liger\">v0.5.0.9000<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html\">v1.9.1<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>","<a href=\"https://github.com/chriscainx/mnnpy\">v0.1.9.5<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://doi.org/doi:10.18129/B9.bioc.batchelor\">v1.12.3<\/a>","<a href=\"https://github.com/brianhie/scanorama\">v1.7<\/a>"]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>Cell Cycle Score<\/th>\n      <th>Isolated label Silhouette<\/th>\n      <th>kBET<\/th>\n      <th>PC Regression<\/th>\n      <th>Silhouette<\/th>\n      <th>Batch ASW<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n      <th>Library<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bfrtip","paging":false,"columnDefs":[{"targets":10,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":9,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":11,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8,9,10,11,12]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8,9,10,11]}],"buttons":["searchPanes",{"extend":"collection","buttons":["csv","excel","pdf"],"text":"Download"}],"language":{"searchPanes":{"collapse":"Filter Rows"}},"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render","options.columnDefs.7.render","options.columnDefs.8.render","options.columnDefs.9.render"],"jsHooks":[]}</script>
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

-   **[Random Embedding by Celltype](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

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

-   **[FastMNN embed (full/scaled)](https://doi.org/doi:10.18129/B9.bioc.batchelor)**: Missing 'method_description'. [\[lun2019fastmnn\]](/bibliography#lun2019fastmnn)

<!-- -->

-   **[FastMNN embed (full/unscaled)](https://doi.org/doi:10.18129/B9.bioc.batchelor)**: Missing 'method_description'. [\[lun2019fastmnn\]](/bibliography#lun2019fastmnn)

<!-- -->

-   **[FastMNN embed (hvg/scaled)](https://doi.org/doi:10.18129/B9.bioc.batchelor)**: Missing 'method_description'. [\[lun2019fastmnn\]](/bibliography#lun2019fastmnn)

<!-- -->

-   **[FastMNN embed (hvg/unscaled)](https://doi.org/doi:10.18129/B9.bioc.batchelor)**: Missing 'method_description'. [\[lun2019fastmnn\]](/bibliography#lun2019fastmnn)

<!-- -->

-   **[Harmony (full/scaled)](https://github.com/lilab-bcb/harmony-pytorch)**: Missing 'method_description'. [\[korsunsky2019fast\]](/bibliography#korsunsky2019fast)

<!-- -->

-   **[Harmony (full/unscaled)](https://github.com/lilab-bcb/harmony-pytorch)**: Missing 'method_description'. [\[korsunsky2019fast\]](/bibliography#korsunsky2019fast)

<!-- -->

-   **[Harmony (hvg/scaled)](https://github.com/lilab-bcb/harmony-pytorch)**: Missing 'method_description'. [\[korsunsky2019fast\]](/bibliography#korsunsky2019fast)

<!-- -->

-   **[Harmony (hvg/unscaled)](https://github.com/lilab-bcb/harmony-pytorch)**: Missing 'method_description'. [\[korsunsky2019fast\]](/bibliography#korsunsky2019fast)

<!-- -->

-   **[Liger (full/unscaled)](https://github.com/welch-lab/liger)**: Missing 'method_description'. [\[welch2019single\]](/bibliography#welch2019single)

<!-- -->

-   **[Liger (hvg/unscaled)](https://github.com/welch-lab/liger)**: Missing 'method_description'. [\[welch2019single\]](/bibliography#welch2019single)

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

-   **[No Integration by Batch](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[Random Integration](https://github.com/openproblems-bio/openproblems)**: Missing 'method_description'. [\[openproblems\]](/bibliography#openproblems)

<!-- -->

-   **[SCALEX (full)](https://github.com/jsxlei/SCALEX)**: Missing 'method_description'. [\[xiong2021online\]](/bibliography#xiong2021online)

<!-- -->

-   **[SCALEX (hvg)](https://github.com/jsxlei/SCALEX)**: Missing 'method_description'. [\[xiong2021online\]](/bibliography#xiong2021online)

<!-- -->

-   **[Scanorama (full/scaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama (full/unscaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama (hvg/scaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama (hvg/unscaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama gene output (full/scaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama gene output (full/unscaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama gene output (hvg/scaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[Scanorama gene output (hvg/unscaled)](https://github.com/brianhie/scanorama)**: Missing 'method_description'. [\[hie2019efficient\]](/bibliography#hie2019efficient)

<!-- -->

-   **[scANVI (full/unscaled)](https://github.com/YosefLab/scvi-tools)**: Missing 'method_description'. [\[xu2021probabilistic\]](/bibliography#xu2021probabilistic)

<!-- -->

-   **[scANVI (hvg/unscaled)](https://github.com/YosefLab/scvi-tools)**: Missing 'method_description'. [\[xu2021probabilistic\]](/bibliography#xu2021probabilistic)

<!-- -->

-   **[scVI (full/unscaled)](https://github.com/YosefLab/scvi-tools)**: Missing 'method_description'. [\[lopez2018deep\]](/bibliography#lopez2018deep)

<!-- -->

-   **[scVI (hvg/unscaled)](https://github.com/YosefLab/scvi-tools)**: Missing 'method_description'. [\[lopez2018deep\]](/bibliography#lopez2018deep)

</details>
<details>
<summary>
Metric descriptions
</summary>

-   **Cell Cycle Score**: Missing 'metric_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Isolated label Silhouette**: Missing 'metric_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **kBET**: Missing 'metric_description'. [\[bttner2018test\]](/bibliography#bttner2018test)

<!-- -->

-   **PC Regression**: Missing 'metric_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Silhouette**: Missing 'metric_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

<!-- -->

-   **Batch ASW**: Missing 'metric_description'. [\[luecken2022benchmarking\]](/bibliography#luecken2022benchmarking)

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

-   **Random Embedding by Celltype**: Missing 'method_description'.

<!-- -->

-   **Random Integration by Celltype**: Missing 'method_description'.

<!-- -->

-   **No Integration**: Missing 'method_description'.

<!-- -->

-   **No Integration by Batch**: Missing 'method_description'.

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
  Task id: batch_integration_embed
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_embed
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_embed
  Field: dataset_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_embed
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_embed
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_embed
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_embed
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_embed
  Field: method_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_embed
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_embed
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_embed
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_embed
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_embed
  Field: metric_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_embed
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_embed
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_embed
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_embed
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_embed
  Field: task_description
"> 1.0000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_embed
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_embed
  Field: task_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_full_scaled
  Percentage missing: 17%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_full_scaled
  Percentage missing: 17%
"> Method 'combat_full_scaled' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_full_scaled
  Percentage missing: 17%
"> 0.1666667 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_full_scaled
  Percentage missing: 17%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_full_scaled
  Percentage missing: 17%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_scaled
  Percentage missing: 17%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_scaled
  Percentage missing: 17%
"> Method 'combat_hvg_scaled' %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_scaled
  Percentage missing: 17%
"> 0.1666667 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_scaled
  Percentage missing: 17%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_scaled
  Percentage missing: 17%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.8462447338086947%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.8462447338086947%
"> Best score combat_full_scaled isolated_labels_sil </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.8462447338086947%
"> 2.8462447 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.8462447338086947%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.8462447338086947%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.6717541342340247%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.6717541342340247%
"> Best score combat_hvg_scaled isolated_labels_sil </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.6717541342340247%
"> 2.6717541 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.6717541342340247%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: combat_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.6717541342340247%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.576365725670163%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.576365725670163%
"> Best score harmony_hvg_scaled isolated_labels_sil </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.576365725670163%
"> 2.5763657 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.576365725670163%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_hvg_scaled
  Metric id: isolated_labels_sil
  Best score: 2.576365725670163%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.356019170255741%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.356019170255741%
"> Best score harmony_full_scaled isolated_labels_sil </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.356019170255741%
"> 2.3560192 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.356019170255741%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_embed
  Method id: harmony_full_scaled
  Metric id: isolated_labels_sil
  Best score: 2.356019170255741%
"> ✗ </td>
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
