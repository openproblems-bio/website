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
<link href="index_files/libs/crosstalk-1.2.0/css/crosstalk.min.css" rel="stylesheet" />
<script src="index_files/libs/crosstalk-1.2.0/js/crosstalk.min.js"></script>
<script src="index_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="index_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


## Description

<!--- TODO: add links --->

## The task

This is a sub-task of the overall batch integration task. Batch (or data) integration
methods integrate datasets across batches that arise from various biological and
technical sources. Methods that integrate batches typically have three different types
of output: a corrected feature matrix, a joint embedding across batches, and/or an
integrated cell-cell similarity graph (e.g., a kNN graph). This sub-task focuses on all
methods that can output integrated graphs, and includes methods that canonically output
the other two data formats with subsequent postprocessing to generate a graph. Other
sub-tasks for batch integration can be found for:

-   [embeddings](../batch_integration_embed/), and
-   [corrected features](../batch_integration_feature/)

This sub-task was taken from a [benchmarking study of data integration
methods](https://openproblems.bio/bibliography#luecken2022benchmarking).

## The metrics

Metrics for batch integration (graph) measure how well batches are mixed while
biological signals are preserved. They are divided into batch correction and biological
variance conservation metrics.

### Batch correction

-   **Graph connectivity**: The graph connectivity metric assesses whether the kNN graph
    representation, G, of the integrated data connects all cells with the same cell identity
    label.

### Biological variance removal

-   **Adjusted rand index (ARI)**: The Rand index compares the overlap of two clusterings;
    it considers both correct clustering overlaps while also counting correct disagreements
    between two clusterings.
-   **Iso label F1 score**: Isolated cell labels are identified as the labels present in
    the least number of batches in the integration task. The score evaluates how well these
    isolated labels separate from other cell identities based on clustering.
-   **Normalized mutual information (NMI)**: NMI compares the overlap of two clusterings.
    We used NMI to compare the cell-type labels with Louvain clusters computed on the
    integrated dataset.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="745" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
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

<div id="htmlwidget-3da827c32dd52273e7a1" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-3da827c32dd52273e7a1">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">3<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">3<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","BBKNN (hvg/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","BBKNN (hvg/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">9<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">3<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","BBKNN (full/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">3<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","BBKNN (full/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">3<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">9<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">3<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">3<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","BBKNN (hvg/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","BBKNN (hvg/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","BBKNN (hvg/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (full/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">9<\/a><\/sup>","BBKNN (hvg/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (full/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">6<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (hvg/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">9<\/a><\/sup>","FastMNN feature (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (full/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","BBKNN (full/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">9<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","BBKNN (full/unscaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (hvg/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","FastMNN feature (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","BBKNN (full/scaled) <sup><a href=\"/bibliography#polanski2020bbknn\" target=\"_blank\">8<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN feature (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">2<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">9<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">9<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">5<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">4<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">7<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>"],["Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>"],[0.958757488377643,0.956213244319149,0.95429371124834,0.953781944611734,0.951341758950686,0.951204209932724,0.950288910257055,0.948061524598969,0.944328685012453,0.942801890394466,0.936088311567825,0.929600888392347,0.929417118003458,0.920912186373472,0.911825422787803,0.910688535416708,0.902468255762189,0.900689342394024,0.900016160431544,0.896523337663891,0.893860768656033,0.89229209998545,0.890892071366823,0.889670560873021,0.887932444719785,0.887850530400754,0.883336666418108,0.866879910818434,0.866454813433752,0.865171142106532,0.864906662390007,0.863549928428802,0.861733038677038,0.861484425529319,0.858899422981968,0.858090321496605,0.855909508256597,0.852997936284004,0.851956814949014,0.85190245320203,0.851431051149098,0.847546628939928,0.845575664390234,0.84429502771688,0.844260761119875,0.842279516862406,0.84181575771124,0.841243679469078,0.84095926870173,0.839644427597884,0.839120453027187,0.838138513025088,0.834875987549656,0.830294040580936,0.828530347438096,0.825278783625824,0.82441005475909,0.822426957749053,0.82232805141433,0.82080359725987,0.817919572296425,0.816829851521349,0.814903722978886,0.811902553290573,0.810455067357964,0.810132169289397,0.809739233526477,0.808510348209787,0.80810251466437,0.806326986723549,0.804288359056183,0.803130772244009,0.801470760903551,0.801033035656109,0.79964228892264,0.799087706192369,0.796727210304543,0.796180217436641,0.794978411804537,0.79287683031227,0.792339223423273,0.790309384311371,0.789898387724533,0.788781045887159,0.786898213802894,0.785962851692689,0.785812756550133,0.785310206814658,0.783718708038357,0.780395402460934,0.776074044834297,0.774267651312998,0.772360798700239,0.771401246626964,0.76755975584309,0.766247875849095,0.764964487381783,0.764949988230533,0.764116979234278,0.762113359389651,0.760224450486129,0.756668029739382,0.756364574865417,0.75599349932766,0.755902399169577,0.754054331773944,0.753302943362212,0.753109521247509,0.752491044434101,0.749688590417526,0.748183453793476,0.747700407078953,0.743008307166799,0.73382627714661,0.732874394051372,0.731162417194626,0.731004792395438,0.72968228038792,0.728594259598453,0.72627050626117,0.725586510061748,0.725184216364851,0.72484431633076,0.722501362820465,0.721395344694216,0.717493472352429,0.717484579707936,0.716274361934716,0.715761863319289,0.715014563558001,0.714013920584853,0.712400710931646,0.711254514193525,0.710046036335129,0.708664339432152,0.702099718037887,0.699024602075682,0.697928228047121,0.696727132750068,0.696408124454216,0.69565274149988,0.695605665952958,0.692683751240101,0.681399985284529,0.678025290252085,0.662112718365579,0.629244075262686,0.619046696865314,0.615934201085646,0.615526719756143,0.586604882833226,0.57609726895243,0.567195692109518,0.54645545118733,0.513728084115955,0.502178231446381,0.472323194345714,0.443011090061132,0.207808341871702,0.180740136100722],[0.957798980946152,0.953712336732752,0.951330404266517,0.947568324712799,0.948532621903516,0.944677193139033,0.946512973979787,0.944760619017823,0.944442015057048,0.944375397660184,0.948296643860005,0.915640584864964,0.905463920780188,0.946822274548619,0.847392232427807,0.942029919048551,0.87006402860303,0.914542103622205,0.911026906803194,0.926664120882014,0.841009604073809,0.884764221928954,0.905911521861838,0.83420837272783,0.84402054831647,0.771404909756939,0.825178868114838,0.879074827525321,0.841285689139113,0.767796822688042,0.918531140000329,0.881152996249669,0.775710582506858,0.7780357541664,0.771715527147382,0.815338264327475,0.785931028671991,0.793362909421918,0.779307143968901,0.88404289464062,0.792786603871669,0.658338564342456,0.704454195520573,0.892236558845301,0.79338814508465,0.752052759900922,0.744556399902598,0.807479156900098,0.758769221371095,0.703392250984548,0.730911978333337,0.748264522283153,0.871181712418211,0.783450259492897,0.704868433597163,0.734318520589867,0.677998175510683,0.654040156810918,0.716755495263185,0.694994902813937,0.69076472580933,0.68763245150635,0.749099424765193,0.736901427932647,0.735830268397129,0.731252992893501,0.675374324973556,0.666414177250905,0.745556672184516,0.724123396420335,0.746496062760163,0.60100346769208,0.627489179374828,0.755155358295814,0.633440888273952,0.705041373153531,0.697810202676682,0.733238122296903,0.618424481076565,0.5889829834181,0.731077117383595,0.746134904669652,0.703638180968086,0.639709013976189,0.609380410569739,0.659298294825376,0.639615280023531,0.566129035125618,0.695568594397625,0.611018684940274,0.572256024191937,0.758911150735868,0.59484343591879,0.627574375592699,0.692182618998392,0.608706580098025,0.622922531898665,0.623851921543273,0.604434511322317,0.6267689211913,0.617823276673144,0.621487041128054,0.526118708668576,0.607654738652033,0.468902745621031,0.644468132422152,0.622947222195147,0.706676664609365,0.573133119703964,0.51304529021192,0.701334891037633,0.460156432270857,0.520393012397631,0.535058423674237,0.48173386050708,0.561766552421004,0.470759388941626,0.474895366789725,0.526531289095968,0.491922344467082,0.442537184027384,0.479871760779569,0.505559493144405,0.695101883163039,0.484013287862011,0.595170680700099,0.528045085570683,0.464307368101728,0.606803791936913,0.454173201667784,0.465427557889816,0.501892784703493,0.520809229741524,0.493259509357381,0.52953548469261,0.481023114596263,0.425714562389029,0.43267994826877,0.516913885464686,0.490048617777113,0.550184693043055,0.482905987241329,0.561296077641586,0.442168371147481,0.516760402520689,0.519044249694145,0.392143009641813,0.506411084804207,0.60146541086215,0.581039021790254,0.417038181345291,0.483041354582661,0.461351558472535,0.400061826995801,0.375664128841768,0.3649508101013,0.385966765867286,0.307619211780811,0.0514957404369253,0.0871342855970504],[0.993849901775666,0.995419503997162,0.993057589705711,0.994049873026592,0.995116357164819,0.993120918609613,0.993403861775709,0.995871018046504,0.990577611269612,0.993773400532229,0.992095544019446,0.997339468146504,0.990777481998013,0.99570446920843,0.994132500432869,0.993187448123931,0.986772596143625,0.989572324931212,0.994610360536406,0.939766331268002,0.986107367835291,0.978408560389288,0.982175609002065,0.994784920661714,0.987143393913821,0.988207896602584,0.983430031413642,0.983960040164638,0.939111341161265,0.97193359462647,0.987702201025027,0.948338610303453,0.985392265760404,0.986045578841919,0.986489724044424,0.983686346697431,0.973771406097076,0.942111734423093,0.972149140827084,0.948360323903249,0.939402968237177,0.982942179941736,0.982353784412007,0.950499155033088,0.978668665269987,0.976906056834334,0.987311898242677,0.929479671137851,0.939424559412859,0.975206944055043,0.988703101290157,0.980179186614745,0.952921282381708,0.897255603046086,0.99053835978313,0.96917553267502,0.991029159494181,0.973446084733716,0.96018998224732,0.982842399500755,0.968090397721078,0.922908798906234,0.934251083857967,0.956188535522911,0.951902763897108,0.891151077456339,0.974444368179966,0.990825344016234,0.956168099884674,0.955736240363835,0.955330172032244,0.987168425357284,0.992306945733289,0.951403939441366,0.991326688151652,0.95617480958485,0.939676256035859,0.962291784674696,0.978097888928751,0.981637113964721,0.935290871698518,0.93441921697002,0.975403954068171,0.895924770926542,0.989570457408733,0.929435626401524,0.957208985356564,0.948971788076624,0.955190533156707,0.984864628286361,0.981046528052616,0.96823748636524,0.927128858020993,0.947603317127857,0.955191046999087,0.985441267744418,0.974124093375224,0.973693047227046,0.95548140591078,0.973930927360665,0.973546921386933,0.954876912670035,0.908847288939918,0.953299509443213,0.989403303171738,0.952276158829613,0.955875738710355,0.938347407540583,0.971734682385727,0.922812616815139,0.970109773514329,0.947531451924441,0.989966400746812,0.927168173416825,0.988416618266544,0.949412782334987,0.971606013288965,0.98969529615778,0.888824458974361,0.98551377383264,0.932641848803492,0.971625858302742,0.981179970147647,0.866528258692193,0.851038828978266,0.875303145929384,0.908212266768373,0.816560824647332,0.924422451297393,0.981956386879812,0.980785693735119,0.946639701613774,0.975267500407539,0.945881125843123,0.813681055381549,0.935371232658965,0.988074281811641,0.868264233293403,0.930711463451692,0.970411001863529,0.97026151029692,0.972627190614042,0.934703463153009,0.768690652745978,0.977753016164099,0.95488682583398,0.930569808958774,0.873624168669209,0.949233226297092,0.967145713607181,0.972841532479339,0.897575741921167,0.958686714474994,0.914534176549153,0.690553718382458,0.708254679023933,0.631264322157746,0.678195013671926,0.452706193322637,0.336710989398587],[0.951469594694978,0.951473426663615,0.950160275678938,0.955057736034122,0.941021889979566,0.95283379368398,0.946599366267345,0.938795207063226,0.925109362209911,0.924198191573194,0.885216741476706,0.942888456984248,0.95291485728858,0.836962630076159,0.926411853353381,0.800505249626141,0.884856217218704,0.827757521416403,0.83939318902555,0.844569738325585,0.880912128311705,0.854165155645475,0.802989363860151,0.952317210695646,0.866536129498877,0.947795005382919,0.915610983246563,0.764673923044901,0.84439010786041,0.896148260068843,0.689840316366647,0.794496491149986,0.867582009428572,0.862000441290391,0.848930069347022,0.831218389205609,0.840321016444349,0.846333539523244,0.84862918651552,0.741787342099187,0.843734114358352,0.916632581982267,0.893912575472163,0.692881138997807,0.811799644612078,0.833325720220869,0.841110176959526,0.826492570383776,0.830620126988118,0.887310698461102,0.848498347647236,0.808741892223729,0.695832122447095,0.812051249227721,0.828381603634668,0.792179892914543,0.826331989336426,0.91563919824663,0.834457458323065,0.806092530943619,0.818934148969614,0.876930860919711,0.784949146940817,0.768253040966786,0.769863521383616,0.83807803970682,0.803769243684029,0.855567191000153,0.745705305424106,0.758532268593032,0.72582865387165,0.849291257347487,0.867904214396649,0.696193947398142,0.832369755045377,0.761931447700932,0.803552593143185,0.718323963099301,0.8406281984689,0.852151176610411,0.745587362233996,0.71610339341594,0.733962983257277,0.841537628653832,0.78637696110464,0.802443315253372,0.79512219572501,0.897963488083242,0.724758272060292,0.866449102253522,0.808183568398219,0.55159842106393,0.849475466791613,0.770366408382064,0.663295382273986,0.773399293382174,0.734540361168298,0.733069318857711,0.763093124814939,0.717301956684151,0.729250795672746,0.720854039870962,0.856890381149641,0.74325154373512,0.881611827765532,0.692401094397306,0.702038519149036,0.615522510570536,0.807476689021432,0.85558679810595,0.54166001006663,0.8679070611352,0.77610424834505,0.728339537041655,0.724202511021228,0.69787589820516,0.784692966411379,0.850413822634035,0.768349099153929,0.704039744298283,0.859733167553467,0.751566880379496,0.706373790326106,0.585848364579499,0.856505006992436,0.682906251949391,0.712620526587569,0.865793087995485,0.637965438718884,0.716743131096829,0.699301395621348,0.733517967320754,0.624762696471686,0.735536219774624,0.769902264272411,0.749229542346885,0.839553407043488,0.829234608985025,0.668377808524998,0.632529408688275,0.613468795530924,0.630810248027167,0.632755263814614,0.806049809769578,0.676906936109749,0.560125357915681,0.727631899812492,0.436685354823058,0.135966050466348,0.172046589018303,0.329041992159959,0.297990805617462,0.218781190677273,0.315379080960697,0.61263486644143,0.576449757574957,0.433410629639382,0.38293962756359,0.135683770292755,0.101748657897215],[0.931911476093777,0.924247709883067,0.922626575342194,0.918451844673423,0.920696166754842,0.914184934298269,0.914639439005379,0.912819254268323,0.917185751513241,0.908860571812258,0.918744316915144,0.862535043573671,0.868512211947052,0.904159371660682,0.879365104937155,0.907031524868208,0.868180181083398,0.870885419606276,0.855034185361027,0.875093160179963,0.867413974403329,0.851830461978083,0.872491790743237,0.777371739406891,0.854029707149971,0.843994309860573,0.809126782897388,0.839810852538875,0.84103211557422,0.824805891042773,0.863552992168024,0.8302116160121,0.818247297012318,0.819855927818565,0.828462371389043,0.802118285755903,0.823614581812973,0.830183561767762,0.807741788484552,0.833419252165066,0.829800518129195,0.832273189493252,0.801582102156195,0.841563257991326,0.793186589512784,0.8068335304935,0.79428455574016,0.801523319454585,0.835023167034848,0.792667816890842,0.788368384838018,0.815368450978725,0.819568832951609,0.828419050557042,0.790332992737423,0.805441188323864,0.802280894695071,0.746582391204946,0.777909269823748,0.799284555781169,0.793889016685678,0.779847294753103,0.791315236351566,0.786267208739948,0.784223715754002,0.780046567100928,0.785368997268358,0.721234680571858,0.784979981164183,0.786916041516993,0.789498547560677,0.775059938579186,0.718182704109439,0.801378897489113,0.741431824219579,0.773203194330162,0.745869789362446,0.770866999675664,0.742763078743934,0.748736047255848,0.757401542376983,0.764580022189871,0.746588432604598,0.777952769992072,0.762265026128466,0.752674170290483,0.751304565095426,0.72817651597315,0.759357432538802,0.65924919436358,0.742810058694414,0.818323547086955,0.71799543406956,0.740060885405236,0.759569975100894,0.697444362171762,0.728270963084946,0.729185665294104,0.733458874889076,0.730451632322489,0.720276808211692,0.729454125288478,0.733601920703533,0.719768205480276,0.683691720120007,0.727071941446706,0.732350293394309,0.751891502269551,0.65761968662528,0.707309656537094,0.779629140555312,0.715206682985313,0.685569567177702,0.744738974453725,0.737144586410636,0.715594435817353,0.696960800939782,0.603724635970139,0.730672191169556,0.723606162446677,0.667433839862647,0.697672365997597,0.706264011704883,0.742526944847128,0.694024254944151,0.71659381083084,0.72106043990512,0.71843616699432,0.693855771323966,0.70718553458758,0.710541035093129,0.667552390088563,0.724178630153353,0.665507290365385,0.721538553382036,0.642774982549436,0.542756157058569,0.661534121641287,0.670905373558895,0.692643469487948,0.648695967128621,0.696079237929296,0.641980200351196,0.708691107475081,0.540680806213801,0.614394440018511,0.466631582637664,0.659466179164781,0.777072116716992,0.741875554608836,0.627497825348315,0.625781173688432,0.629963304813269,0.555846720243669,0.376059622798165,0.359057679085333,0.438651059718442,0.403290507228201,0.19134766343449,0.197366611510035],[1459,4163,1699,1640,18426,2258,4240,10569,1290,1550,1471,1340,6211,1459,1559,3100,9440.66666666667,2039,1639,1882,3598,11886,3001,1781,14253.6666666667,1569,1932,11819,1390,1735.66666666667,10755,1940,10728.3333333333,9964,12273,11925,1678,1570,2717,1760,1860,2040,12516,2092,12306,14390,3641,1880,1635.33333333333,4311.33333333333,1198.66666666667,2978,2142,1538,1992,1911.66666666667,2400,2949,17309,11379.3333333333,1363,1809.33333333333,2132,1126.33333333333,1190.66666666667,1688,1346.33333333333,1122.33333333333,1602.33333333333,1293,979,2201,1269,1039,1382,1492.33333333333,3591,6847,868,9310,1078,1402,2812,1866.33333333333,5150,1159,1642.66666666667,1830,1159,1346,13727,4015,3287,1189,1406,768,1010,1270,10169,1458,1519,1836.66666666667,3583.66666666667,2398.66666666667,1289,2248.33333333333,1416.33333333333,1905.66666666667,1228,4120,11182.6666666667,3082,1218,1909,3649,1530,2712,1259,10239,16150,1359,2401,2132,4002,1979,1272,23018,4430,1531.33333333333,1300,1290,1039,3959,1009,1871,2342,1029,3321,880,2561,17133.3333333333,1450,2252,2549,21971,2351,1919,19208,2098,12624,12120,1638,2322,1390,4039,21056,3960.33333333333,21687.6666666667,24799,3840],[538.9,1108.2,441.2,341.8,2042.4,479.6,565.7,2636.5,351.6,205.2,561.9,346.6,878.2,455,1169.8,556.5,1941.46666666667,283.6,218.1,124.3,1549.8,2350.2,336.9,254.4,2447.23333333333,716.7,509.5,2684.1,94.1,457.4,2483.4,99.1,2651.53333333333,1773.06666666667,2366,2370.5,475.9,76.2,1039.1,84.6,133.4,413.2,2615.2,120.3,2697.3,4831.2,1330.6,448.4,506.9,1176.16666666667,368.6,693.2,209.9,529.4,1500.6,469.266666666667,1056.63333333333,369,1516.5,3692.6,239.933333333333,534.7,507.8,94.9333333333333,390.066666666667,502.5,201.666666666667,293.166666666667,136.7,86.0333333333333,84.6,1249.2,169,88.3,176.933333333333,187.1,1270.1,2429.8,481.8,2620.8,594.7,243.6,264.2,475.566666666667,1478,160.6,397.733333333333,455.1,302.1,487.466666666667,2383,1436,986.866666666667,169.5,166.4,355.8,106.1,93.6,2491.6,125.8,119.4,101.533333333333,1293,200.433333333333,145.1,169.233333333333,91.8666666666667,507.666666666667,245.5,1115.1,2452.76666666667,1319.7,167.6,452.4,499.5,540.4,157.2,177.1,1275.1,4696.8,369.2,132,338.1,102.1,439,1124.7,1870.6,1514.7,762.733333333333,230.3,217.4,96.7,560.9,103.8,511,234.2,962.5,1321.5,575,101.7,2071.1,94.3,255.4,476.7,1253.6,419.366666666667,340.8,100.9,1321.7,2383.3,3443.2,591.4,653.1,654,101,100.5,101.466666666667,100.7,100.7,101.3],[3.7109375,3.41796875,4.98046875,3.7109375,4.78515625,78.22265625,2.24609375,3.80859375,2.05078125,3.125,13.4765625,2.34375,30.078125,1.953125,34.9609375,19.43359375,9.21223958333333,2.44140625,2.83203125,5.2734375,142.08984375,13.57421875,2.34375,7.32421875,5.82682291666667,5.2734375,7.32421875,5.6640625,2.9296875,6.93359375,28.90625,10.15625,3.71093749967448,7.68229166666667,10.64453125,11.5234375,7.91015625,3.22265625,36.1328125,6.34765625,5.17578125,4.58984375,7.03125,17.578125,3.3203125,368.06640625,41.69921875,8.00781249902344,5.40364583333333,36.6861979166667,2.1484375,90.6901041666667,21.97265625,7.421875,34.86328125,17.0572916666667,64.4205729166667,29.98046875,586.9140625,318.75,4.8828125,6.67317708300781,17.1875,3.25520833333333,2.21354166666667,7.32421875,4.23177083333333,2.79947916666667,7.51953125,4.23177083333333,3.3203125,27.05078125,2.44140625,4.78515625,3.02734375,7.09635416666667,40.13671875,18.45703125,2.05078125,4.00390624902344,5.46875,2.1484375,23.046875,5.76171875,27.05078125,5.37109375,2.50651041666667,7.91015625,8.203125,8.85416666666667,9.27734375,20.3776041666667,36.1328125,4.6875,8.984375,2.9296875,3.515625,4.6875,25.09765625,7.91015625,8.30078125,13.3463541666667,23.73046875,29.39453125,3.41796875,22.9166666666667,7.03125,3.64583333333333,8.69140625,18.84765625,28.4830729166667,38.28125,2.83203125,5.078125,123.4375,2.34375,37.40234375,3.125,23.7630208333333,446.09375,2.734375,27.734375,20.5078125,4.78515625,6.73828125,8.69140625,25.29296875,25.29296875,8.85416666666667,4.8828125,5.56640625,6.93359375,157.71484375,12.01171875,5.37109375,28.80859375,10.546875,38.28125,2.44140625,17.87109375,593.033854166667,7.8125,23.4375,18.9453125,489.74609375,22.0052083333333,15.4296875,15.13671875,23.2421875,31.4453125,702.44140625,3.125,27.5390625,10.546875,3.61328125,13.18359375,4.42708333333333,15.7552083333333,18.9453125,4.8828125]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>ARI<\/th>\n      <th>Graph connectivity<\/th>\n      <th>Isolated label F1<\/th>\n      <th>NMI<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":9,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8,9]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8,9]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render","options.columnDefs.7.render"],"jsHooks":[]}</script>

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

-   **Combat (full/scaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (full/unscaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (hvg/scaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (hvg/unscaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

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

-   **Harmony (full/scaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (full/unscaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (hvg/scaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (hvg/unscaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Liger (full/unscaled)**<sup><a href="/bibliography#welch2019single" target="_blank">11</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/welch-lab/liger).

<!-- -->

-   **Liger (hvg/unscaled)**<sup><a href="/bibliography#welch2019single" target="_blank">11</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/welch-lab/liger).

<!-- -->

-   **MNN (full/scaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (full/unscaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (hvg/scaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (hvg/unscaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **No Integration**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Random Integration**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **SCALEX (full)**<sup><a href="/bibliography#xiong2021online" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/jsxlei/SCALEX).

<!-- -->

-   **SCALEX (hvg)**<sup><a href="/bibliography#xiong2021online" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/jsxlei/SCALEX).

<!-- -->

-   **Scanorama (full/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (full/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (hvg/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (hvg/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (full/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (full/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (hvg/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (hvg/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">2</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **scANVI (full/unscaled)**<sup><a href="/bibliography#xu2021probabilistic" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scANVI (hvg/unscaled)**<sup><a href="/bibliography#xu2021probabilistic" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

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
"> 1 </td>
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
"> 1 </td>
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
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_graph
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_graph
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
