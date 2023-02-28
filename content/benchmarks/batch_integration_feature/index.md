---
title: "Batch integration feature"
summary: "Removing batch effects while preserving biological variation (feature output)"
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

<!--- TODO: add links --->

## The task

This is a sub-task of the overall batch integration task. Batch (or data) integration
integrates datasets across batches that arise from various biological and technical
sources. Methods that integrate batches typically have three different types of output:
a corrected feature matrix, a joint embedding across batches, and/or an integrated
cell-cell similarity graph (e.g., a kNN graph). This sub-task focuses on all methods
that can output feature matrices. Other sub-tasks for batch integration can be found
for:

-   [graphs](../batch_integration_graph/), and
-   [embeddings](../batch_integration_embed/)

This sub-task was taken from a [benchmarking study of data integration
methods](https://openproblems.bio/bibliography#luecken2022benchmarking).

## The metrics

Metrics for batch integration (feature) measure how well feature-level information is
batch corrected. This is only done on by capturing biological variance conservation.
Further metrics for batch correction and biological variance conservation that are
calculated on lower dimensional feature spaces extrapolated from corrected feature
outputs can be found in the batch integration embed and graph tasks.

-   **HVG conservation**: This metric computes the average percentage of overlapping
    highly variable genes per batch before and after integration.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="929" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **ARI**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Cell Cycle Score**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Graph connectivity**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **HVG conservation**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Isolated label F1**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Isolated label Silhouette**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **kBET**<sup><a href="/bibliography#bttner2018test" target="_blank">2</a></sup>: Missing 'metric_description'.

<!-- -->

-   **NMI**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **PC Regression**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Silhouette**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Batch ASW**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

## Results

<div id="htmlwidget-fb349618de6cdeca17a3" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-fb349618de6cdeca17a3">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">4<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">7<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">5<\/a><\/sup>"],["Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>"],[1.41421178157468,1.40534764637933,1.3674781971042,1.35006056485649,1.32673033848456,1.31368663249025,1.31357832914338,1.30343818144119,1.25103113225591,1.25099688761063,1.19433733264177,1.15095759735719,1.12842063263527,1.10711576012678,1.08607960630325,1.08260483212176,1.08077253846598,1.08067853056085,1.03788877144195,1.02422126445654,1.02418784991122,1.02065100638648,1.0163295274102,1.00146196204986,1.00002036466162,0.993609827995084,0.992696130088304,0.97377309158103,0.962334894519414,0.958678427213579,0.954492793847245,0.94182531540565,0.936985895824254,0.935981399671585,0.92822163020069,0.926723428467195,0.926370494542097,0.924940618628399,0.922354148757713,0.922352272666676,0.921722945456932,0.903165215194853,0.902989882663298,0.895319482567168,0.890368088426217,0.887696280841136,0.886326288840002,0.885737998880579,0.880712446361104,0.875197385744644,0.867787176914853,0.852870807868811,0.841034840268441,0.840993299600224,0.836646685561692,0.83147290975937,0.830293207517551,0.82452282686163,0.806584626994542,0.794575570616523,0.786276844074454,0.778075468934655,0.768199700441157,0.764682791327299,0.76189420018599,0.742562519734429,0.740880660299778,0.701965386911408,0.695623841059834,0.695507488234215,0.675072259062283,0.673102863846441],[4.2463505911219,4.2460509936583,4.16521791884088,3.80924767870689,3.78242957213683,4.17049037040938,4.2462040635536,4.25904675056472,3.9750039990404,3.97597707221163,3.35605373574333,4.04006778778548,2.95836544108674,2.9412850577805,2.68483081325473,3.26756247093181,2.49068400651612,2.42111050411484,2.98929042225431,2.56124319840053,2.34511079429542,2.50027342374645,2.48714789685523,2.09766453698209,2.5936896903196,2.58686166355852,2.56173546294993,1.59195424829097,2.31836900263586,2.10640167315651,2.52844114660669,2.18472825684316,2.31977239793454,2.31149357606954,2.20287037484091,2.07876277706533,2.43402490668394,2.09482537227511,2.24786056991712,1.89258038690894,2.24308691521785,1.13087605615135,2.04321060337559,1.31993236619752,2.37501615751616,1.04435948829399,2.29724167478895,2.1619244338172,1.24877273066792,2.07274039472517,1.10897303934222,1.21475175578631,1.64457252074612,1.64639732893669,2.19807826260644,1.11907011963366,1.03890314583373,1.86763579705146,1.05955095905317,0.925515256888596,1.36752054235931,1.21747434365146,1.19873927842616,1.46848990344613,1.14639140440954,1.06737818283605,1.08035602043801,1.06700632810399,1.21734488771155,1.06100004332241,1.12120730860306,1.10968422586702],[1.18162860060994,1.23107222766529,0.877920571469455,1.15559478164981,0.877916836558976,0.973044229035498,0.0626939536776979,0.919794810128592,0.450927855194204,0.45093881714331,1.04037686522911,0.836135529510763,0.0674817932121563,0.766974181346177,0.969109548387962,0.586490750196489,1.15854333201452,1.11196053705993,0.024706772069331,1.03526547473767,1.00057036375725,0.943568231455337,1.03527943190988,1.12087606132263,0.84784742340491,0.340265891873021,0.902102679314381,1.14706138842239,1.03262611533044,0.782235280601715,0.51164181187259,0.348762327257092,0.991400347867989,0.991397918357956,1.03143761200206,0.762348898177902,0.570144031496706,1.1438113774044,0.898384519048369,1.15047319439929,0.898370197020197,1.15019001802922,1.06703430928267,1.04978146653262,0.750368565133024,1.17177812433949,0.82915387065167,0.611356943060274,1.01917080160874,0.33176262061738,1.17971646577272,0.828408994093682,1.21447733576156,1.21452176290963,0.0667255299478932,0.983112209566723,0.879472272235356,0.690176227800762,0.547105545128522,0.633521635054544,1.2365235408127,0.904109938255976,1.23647550487556,0.345967525031245,0.530188599971344,0.467163376686531,0.387959690444659,0.359224146722535,0.724793938087546,0.440988445174498,1.02969297709217,1.02970540010482],[1.25060288376677,1.24977851376309,1.18636441511573,1.25109444559103,1.18206299457814,1.24644386472779,1.23853103337983,1.25095218943072,1.19325792564615,1.19186374211012,1.24858491972335,1.22377868165601,1.23676869941078,1.24921757768983,1.23675004088549,1.2484080791007,1.22598265378209,1.24593281351879,1.23172517584874,1.20327926470792,1.23990422817848,1.21815773565786,1.20087876264653,1.20979121782876,1.21716787300799,1.14643830540782,1.22636784162451,1.24752554151644,1.1889251045604,1.22666665126034,1.12789362543639,1.14449129852937,1.19333994266789,1.1917004749186,1.16491279783268,1.21846199543469,1.12961369563737,1.18712827891995,1.20168367438297,1.17419579752383,1.20095841371362,1.24021679865956,1.16737611105591,1.21577948451204,1.20978306970033,1.2065929362391,1.20816975343587,1.13655127579213,1.17454417358266,1.11072548514202,1.24679976678686,1.24330373588539,1.18498157507183,1.18523715938723,1.08305821018984,1.22526873843702,1.23860821971018,1.18694464948749,1.24185727153078,1.23960179614745,1.22887281844284,1.22448990670986,1.23013343634013,1.01327359137308,0.996547207734565,1.06881157074095,1.07117018720625,0.963900003785178,1.21862587795748,0.960215356194833,1.22795012165157,1.2246357404229],[0.0602988260405549,-0.702241195304162,-0.676093916755603,-0.276414087513341,-0.676093916755603,-0.183564567769477,-0.757875923712873,-0.788153681963714,-0.699039487726788,-0.69957310565635,0.0576307363927426,-0.406083244397012,-0.802174732711738,-0.778014941302028,-0.390267589150774,-0.794023479188901,0.0626443900485215,-0.131685042367127,-0.707577374599787,-0.38258815895963,0.098360655737705,-0.47339454203378,-0.383096894117131,0.0576914319092564,-0.109394703656999,-0.460686585383599,-0.0267494227059932,-0.266808964781217,-0.151639344262295,-0.462786998070161,-0.186633039092055,-0.47895271573245,-0.0977301387137453,-0.098045397225725,-0.176229508196721,-0.475853589929663,-0.176860025220681,0.093001261034048,-0.354921745658307,0.0863808322824716,-0.354509344300508,0.0346330830709616,-0.180643127364439,-0.081191605705107,-0.175329635529846,0.029062727052555,0.276481715006305,-0.173392181588903,0.209962168978562,-0.415316323363454,-0.217001695325745,-0.35916686849116,-0.0135561160151324,-0.0145018915510719,-0.594983991462113,-0.186728021312667,-0.455800435940906,0.186948297604035,-0.458706708646161,-0.45289416323565,-0.375151368370065,-0.173165415354807,-0.373940421409542,-0.38790902274009,-0.192622950819672,-0.448050375393558,-0.447323807217244,-0.364979413901671,-0.306853959796561,-0.376120125938484,-0.350690239767498,-0.350932429159603],[1.32629405388636,1.36763828072223,1.21539788990257,1.27559731351427,1.21289803897184,0.990700645051138,1.34789170781664,1.37119612712648,1.11151712318845,1.11133223747592,1.22070995700835,0.988362869493551,1.31551401032847,1.36032195329892,1.0816648640322,1.36148890162873,1.07315511183696,1.08529640116308,1.3279116950458,0.992882305209362,1.05056026551623,1.0970724558941,1.00245501865687,1.03594605903326,1.07681108861028,1.17027623896266,0.897424982218154,1.26981291535666,1.07111783981406,1.18209720436631,1.0851376821737,1.15512165931708,0.843717606870356,0.844831352818455,1.02205369617899,1.13518355882404,1.06354150511462,0.972954907285125,0.952407716060896,1.00084378732006,0.953082210327323,0.920216374339406,0.967881916054827,1.14722458193599,0.817841296740258,0.886284432771364,0.787124068012414,1.04075067468229,1.08584200732316,1.14953324053465,0.929731624458729,0.800545222764098,0.937238606313572,0.935076070289708,1.10792571098065,1.08601882312815,0.897967544376823,0.939225466024995,1.11485181998595,1.07617985878855,0.949635664180321,0.91445023359091,0.919531418855158,1.08737484202468,1.08981517531417,1.06471328544907,1.09939550395672,1.07993735187585,0.525935554702228,1.06438363977921,0.810814840417061,0.810490901479944],[1.58145621898583,2.15264991009201,1.26826366465688,1.83878967192086,1.26826663646538,1.20719904618938,2.56098247820657,1.40709177757815,1.00207563992163,1.00205173395769,1.18863637025898,0.770859002877142,2.0696597014173,1.66807689411949,1.24881721747255,1.25095640950242,0.972776287784597,1.15814179303408,2.03785963577242,0.678797295000701,0.945706781804232,1.03642195118458,0.678887523670344,0.926173596873904,0.796870468956888,1.43748885730249,0.657382702069368,1.44304230779139,0.696260047677354,1.08653125090048,1.0103746275628,1.38869375572095,0.693611688999004,0.69361333592606,0.801332900357263,0.964702114077629,0.847478348483385,0.665397607752949,0.545661778763322,0.76145834075322,0.545470786378298,0.671475036615018,0.771526211051269,0.997015013256537,0.510528527464042,0.828426079609514,0.467276687395651,0.797997661613514,0.918864291204591,1.26879776464173,0.689928925377135,0.796931273368763,0.641532387027727,0.641640344937822,1.53448564427667,0.629138440773627,0.90084117561833,0.512704641950067,0.895256810904589,0.871623721679197,0.0747825986195943,0.297672372623071,0.07451653134622,1.154081102452,0.982524072907172,1.08604693818276,0.90400574521752,0.970535996539246,0.248021937564916,0.945233590172146,-0.00670674260554374,-0.00719566781446208],[0.114556633252919,0.136992067342659,0.373771226454211,0.141268868790754,0.37174011274132,0.251251941668108,0.260751351819999,0.194326929494534,0.335568683616592,0.336524453196645,0.115078136354557,0.291205056757083,0.21581671083009,0.182227133767361,0.119560093570806,0.165789645954258,0.0635703669277414,0.114563875802961,0.192260504957502,0.261132749756934,0.146641985552641,0.102540267513074,0.260342151092477,0.0713569315077038,0.138059674290133,0.193397663030899,0.180244247472424,0.113974332562896,0.142012182659191,0.121991343419785,0.137450042979925,0.134098834520775,0.257205598625383,0.254775589029399,0.0518150050822713,0.0892861764960073,0.184355706619599,0.0222088029074904,0.272365552451232,0.04728057380445,0.272745217499905,0.0539456646228144,0.0667043883118414,0.0858534639430155,0.191222797472251,0.0517120843641043,0.0583142206680903,0.192186239489637,0.117657412514789,0.171411702441265,0.0557807730654893,0.083628539079625,0.327213927027397,0.327614300931636,0.148835826828008,0.0259286467513622,0.0614788679624151,0.0725268804021361,0.0417347138328026,0.0353644952219224,0.154510751506713,0.231166580081072,0.152421424191207,0.135178504314637,0.185561318964276,0.049029749752309,0.135085930653099,0.129788362876656,0.209936455257533,0.0711383671516262,0.152957903225415,0.155453041855726],[1.53091961749888,1.53947832429612,1.47360266276194,1.48085239373788,1.41696672286769,1.4931599527071,1.53435618928756,1.54660621889563,1.40358512351247,1.40336411866651,1.36542553150384,1.40839167138767,1.40014359742461,1.2577129902713,1.2709203380561,1.34928463856456,1.2368020714626,1.25555883731686,1.28723709585816,1.22802902622243,1.23204465713271,1.24736164096754,1.20928812684526,1.16261873084971,1.24111195682834,1.24837271362133,1.20334764690938,1.09038274693051,1.2218312701729,1.15979144363628,1.26997866732044,1.23063906007439,1.18456519339276,1.18503138797354,1.17762794905077,1.1468463634565,1.2169644334323,1.15749568459815,1.15110692625318,1.12694407005912,1.14830094340028,1.02199091229077,1.10832291234362,1.06443077226122,1.1426920806672,0.99548659098618,1.14100876253937,1.13088447683509,1.0511937228329,1.12622575570429,1.05377946107998,1.03217073304384,1.04095395186501,1.04124822900566,1.18285979921258,1.05171584702026,1.01785075495623,1.0681526465164,0.999830070464647,0.982931539461319,1.02586626969454,0.975874225481677,1.02591922251258,1.08814199307009,1.04991767051487,1.0217949154781,0.993797518144137,0.960555694419606,0.951531924097535,1.03164850948281,1.00870843108735,1.00036375482335],[1.00087024199831,0.841665785463052,0.700785731821243,0.671088408126597,0.700810871187828,0.999282422111672,0.739602772560841,1.0009136126271,0.865011019839992,0.865028382913102,1.00088614793893,1.00067096912999,0.5298263585811,0.949321549066908,0.872136523944118,1.0009136126271,1.0006323565061,0.689240967485291,0.704600599154217,0.671071098809233,0.864968493860892,1.000664637869,0.671072912163939,1.00061161506581,0.924927007848704,0.75113046608137,0.998975609374905,0.722511815118648,0.953731007481375,0.940983073347715,0.800381572029005,0.544068102631941,0.860177030138464,0.860174448352152,1.0003279497291,1.00066463786759,0.900559287732657,1.00031963797116,0.771409352112962,1.00029653868001,0.771402131253104,1.00070718954884,1.0003279497291,0.725354708821336,1.00018265737173,1.0006521585785,0.997319669976541,0.917268819099382,0.857032807164006,0.748681733607026,0.531666000468385,0.849816778520597,0.81139276414471,0.811380379993204,0.277553962729856,0.596519504181354,1.0007523512508,0.999305332559468,0.919896663494862,1.00075235124658,0.452233416951838,1.0003247360365,0.452250534467992,0.386247820929438,0.630813167265507,0.301996377285718,0.613229337950611,0.624175782567479,1.00057167042574,0.250376332792953,0.637819293432581,0.63780260977461],[2.25091368251835,2.33530224746123,4.1686276532236,2.44387284888444,4.16863135161524,2.43391924418025,2.97065819351444,2.33512534106105,3.7074141759968,3.70746985733762,1.61139006001771,1.63186271241481,2.78580620982558,1.61772386390289,1.80318060478775,1.62789865297385,1.68234835052225,1.91728948991086,1.74153060609139,2.50067144018798,1.5640335396427,1.76000616096768,2.50069706370336,1.43697346732023,1.48070589975531,2.0428069060397,1.56748453856313,1.71107085799912,1.36090794402747,1.42052669390951,1.77479992638751,2.10119166308677,1.58099082952896,1.58099770414769,1.3692304038124,1.43894902442869,1.59683690295336,1.27146243416732,1.92479455654948,1.36121135416665,1.92478855178689,1.52466893488108,1.36175846567779,1.54166810004734,1.1970820209183,1.33831898777632,1.22092077793649,1.46684095241277,1.40969873528257,1.47970200261791,1.74396208120545,1.5935336671467,0.975680341042883,0.975652688082134,1.61390743192828,1.50423470686031,1.57566273802957,1.04240751465346,1.28294827379817,1.32718995463443,1.75246213534715,1.04761359357264,1.75239583781138,1.40662821024385,1.30866412447386,1.74296885304723,1.56092562165131,1.23073444934957,0.916975835686613,1.29731307432942,1.09126112422869,1.09127113832097],[1.01243824764163,1.0604369550128,0.288402350655271,1.05967389001217,0.288404502962562,0.868625809081944,0.245565800472837,0.840919920909857,0.416020396585155,0.41598845436076,0.932938198888579,0.875282534313576,0.635419169582938,0.963427101453264,1.05017321409486,0.843883471048396,0.921358995724231,1.02005365912983,0.587231353409332,0.516650214948785,0.778164583545164,0.794489107029414,0.516672808085456,0.89637793385512,0.792427631912692,0.473355987451708,0.751341143181154,0.640976818183512,0.751542669616795,0.981025082820893,0.439954669042698,0.607236227213068,0.479794356755192,0.479825006019767,0.565058751517853,0.834605757240435,0.423416647029811,0.565741440596693,0.53514273645361,0.544210123435397,0.535256377729298,1.18589729893437,0.559388969778095,0.782665956436342,0.774661435234945,1.21198547924138,0.466577976828674,0.460748692472983,0.595098058812245,0.582906866523118,1.22232250383216,1.29765505535908,0.486895949967165,0.486659922679816,0.584667153940511,1.11192299231327,0.977488648660532,0.503723641427659,1.22810547739262,1.10054483089481,0.781788915274039,0.918819643632843,0.781753937435891,0.714036234455241,0.653036411310266,0.74633484301357,0.751085514852476,0.700740553687039,0.9449781299636,0.904405138114945,0.702779832320254,0.702852786635575],[1899,2701,2249,2572,2269,3171,2481,2192,1749,1809,2192,14028,2339,21511,2458.33333333333,2552,2136,2752.33333333333,3249,2273.33333333333,2922,2167.33333333333,2297.33333333333,1775,2733,2708,2851.33333333333,2640,16180,18413.3333333333,2350,2374.33333333333,2262,2241,2130,2098,2582,2180,1982.33333333333,1632,1880.66666666667,2329,1811,7610,12620.3333333333,1501,2682,2990,15420,3999.66666666667,2763,1941,1993,1967,2350,4770,2180,9755,17549,1931,2382,2701,2309,3427,5201,2434,3061,5760,14078,2730,2171,1900],[164.4,488.2,145,591.3,134.3,1049.4,415.8,330.8,123.3,249.3,213.7,2469.9,477.6,1433.3,1175.1,259.7,240.233333333333,1116.26666666667,1150.2,186.033333333333,1223.7,306.8,170.9,692.7,1603.4,440.966666666667,1286.46666666667,2561.4,3640.5,2844.63333333333,572.3,452.133333333333,228.9,222.3,427,641.233333333333,313.4,333.1,221.466666666667,857,176.733333333333,223.2,1036.7,3150.46666666667,2480.56666666667,1007.4,1410.8,512.7,2358.7,991.3,1533.8,1433.7,180.9,217.1,1429.4,4531.3,162.6,2527.9,3460.1,627.3,156.1,1399.2,184.2,1645.26666666667,1767.9,306.5,593.7,1311,2443.9,1738.5,198,226],[3.125,33.30078125,5.17578125,92.578125,5.2734375,19.43359375,5.2734375,3.7109375,17.28515625,21.97265625,13.4765625,28.80859375,4.58984375,489.94140625,48.9583333333333,15.4296875,4.23177083333333,66.30859375,30.078125,7.03124999967448,19.62890625,4.98046875,7.48697916666667,17.0572916666667,25.9765625,6.90104166666667,20.5729166666667,187.3046875,584.47265625,593.45703125,7.421875,5.76171875,7.91015625,8.88671875,5.37109375,21.4192708333333,7.8125,4.6875,29.3619791666667,17.1875,22.9166666666667,4.8828125,23.046875,332.161458333333,26.3346354166667,20.5078125,18.45703125,41.796875,361.71875,36.71875,86.71875,87.59765625,23.4375,28.61328125,27.05078125,447.4609375,5.859375,24.0234375,705.95703125,25.78125,8.30078125,23.828125,8.00781249902344,23.7630208333333,18.9453125,5.2734375,7.6171875,38.28125,26.171875,25.29296875,37.5,28.02734375]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>ARI<\/th>\n      <th>Cell Cycle Score<\/th>\n      <th>Graph connectivity<\/th>\n      <th>HVG conservation<\/th>\n      <th>Isolated label F1<\/th>\n      <th>Isolated label Silhouette<\/th>\n      <th>kBET<\/th>\n      <th>NMI<\/th>\n      <th>PC Regression<\/th>\n      <th>Silhouette<\/th>\n      <th>Batch ASW<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":15,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":14,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":16,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":9,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":10,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":11,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":12,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":13,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render","options.columnDefs.7.render","options.columnDefs.8.render","options.columnDefs.9.render","options.columnDefs.10.render","options.columnDefs.11.render","options.columnDefs.12.render","options.columnDefs.13.render","options.columnDefs.14.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **Random Integration by Batch**<sup><a href="/bibliography#openproblems" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Random Integration by Celltype**<sup><a href="/bibliography#openproblems" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Combat (full/scaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (full/unscaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (hvg/scaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (hvg/unscaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **FastMNN feature (full/scaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN feature (full/unscaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN feature (hvg/scaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN feature (hvg/unscaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **MNN (full/scaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (full/unscaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (hvg/scaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (hvg/unscaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **No Integration**<sup><a href="/bibliography#openproblems" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Random Integration**<sup><a href="/bibliography#openproblems" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **SCALEX (full)**<sup><a href="/bibliography#xiong2021online" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/jsxlei/SCALEX).

<!-- -->

-   **SCALEX (hvg)**<sup><a href="/bibliography#xiong2021online" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/jsxlei/SCALEX).

<!-- -->

-   **Scanorama gene output (full/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (full/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (hvg/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (hvg/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

</details>
<details>
<summary>
Baseline methods
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
Datasets
</summary>

-   **Immune (by batch)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Lung (Viera Braga et al.)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'dataset_description'.

<!-- -->

-   **Pancreas (by batch)**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'dataset_description'.

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
"> 1.000000 </td>
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
"> 1.000000 </td>
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
"> 1.000000 </td>
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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_scaled
  Metric id: ari
  Best score: 4.259046750564723%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_scaled
  Metric id: ari
  Best score: 4.259046750564723%
"> Best score combat_hvg_scaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_scaled
  Metric id: ari
  Best score: 4.259046750564723%
"> 4.259047 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_scaled
  Metric id: ari
  Best score: 4.259046750564723%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_scaled
  Metric id: ari
  Best score: 4.259046750564723%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_unscaled
  Metric id: ari
  Best score: 4.2463505911218995%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_unscaled
  Metric id: ari
  Best score: 4.2463505911218995%
"> Best score combat_hvg_unscaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_unscaled
  Metric id: ari
  Best score: 4.2463505911218995%
"> 4.246351 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_unscaled
  Metric id: ari
  Best score: 4.2463505911218995%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_hvg_unscaled
  Metric id: ari
  Best score: 4.2463505911218995%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_scaled
  Metric id: ari
  Best score: 4.2462040635536%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_scaled
  Metric id: ari
  Best score: 4.2462040635536%
"> Best score scanorama_feature_hvg_scaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_scaled
  Metric id: ari
  Best score: 4.2462040635536%
"> 4.246204 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_scaled
  Metric id: ari
  Best score: 4.2462040635536%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_scaled
  Metric id: ari
  Best score: 4.2462040635536%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_scaled
  Metric id: ari
  Best score: 4.246050993658297%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_scaled
  Metric id: ari
  Best score: 4.246050993658297%
"> Best score mnn_hvg_scaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_scaled
  Metric id: ari
  Best score: 4.246050993658297%
"> 4.246051 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_scaled
  Metric id: ari
  Best score: 4.246050993658297%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_scaled
  Metric id: ari
  Best score: 4.246050993658297%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_hvg performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_hvg
  Metric id: ari
  Best score: 4.170490370409384%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_hvg performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_hvg
  Metric id: ari
  Best score: 4.170490370409384%
"> Best score scalex_hvg ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_hvg performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_hvg
  Metric id: ari
  Best score: 4.170490370409384%
"> 4.170490 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_hvg performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_hvg
  Metric id: ari
  Best score: 4.170490370409384%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_hvg performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_hvg
  Metric id: ari
  Best score: 4.170490370409384%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_unscaled
  Metric id: ari
  Best score: 4.1652179188408756%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_unscaled
  Metric id: ari
  Best score: 4.1652179188408756%
"> Best score fastmnn_feature_hvg_unscaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_unscaled
  Metric id: ari
  Best score: 4.1652179188408756%
"> 4.165218 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_unscaled
  Metric id: ari
  Best score: 4.1652179188408756%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_unscaled
  Metric id: ari
  Best score: 4.1652179188408756%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_full performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_full
  Metric id: ari
  Best score: 4.040067787785484%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_full performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_full
  Metric id: ari
  Best score: 4.040067787785484%
"> Best score scalex_full ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_full performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_full
  Metric id: ari
  Best score: 4.040067787785484%
"> 4.040068 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_full performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_full
  Metric id: ari
  Best score: 4.040067787785484%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scalex_full performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scalex_full
  Metric id: ari
  Best score: 4.040067787785484%
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_scaled
  Metric id: ari
  Best score: 3.975977072211627%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_scaled
  Metric id: ari
  Best score: 3.975977072211627%
"> Best score fastmnn_feature_full_scaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_scaled
  Metric id: ari
  Best score: 3.975977072211627%
"> 3.975977 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_scaled
  Metric id: ari
  Best score: 3.975977072211627%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_scaled
  Metric id: ari
  Best score: 3.975977072211627%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_unscaled
  Metric id: ari
  Best score: 3.9750039990404034%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_unscaled
  Metric id: ari
  Best score: 3.9750039990404034%
"> Best score fastmnn_feature_full_unscaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_unscaled
  Metric id: ari
  Best score: 3.9750039990404034%
"> 3.975004 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_unscaled
  Metric id: ari
  Best score: 3.9750039990404034%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_full_unscaled
  Metric id: ari
  Best score: 3.9750039990404034%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_unscaled
  Metric id: ari
  Best score: 3.809247678706888%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_unscaled
  Metric id: ari
  Best score: 3.809247678706888%
"> Best score mnn_hvg_unscaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_unscaled
  Metric id: ari
  Best score: 3.809247678706888%
"> 3.809248 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_unscaled
  Metric id: ari
  Best score: 3.809247678706888%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_hvg_unscaled
  Metric id: ari
  Best score: 3.809247678706888%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_scaled
  Metric id: ari
  Best score: 3.7824295721368313%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_scaled
  Metric id: ari
  Best score: 3.7824295721368313%
"> Best score fastmnn_feature_hvg_scaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_scaled
  Metric id: ari
  Best score: 3.7824295721368313%
"> 3.782430 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_scaled
  Metric id: ari
  Best score: 3.7824295721368313%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method fastmnn_feature_hvg_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: fastmnn_feature_hvg_scaled
  Metric id: ari
  Best score: 3.7824295721368313%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_unscaled
  Metric id: ari
  Best score: 3.356053735743325%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_unscaled
  Metric id: ari
  Best score: 3.356053735743325%
"> Best score combat_full_unscaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_unscaled
  Metric id: ari
  Best score: 3.356053735743325%
"> 3.356054 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_unscaled
  Metric id: ari
  Best score: 3.356053735743325%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_unscaled
  Metric id: ari
  Best score: 3.356053735743325%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_scaled
  Metric id: ari
  Best score: 3.2675624709318094%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_scaled
  Metric id: ari
  Best score: 3.2675624709318094%
"> Best score combat_full_scaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_scaled
  Metric id: ari
  Best score: 3.2675624709318094%
"> 3.267562 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_scaled
  Metric id: ari
  Best score: 3.2675624709318094%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: combat_full_scaled
  Metric id: ari
  Best score: 3.2675624709318094%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_scaled
  Metric id: ari
  Best score: 2.9892904222543057%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_scaled
  Metric id: ari
  Best score: 2.9892904222543057%
"> Best score scanorama_feature_full_scaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_scaled
  Metric id: ari
  Best score: 2.9892904222543057%
"> 2.989290 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_scaled
  Metric id: ari
  Best score: 2.9892904222543057%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_scaled
  Metric id: ari
  Best score: 2.9892904222543057%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_unscaled
  Metric id: ari
  Best score: 2.9583654410867406%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_unscaled
  Metric id: ari
  Best score: 2.9583654410867406%
"> Best score scanorama_feature_hvg_unscaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_unscaled
  Metric id: ari
  Best score: 2.9583654410867406%
"> 2.958365 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_unscaled
  Metric id: ari
  Best score: 2.9583654410867406%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_hvg_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_hvg_unscaled
  Metric id: ari
  Best score: 2.9583654410867406%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_full_scaled
  Metric id: ari
  Best score: 2.9412850577804988%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_full_scaled
  Metric id: ari
  Best score: 2.9412850577804988%
"> Best score mnn_full_scaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_full_scaled
  Metric id: ari
  Best score: 2.9412850577804988%
"> 2.941285 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_full_scaled
  Metric id: ari
  Best score: 2.9412850577804988%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method mnn_full_scaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: mnn_full_scaled
  Metric id: ari
  Best score: 2.9412850577804988%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_unscaled
  Metric id: ari
  Best score: 2.1980782626064426%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_unscaled
  Metric id: ari
  Best score: 2.1980782626064426%
"> Best score scanorama_feature_full_unscaled ari </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_unscaled
  Metric id: ari
  Best score: 2.1980782626064426%
"> 2.198078 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_unscaled
  Metric id: ari
  Best score: 2.1980782626064426%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method scanorama_feature_full_unscaled performs a lot better than baselines.
  Task id: batch_integration_feature
  Method id: scanorama_feature_full_unscaled
  Metric id: ari
  Best score: 2.1980782626064426%
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
