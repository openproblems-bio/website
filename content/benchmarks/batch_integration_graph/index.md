---
title: "Batch integration graph"
summary: "Removing batch effects while preserving biological variation (graph output)"
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
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="718" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **ARI**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Graph connectivity**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Isolated label F1**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **NMI**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

## Results

<div id="htmlwidget-a844844cc219733af4e3" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-a844844cc219733af4e3">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons","Responsive"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">5<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">5<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">5<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">5<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">7<\/a><\/sup>","BBKNN (hvg/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">5<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">5<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","BBKNN (hvg/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">7<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">7<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","BBKNN (hvg/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (hvg/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">7<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">2<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">7<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">7<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (full/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">4<\/a><\/sup>","BBKNN (full/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (hvg/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (hvg/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","BBKNN (full/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (full/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (full/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (full/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">9<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>"],["Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>"],[1.36569316232259,1.24062795823097,1.13099894217589,1.05747542192162,1.00684577368041,0.966275020835187,0.927302296099098,0.921207500507708,0.896445900331948,0.89094619539528,0.882686332487932,0.882558677910522,0.881631870953188,0.879347245321213,0.877879475143631,0.876788999515086,0.874276141490117,0.871540985523525,0.870701053349309,0.8697363483531,0.869261297577819,0.868980805615312,0.865865950492303,0.862771934902808,0.862248590310478,0.861109895826895,0.860976286905069,0.860523293136528,0.858780473068164,0.857911204951248,0.857239546337379,0.856282572227798,0.855628589995399,0.855064901605962,0.851349330143761,0.850104952916697,0.850015587705194,0.849674288031123,0.849332988357053,0.844719967579088,0.84433607824441,0.842298700882146,0.842056241398668,0.840549046382578,0.840426703870433,0.838967652233703,0.833677484548469,0.83127359625851,0.829673347803385,0.828387316863234,0.825469502769756,0.825033121431923,0.821186825423649,0.81165098700239,0.804064408225779,0.801551099494484,0.799159952774306,0.794796202023047,0.793364288736034,0.789089955958776,0.788645642257461,0.787890976687229,0.787176796575659,0.786995583501585,0.780626878267137,0.777753391511754,0.773392845231987,0.773063589129838,0.769514956603502,0.767860744702748,0.764583824042931,0.761422981182621,0.76079266476077,0.753983827304203,0.749257681520654,0.747866356972109,0.746236108716278,0.745422498861149,0.745412884320533,0.744605860460447,0.730909249522629,0.72940927862762,0.717553303439461,0.717350429008609,0.714320380285872,0.712107048528837,0.711843925681063,0.709069370290294,0.701025834284488,0.695295103779191,0.691774764216021,0.690327455742128,0.689693722558389,0.68939306348549,0.686737313159771,0.685770434670408,0.68250995125859,0.680480552407417,0.678282589357408,0.678125994786153,0.675806080122048,0.675535670883178,0.671140090353086,0.670927580568011,0.669015887910913,0.665975820553596,0.664056936528813,0.662219096758605,0.656353352354926,0.655776237987165,0.654172894758623,0.651471088699775,0.646257011605805,0.633210810415878,0.627465596142449,0.585858709461208,0.559473648917409,0.533637466127843,0.439809336113237,0.401596868826209],[0.8283457068501,0.494660631505984,0.859223492465221,0.78088255580657,0.599258403984712,0.795337084083983,0.942758231761206,0.928385430972857,0.887388399398787,0.957223652176734,0.879163776712367,0.943941559755086,0.836564864034615,0.917988032904411,0.948665530922417,0.945914273275857,0.911976536605353,0.879707828054673,0.939890450099281,0.943442593537647,0.949120678024812,0.903745731602815,0.94478929649834,0.867604584933321,0.948587666410036,0.870416599812074,0.951442301947687,0.81547409635426,0.948441207231594,0.930590984410314,0.80115356863328,0.786088491841831,0.840340242760638,0.867143887803888,0.785846568376182,0.862065553708889,0.73970609977028,0.792584170644871,0.845462241519461,0.919417985416924,0.916972813002758,0.793540123007464,0.744744297096372,0.79628769287091,0.847599126756168,0.807620769867296,0.871234558187365,0.783609547447413,0.832043830049508,0.934848346507434,0.752235142981182,0.849871004777589,0.813739938910584,0.788256926213015,0.749283980236479,0.731450675702744,0.797900800159266,0.716963842027683,0.857531173758942,0.748299707607491,0.724197209999734,0.750361678301492,0.659548905505354,0.7777818294147,0.698032485070457,0.776066484717766,0.723734146218354,0.703856176463439,0.699629510647257,0.698858685674029,0.691053207896073,0.763304352599756,0.604725478272549,0.678828787315773,0.733419404763039,0.513403480526453,0.545681695088613,0.627848321503613,0.549178147589022,0.577959909650772,0.762660118348735,0.794723729426933,0.49725038460237,0.695326157721176,0.7620084092737,0.743271744369651,0.743967153809292,0.5626035191674,0.920594758424922,0.494017315533965,0.82744771694036,0.587247512282441,0.445322621615719,0.917383722437111,0.493017573639517,0.608690375897885,0.684744492457684,0.572762012175844,0.876471411275851,0.607190719782589,0.719064760184797,0.685356609998085,0.709547255905937,0.839085780552373,0.700447414012976,0.714985047841738,0.832963610651327,0.520745797932483,0.787684803065273,0.876695904462205,0.788304796971328,0.857208083507631,0.573447111085592,0.856490992644475,0.506774155055362,0.457531182537199,0.535425099317265,0.440166420481865,0.373558685908368,0.375524040913355],[0.964268534806334,0.904842331240864,0.962620126939614,0.935898313005227,0.940085893880004,0.926720759077131,0.982967081016334,0.976737439137842,0.986685208822471,0.977040041036384,0.983911457652736,0.988250340590571,0.982005453559394,0.986582738888364,0.980283927553498,0.975596010202819,0.98035367306953,0.985943637900849,0.957283848561294,0.973912759827919,0.983217824522069,0.974636222554089,0.976795888486324,0.978454894169727,0.986480268954258,0.936992223743636,0.977628614010701,0.983636935211126,0.980403872998223,0.976955402629009,0.956094489522379,0.973691963817385,0.966288478859092,0.976356336093808,0.972308799189392,0.977779729322989,0.990730936221554,0.983498088272203,0.976265240322852,0.986448817056626,0.930979993316699,0.978604056016969,0.987273467980945,0.971562293888541,0.954823975474921,0.929266076169319,0.947615640838733,0.896944406450888,0.959435623311655,0.965965205508146,0.976836108917991,0.956153334245255,0.954916599976442,0.963864271690944,0.934051940747024,0.890821391214648,0.942815825745255,0.960069403973987,0.912732072691392,0.934678054479809,0.961587398062016,0.955025679746461,0.929221898028424,0.92611280880416,0.939493544916929,0.982292883751428,0.935196977398795,0.975329456519145,0.955401658088034,0.955235868813641,0.955286487156066,0.983954703324187,0.955346566101366,0.95465165817381,0.90752809120412,0.922578828389185,0.925679916339235,0.94744461582839,0.956655651756801,0.928781004289284,0.910531726422432,0.929601334908152,0.862417326118151,0.866123993810783,0.929517101464785,0.928736265025087,0.928220190806254,0.934291432076523,0.865716886743497,0.945937682558505,0.957071664972827,0.93087783008439,0.7681790004795,0.942891307966401,0.945990097631068,0.990673007674936,0.921048054628288,0.933498619767931,0.896106011625509,0.981460589591747,0.966413659260729,0.91967779483167,0.902455285919832,0.904176990069843,0.964360368081772,0.913443004253795,0.903747715773503,0.989936010555057,0.902236661236532,0.893417907104834,0.901038723524475,0.893387388739659,0.971649071190717,0.870619139763141,0.873241396181448,0.901686256194793,0.730021245414701,0.725818722690534,0.578396049199619,0.59391849701862],[2.85492227979275,3.06470515667407,1.82154736774771,1.73202663494496,1.86553689245769,1.31266810596599,0.869754685600972,0.896948762233736,0.853538788449102,0.702646046750781,0.827788657669839,0.690846286701209,0.869390380515098,0.72388726987222,0.668280322226845,0.673797368688408,0.729797586367063,0.765811473891047,0.685078493542649,0.668280322226845,0.626883449466976,0.727360504807365,0.631806515064287,0.734270489420274,0.594235751295337,0.759345911147058,0.598714385387,0.840776661080884,0.589815661440166,0.626883449466976,0.838453958496983,0.841657529373572,0.753682407290394,0.710830848643489,0.831846035846811,0.715328177336145,0.854310705560498,0.77847837615564,0.702646046750781,0.607852001251869,0.657484375194145,0.803772905205313,0.841831998796459,0.759785259773707,0.707655944940822,0.817372987135087,0.668233605446262,0.816045775543334,0.690593383582159,0.519094223757436,0.76588811225702,0.652376405576114,0.704200295615318,0.667250977979973,0.741514521193236,0.803788844184275,0.661728405760835,0.72414443071767,0.598714385387,0.706038425765228,0.696108273621669,0.653534292489331,0.807153231392994,0.668857049876776,0.738999714366552,0.53946711827563,0.681040086423271,0.666368628241316,0.653551947158786,0.648459119813302,0.65648677485941,0.518212968510933,0.749522291711086,0.665972436327524,0.609130990097179,0.848044492035204,0.778363284944133,0.666221633733101,0.714811690832898,0.708682077853062,0.450819151764718,0.379401218008086,0.777893438754624,0.565311167319859,0.371619799396433,0.380589881141012,0.378934649048213,0.69428757062344,0.15211601181835,0.675585876079918,0.220296149547902,0.586441193863527,0.84097518667635,0.0422589921747248,0.642565832918386,0.410653914324416,0.380569938553061,0.564643073298675,0.118574044187737,0.428573935769996,0.247372726820187,0.353037546593483,0.350003675629551,0.105268143526841,0.301228730697424,0.309603940151767,0.0867528239334564,0.452486461465648,0.112720642468722,0.0304892171070481,0.10431735093764,0.05456480700486,0.382161311846946,0.00571978063566116,0.470230602127751,0.448737957009385,0.417052301550608,0.47116802697387,0.472105451819989,0.268793435781358],[0.815236127841178,0.498303713502972,0.880604781551012,0.781094183929728,0.622501904399213,0.83037413421364,0.913729186017879,0.882758369686396,0.858171204657431,0.926875041617218,0.839881437916785,0.907196524595222,0.838566785703646,0.888930939619855,0.914288119871766,0.911848345893262,0.874976769918523,0.854701002247533,0.900551421194012,0.89330971781999,0.917823238297418,0.870180763496977,0.91007210192026,0.870757771087912,0.919690674582279,0.877684848604812,0.916119846274891,0.802205479899843,0.916461150602674,0.897214983298691,0.833256168696873,0.823692303878406,0.862203231071474,0.865928533882665,0.815395917162656,0.845246351298764,0.815314609268444,0.844136517051781,0.872958424835117,0.865161066590933,0.871907131464035,0.793277719298837,0.794375201720897,0.834560938997153,0.851627768309819,0.801610775763109,0.847626133721515,0.828494655592405,0.836620554270219,0.893641491679922,0.806918646922832,0.841731741128734,0.811890467192252,0.827231772125629,0.791407190726376,0.780143486876267,0.79419477943187,0.77800713137285,0.804479523106803,0.767343635982578,0.772689687346425,0.792642256211633,0.752783151375866,0.775230645910706,0.745981768714609,0.813187079302193,0.753600170887527,0.746700095295454,0.769476710519934,0.768889304510019,0.755508826260174,0.780219900295606,0.733576322958079,0.716482427399704,0.746952240018278,0.707438626937595,0.735219538493132,0.740175424379493,0.761006047103412,0.76300045004867,0.79962600155463,0.813910832167309,0.7326520642827,0.742640397182618,0.794136211008569,0.795830303579598,0.796253709060492,0.645094959293811,0.865675680151181,0.665639540944374,0.762283525402995,0.656743286738152,0.704298081461987,0.855038231363725,0.665375748450114,0.733064440784396,0.743677319395326,0.65101850438722,0.821978890340538,0.69527873400028,0.770373174222478,0.744070732109473,0.722554143957024,0.835179408122986,0.710027038851479,0.725871289967085,0.832763595756964,0.685708117081231,0.822771302649176,0.822501923274573,0.823030707601051,0.800724075546951,0.657770552299963,0.800013328620237,0.659616231205233,0.535479442103454,0.555395949387061,0.497396694365102,0.335177157524971,0.368151501591504],[1938,1350,1318,2363.5,1194.5,1533.5,970,1215,6748,1149,24939,33769,4222.5,8408,810,1149,28969.5,28084.5,5994,800,1178,1916,33000,1458.5,10068,1339.5,1917,22400,1709,23574,990,1739,12530,2869,4029,29321,3469,2574,1679,790,2017,35068,7230,11944.5,925,1943,1605.5,1530,14778.5,1268,11359,2423,2502,915,701,1749,2463,36100,1712,2929,23563,910,1010,7210.5,12709,835,3088,1039,1070,859,1029,800,20118,2909,2789,5869,8794.5,1020,11599,11720,13476.5,865,11099.5,15748,859.5,829,1014.5,639,6835,1370,870,25350,10600,980,1060,870,1030,931,1000,810,985.5,1299.5,747.5,820,905,980.5,690,991,799,1229,959,1030,940,856,28047,14600,9673,31158,34269,3598],[936.1,153.8,206,1329.1,177.35,274.3,149.6,916.2,1333.3,191.3,2698.2,1812.1,1000.35,1833.5,170.5,137.3,2434.05,1961,698,123.7,185.8,481.3,2169.9,291.7,2333.7,262.5,785.2,2109.9,292.2,1578.2,162.9,397.6,2527.2,787.95,1283.7,1845.35,2331.2,1311.35,291.5,135.2,1226.2,2112.5,1084.5,2429,240.9,350,370.2,333.7,1087.7,390.4,2330.8,955.45,819.25,178.15,344.5,342.6,1349.35,3591,911.4,1125.7,1477.4,75.9,176.2,1166.85,1422.3,118.45,1157.2,200.9,133.3,74.4,116,171.1,2441.1,1472.5,1722.1,2044,1622.05,185.8,1329,1200.1,1848.95,66,1469.1,103.1,120.3,64.1,111.1,372.5,1256.8,86.3,162,2830.65,1609.2,131.9,82.3,113.2,75.6,132.6,68.9,207,175.4,81.35,242.4,56.1,140.35,122.85,124.6,218.9,53.8,76.4,88.9,113.1,118.7,112.3,100.5,2070.3,102.95,100.4,100.3,102.8],[7.32421875,15.52734375,4.78515625,8.0078125,17.578125,6.103515625,3.61328125,30.37109375,4.19921875,4.78515625,5.6640625,5.76171875,34.27734375,5.224609375,3.22265625,13.57421875,5.712890625,8.88671875,19.53125,1.953125,4.78515625,2.34375,5.76171875,6.8359375,6.25,6.201171875,2.05078125,12.01171875,35.3515625,3.7109375,4.58984375,8.88671875,324.8046875,93.310546875,151.26953125,3.515625,94.140625,78.076171875,62.01171875,2.34375,2.44140625,3.3203125,38.18359375,345.1171875,15.380859375,8.7890625,6.8359375,7.6171875,18.9453125,4.8828125,365.4296875,2.099609375,2.63671875,3.955078125,17.1875,7.421875,2.392578125,584.375,30.37109375,2.1484375,18.359375,4.1015625,5.56640625,34.27734375,38.18359375,2.001953125,2.9296875,19.62890625,8.88671875,3.3203125,7.91015625,2.63671875,22.94921875,2.34375,8.69140625,17.7734375,22.021484375,4.6875,26.26953125,26.26953125,22.94921875,3.61328125,22.021484375,4.78515625,6.54296875,3.173828125,7.080078125,23.046875,22.94921875,12.59765625,7.32421875,539.404296875,17.7734375,2.83203125,6.93359375,2.05078125,6.689453125,29.58984375,6.4453125,2.9296875,2.83203125,11.962890625,20.41015625,3.125,8.0078125,26.5625,5.17578125,2.83203125,3.02734375,11.328125,5.2734375,23.53515625,8.69140625,17.7734375,15.13671875,494.43359375,4.19921875,14.208984375,13.28125,3.61328125]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>ARI<\/th>\n      <th>Graph connectivity<\/th>\n      <th>Isolated label F1<\/th>\n      <th>NMI<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":9,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8,9]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8,9]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filters"}},"order":[],"autoWidth":false,"orderClasses":false,"responsive":true}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render","options.columnDefs.7.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **Random Integration by Batch**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **BBKNN (full/scaled)**<sup><a href="/bibliography#polanski2020bbknn" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/Teichlab/bbknn).

<!-- -->

-   **BBKNN (full/unscaled)**<sup><a href="/bibliography#polanski2020bbknn" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/Teichlab/bbknn).

<!-- -->

-   **BBKNN (hvg/scaled)**<sup><a href="/bibliography#polanski2020bbknn" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/Teichlab/bbknn).

<!-- -->

-   **BBKNN (hvg/unscaled)**<sup><a href="/bibliography#polanski2020bbknn" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/Teichlab/bbknn).

<!-- -->

-   **Random Graph by Celltype**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Random Integration by Celltype**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Combat (full/scaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (full/unscaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (hvg/scaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (hvg/unscaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **FastMNN embed (full/scaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN embed (full/unscaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN embed (hvg/scaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN embed (hvg/unscaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN feature (full/scaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN feature (full/unscaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN feature (hvg/scaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN feature (hvg/unscaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **Harmony (full/scaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (full/unscaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (hvg/scaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (hvg/unscaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Liger (full/unscaled)**<sup><a href="/bibliography#welch2019single" target="_blank">11</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/welch-lab/liger).

<!-- -->

-   **Liger (hvg/unscaled)**<sup><a href="/bibliography#welch2019single" target="_blank">11</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/welch-lab/liger).

<!-- -->

-   **MNN (full/scaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (full/unscaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (hvg/scaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (hvg/unscaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **No Integration**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Random Integration**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **SCALEX (full)**<sup><a href="/bibliography#xiong2021online" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/jsxlei/SCALEX).

<!-- -->

-   **SCALEX (hvg)**<sup><a href="/bibliography#xiong2021online" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/jsxlei/SCALEX).

<!-- -->

-   **Scanorama (full/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (full/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (hvg/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (hvg/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (full/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (full/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (hvg/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (hvg/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **scANVI (full/unscaled)**<sup><a href="/bibliography#xu2021probabilistic" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scANVI (hvg/unscaled)**<sup><a href="/bibliography#xu2021probabilistic" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scVI (full/unscaled)**<sup><a href="/bibliography#lopez2018deep" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scVI (hvg/unscaled)**<sup><a href="/bibliography#lopez2018deep" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

</details>
<details>
<summary>
Baseline methods
</summary>

-   **Random Integration by Batch**: Missing 'method_description'.

<!-- -->

-   **Random Graph by Celltype**: Missing 'method_description'.

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
  Task id: batch_integration_graph
  Field: dataset_description
"> Dataset info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_graph
  Field: dataset_description
"> Pct 'dataset_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_graph
  Field: dataset_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_graph
  Field: dataset_description
"> percent_missing(dataset_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Dataset metadata field 'dataset_description' should be defined
  Task id: batch_integration_graph
  Field: dataset_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_graph
  Field: method_description
"> Method info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_graph
  Field: method_description
"> Pct 'method_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_graph
  Field: method_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_graph
  Field: method_description
"> percent_missing(method_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method metadata field 'method_description' should be defined
  Task id: batch_integration_graph
  Field: method_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_graph
  Field: metric_description
"> Metric info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_graph
  Field: metric_description
"> Pct 'metric_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_graph
  Field: metric_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_graph
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_graph
  Field: metric_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_graph
  Field: task_description
"> Task info </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_graph
  Field: task_description
"> Pct 'task_description' missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_graph
  Field: task_description
"> 1.000000 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_graph
  Field: task_description
"> percent_missing([task_info], field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Task metadata field 'task_description' should be defined
  Task id: batch_integration_graph
  Field: task_description
"> ✗✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: combat_full_scaled
  Metric id: isolated_labels_f1
  Best score: 3.0647051566740684%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: combat_full_scaled
  Metric id: isolated_labels_f1
  Best score: 3.0647051566740684%
"> Best score combat_full_scaled isolated_labels_f1 </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: combat_full_scaled
  Metric id: isolated_labels_f1
  Best score: 3.0647051566740684%
"> 3.064705 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: combat_full_scaled
  Metric id: isolated_labels_f1
  Best score: 3.0647051566740684%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method combat_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: combat_full_scaled
  Metric id: isolated_labels_f1
  Best score: 3.0647051566740684%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: harmony_full_scaled
  Metric id: isolated_labels_f1
  Best score: 2.8549222797927465%
"> Scaling </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: harmony_full_scaled
  Metric id: isolated_labels_f1
  Best score: 2.8549222797927465%
"> Best score harmony_full_scaled isolated_labels_f1 </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: harmony_full_scaled
  Metric id: isolated_labels_f1
  Best score: 2.8549222797927465%
"> 2.854922 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: harmony_full_scaled
  Metric id: isolated_labels_f1
  Best score: 2.8549222797927465%
"> best_score &lt;= 2 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Method harmony_full_scaled performs a lot better than baselines.
  Task id: batch_integration_graph
  Method id: harmony_full_scaled
  Metric id: isolated_labels_f1
  Best score: 2.8549222797927465%
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
