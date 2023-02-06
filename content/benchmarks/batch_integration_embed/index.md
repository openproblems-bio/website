---
title: "Batch integration embed"
summary: "Removing batch effects while preserving biological variation (embedding output)"
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
that can output joint embeddings, and includes methods that canonically output corrected
feature matrices with subsequent postprocessing to generate a joint embedding. Other
sub-tasks for batch integration can be found for:

-   [graphs](../batch_integration_graph/), and
-   [corrected features](../batch_integration_features)

This sub-task was taken from a
[benchmarking study of data integration
methods](https://openproblems.bio/bibliography#luecken2022benchmarking).

## The metrics

Metrics for batch integration (embed) measure how well batches are mixed while
biological signals are preserved. They are divided into batch correction and biological
variance conservation metrics.

### Batch correction

-   **kBET**: kBET determines whether the label composition of a k nearest neighborhood of
    a cell is similar to the expected (global) label composition
    ([Buettner et al., Nat Meth 2019](https://openproblems.bio/bibliography#bttner2018test)).
    The test is repeated for a random subset of cells,
    and the results are summarized as a rejection rate over all tested neighborhoods.
-   **Silhouette batch score**: The absolute silhouette width is computed over batch
    labels per cell. As 0 then indicates that batches are well mixed and any deviation from
    0 indicates a batch effect, we use the 1-abs(ASW) to map the score to the scale \[0;1\].
-   **Principal component regression (PC regression)**: This compare the explained
    variance by batch before and after integration. It returns a score between 0 and 1
    (scaled=True) with 0 if the variance contribution hasn't changed. The larger the score,
    the more different the variance contributions are before and after integration.

### Biological variance conservation

-   **Cell cycle score**: The cell-cycle conservation score evaluates how well the
    cell-cycle effect can be captured before and after integration.
-   **Isolated label silhouette**: This score evaluates the compactness for the label(s)
    that is(are) shared by fewest batches. It indicates how well rare cell types can be
    preserved after integration.
-   **Cell type ASW**: The absolute silhouette with is computed on cell identity labels,
    measuring their compactness.

## Summary

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="903" alt="Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the mean of the scaled scores (group Overall), the mean scores per dataset (group Dataset) and the mean scores per metric (group Metric).</figcaption>
</figure>

## Metrics

-   **ARI**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Cell Cycle Score**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

<!-- -->

-   **Graph connectivity**<sup><a href="/bibliography#luecken2022benchmarking" target="_blank">1</a></sup>: Missing 'metric_description'.

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

<div id="htmlwidget-50b0f6f9dc1b561fae0b" style="width:100%;height:auto;" class="datatables html-widget"></div>
<script type="application/json" data-for="htmlwidget-50b0f6f9dc1b561fae0b">{"x":{"filter":"none","vertical":false,"extensions":["Select","SearchPanes","Buttons"],"caption":"<caption>Results table of the scores per method, dataset and metric (after scaling). Use the filters to make a custom subselection of methods and datasets. The \"Overall mean\" dataset is the mean value across all datasets.<\/caption>","data":[["MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">8<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">8<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","scANVI (hvg/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">8<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">8<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">8<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","scANVI (full/unscaled) <sup><a href=\"/bibliography#xu2021probabilistic\" target=\"_blank\">7<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">8<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","scVI (hvg/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">8<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","scVI (full/unscaled) <sup><a href=\"/bibliography#lopez2018deep\" target=\"_blank\">8<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Scanorama (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","Combat (full/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","MNN (hvg/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","Combat (hvg/unscaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","SCALEX (hvg) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Combat (hvg/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","MNN (hvg/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","MNN (full/unscaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","MNN (full/scaled) <sup><a href=\"/bibliography#haghverdi2018batch\" target=\"_blank\">3<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Harmony (hvg/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","SCALEX (full) <sup><a href=\"/bibliography#xiong2021online\" target=\"_blank\">6<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Harmony (full/unscaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Combat (full/scaled) <sup><a href=\"/bibliography#hansen2012removing\" target=\"_blank\">5<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Harmony (hvg/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Harmony (full/scaled) <sup><a href=\"/bibliography#korsunsky2019fast\" target=\"_blank\">4<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","FastMNN embed (hvg/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (hvg/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","FastMNN embed (full/unscaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","FastMNN embed (full/scaled) <sup><a href=\"/bibliography#lun2019fastmnn\" target=\"_blank\">10<\/a><\/sup>","Scanorama (full/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (full/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (hvg/scaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Scanorama gene output (hvg/unscaled) <sup><a href=\"/bibliography#hie2019efficient\" target=\"_blank\">9<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (full/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>","Liger (hvg/unscaled) <sup><a href=\"/bibliography#welch2019single\" target=\"_blank\">11<\/a><\/sup>"],["Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Overall mean","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Immune (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Pancreas (by batch) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Overall mean","Overall mean","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>","Lung (Viera Braga et al.) <sup><a href=\"/bibliography#luecken2022benchmarking\" target=\"_blank\">1<\/a><\/sup>"],[0.734464982678824,0.730973327318309,0.723317087859757,0.715379908583824,0.711276831785602,0.705953399544799,0.700325907876176,0.697193685873383,0.691055413074358,0.685863522249728,0.684421488916046,0.674404867300346,0.673830728049357,0.66521925863068,0.663200410032387,0.66269149590905,0.661470413425389,0.659356073336674,0.658922840302805,0.65813093072789,0.656895099643961,0.654145283547515,0.65298094161128,0.648450361796125,0.646590889769178,0.644790561196927,0.644545475713785,0.643675966915002,0.641652618382478,0.640412050527007,0.63905261396819,0.63846613331031,0.638011256148796,0.637403042110338,0.63693470945773,0.636895935693803,0.635103593461056,0.634687500605162,0.634461231547165,0.634441843132027,0.633837274856405,0.631539316424537,0.631338256862265,0.629878745670483,0.629079815796164,0.625860276720631,0.625606201826906,0.624580383789216,0.624252247259325,0.621898103360152,0.621838898980088,0.620631786158113,0.620274457568906,0.617467119007737,0.614773095093281,0.613044933548786,0.610282944503018,0.609320814206298,0.609194699641564,0.609168593506481,0.605122633461462,0.604864885850299,0.604345284083228,0.601995949929392,0.601851879905973,0.600149625143987,0.599931859758441,0.599815182088082,0.599790218448313,0.598973215997484,0.59692378880679,0.596431551539184,0.594665879336464,0.592736658451114,0.590823791705542,0.590477164049004,0.587458449229299,0.587215710499461,0.587160861570191,0.584257777562854,0.583249257559305,0.581290047367489,0.579098642921534,0.578541400746984,0.576966275605061,0.576678422877335,0.575002204399459,0.570799282433946,0.569337490505156,0.566746635240874,0.565796019803235,0.560239728550323,0.559216528696631,0.558115645355504,0.557466822775682,0.556837152037956,0.55525955245178,0.553381705554317,0.550403228820348,0.549196396279602,0.54871361735432,0.54827670725403,0.543883128368692,0.536471291679574,0.535943905893783,0.533819783299796,0.533030862144549,0.528876453320278,0.52749568471018,0.524825020613293,0.522883075583268,0.517164896195355,0.5166531333304,0.51155389456494,0.500843654169065,0.495672563259785,0.495560677023371,0.495110588782189,0.494188775785868,0.492448099376473,0.481657075138235,0.476962363199126,0.437528944319078,0.396579603391852,0.386584920180454,0.384769037968418,0.239815806387052,0.212771928329162],[0.944672472869337,0.944862302606786,0.94473918300727,0.94085882613047,0.906352445433889,0.921464872406478,0.947563851121128,0.948391533530283,0.847379211580501,0.948528230587909,0.944755905866215,0.953607381695707,0.825748684789987,0.88478116106441,0.948467330175804,0.870061863279057,0.844060189300444,0.841934529798763,0.716797130917608,0.951688048552885,0.879092602975888,0.761012996583364,0.918524188888973,0.771797047077053,0.815365408763053,0.778747169883637,0.775768059576212,0.67557880626723,0.704559734337535,0.727164895313356,0.895731958293581,0.755500437438112,0.786759132612156,0.68455002423072,0.752089207017922,0.705399821036919,0.768243716915448,0.733474183924931,0.724791103945989,0.79341851608796,0.95801899722846,0.779657297888281,0.70478983628771,0.69106258565092,0.847790769104394,0.695375838266864,0.744158236175549,0.572408770712054,0.505736056862653,0.795588914892634,0.755212839539875,0.703681744808073,0.723484611657559,0.653293100988367,0.589129756774459,0.454368115328167,0.550254219388904,0.75733675738548,0.724034759415285,0.566283969581303,0.881727249465636,0.64201069867943,0.731240382090467,0.883678801250449,0.660005453189578,0.783482091320206,0.519509037139221,0.694008325462973,0.727367095547131,0.6929106943581,0.516719171401782,0.558709218992475,0.627629120466251,0.807507456588736,0.60160772676858,0.73833512463268,0.465618452642053,0.771385405495706,0.75890851397731,0.50087104007474,0.67827892918064,0.492103777983908,0.754084560117209,0.530285382356188,0.494136957336743,0.493609490868021,0.417246355847323,0.69785462320298,0.748155428709898,0.533527845802654,0.495083256381457,0.581188631919457,0.626371750956162,0.626288001603662,0.681135326042619,0.656625849598894,0.561830970745366,0.442736252886446,0.695146701799992,0.392091145879036,0.513116870340316,0.483225959483251,0.400656434250184,0.646192977855237,0.633135860916209,0.592310046061755,0.609877847408167,0.546337178291187,0.535224453383264,0.572868752570893,0.521973133411054,0.444995911127044,0.539925591607758,0.504378374154517,0.52821361972875,0.501575712692517,0.503251046066106,0.479933777321953,0.432882537127049,0.464513116043414,0.494626304439836,0.506483640130634,0.364896626237234,0.375610859062809,0.386072609661556,0.307738238594321,0.0518344494150957,0.0874602681218676],[0.901750726552764,0.870285545465374,0.866848216812791,0.740366530101996,0.690020335814179,0.724016107857782,0.68201856129094,0.589348805493592,0.848470153176507,0.616125373719962,0.621403568692003,0.451346320554139,0.482259159709137,0.681459001029351,0.418440930200373,0.605153471625509,0.626851128465082,0.554795778788605,0.867798888387881,0.066709092441404,0.73739805582484,0.6928796283482,0.646219105012792,0.682655093293037,0.676450207445571,0.577017217585576,0.583542092306615,0.82577894562022,0.527029955850443,0.708906464717986,0.0578868652479592,0.793982551514378,0.434185299854071,0.790399708185087,0.812746135290716,0.747203033395215,0.247273811121094,0.903382796186888,0.794567971827642,0.644167842336648,0.0730168208679176,0.632886700477335,0.726870315212902,0.676659660444769,0.652456656145838,0.716673341844248,0.79120219319856,0.636160515110782,0.800001151404051,0.652457097801246,0.448335944897817,0.792154542328256,0.247476780885511,0.628541412791547,0.485054865891194,0.75606727207506,0.777166196489602,0.74035483108862,0.784187780992617,0.240927041067806,0.351037624408859,0.734243388312432,0.676027984108481,0.351037366915296,0.770307251284399,0.42908272755471,0.236207532510757,0.76275289270655,0.737369437256315,0.740370902719101,0.666265840892965,0.544001458014501,0.854421347972808,0.42673581883976,0.85739334344852,0.735007603664378,0.577653168758967,0.072838019114397,0.264257296030022,0.775525937983538,0.735058946053997,0.782478111453424,0.685270941954254,0.62788327911253,0.907377896969668,0.907290309230002,0.797433860187959,0.455701105008931,0.385105937764573,0.818050092176052,0.623600384154233,0.619111954606102,0.645074842667047,0.644997721312535,0.253689464874421,0.0831473293947325,0.728927746889196,0.749786310190319,0.587896373572219,0.4678949108551,0.405332567477067,0.696022637996886,0.499982282478615,0.0399363690107862,0.256816011747091,0.236643756240259,0.812211323758677,0.812348837641645,0.29067233966744,0.0740368049321806,0.251059385016819,0.38900928613331,0.0966913392479413,0.264966836860929,0.309199885201536,0.676665487792308,0.676809006622613,0.273808782641208,0.21429379470106,0.261494556669105,0.302194768081967,0.614692916987384,0.451771612155627,0.269217206374964,0.340289323928827,0.396149684827299,0.121984525338887,0.163754391839297],[0.993094080858232,0.99218463314023,0.993749108345673,0.988444208457775,0.981602394738634,0.991585391804714,0.9940266594579,0.992064705915873,0.994109609223175,0.995097304331337,0.995854909414431,0.994735672477703,0.983365386053009,0.978582049561413,0.99474286991804,0.986611697650661,0.987192040640426,0.985711177233951,0.960509859344296,0.993000420825305,0.984088922694146,0.980224780526694,0.987654222922619,0.986517370912868,0.983817428378729,0.986548537316125,0.985456554967824,0.974605123227643,0.982389894895796,0.969354190314703,0.990741501664129,0.966597476979474,0.973982155223779,0.990847293412653,0.977091618758557,0.990614384918913,0.972019595380815,0.908548104749757,0.935654621710207,0.978840064475846,0.99351171581751,0.972431612281258,0.938347451708067,0.96828476336157,0.940050616324532,0.982782071279211,0.955792545191199,0.981085313651607,0.981218482676269,0.939873342276907,0.987413848289057,0.975601585524119,0.975264723779511,0.935540853689585,0.981674691013194,0.982041932118614,0.970357730175459,0.952103055687725,0.96201110916315,0.94907621009336,0.948517218119463,0.958061444914825,0.973792068389932,0.946276020406082,0.930002617532169,0.898278174606631,0.947638821385349,0.966509036990791,0.934779382351966,0.956287685675424,0.977666222741072,0.975148648440594,0.948024329218643,0.930046308365052,0.949337113317496,0.955222253090678,0.980825013094641,0.988161891399087,0.939702367956848,0.987817886095869,0.956662689263194,0.985543417845124,0.946504454131954,0.955414566168198,0.947324077443929,0.946363467914382,0.97289710844101,0.940135059047674,0.88572416872459,0.928688548301414,0.959017562730483,0.967212945256386,0.95590178786009,0.954951822168585,0.924275848149722,0.984230244683599,0.949819255209009,0.932779687730753,0.867600716217912,0.931624550249993,0.923432824427447,0.897785338675359,0.91470907026599,0.979439721051984,0.900460075932429,0.929372251799193,0.973513087259777,0.973827039837252,0.927317213446404,0.987188793038392,0.909175695853257,0.770736107418821,0.9814236347462,0.886853279848079,0.908400097379216,0.97221597818529,0.971864068016877,0.816905470093933,0.86854197529792,0.854619344685025,0.831425814389097,0.87463960991581,0.707116476414238,0.689346458008516,0.631671830249891,0.678527413000787,0.453826152672313,0.338068316523246],[0.95271321149167,0.92500180142878,0.9238534537433,0.819845972393693,0.802485698709409,0.822845973349574,0.954942839434636,0.88503161261468,0.926223722470198,0.9408711102082,0.938638734692675,0.950840941859582,0.925268496610397,0.853411691266493,0.939860412109,0.884532371662911,0.866177599945393,0.884695232967932,0.833602172956171,0.950032858536621,0.763458096901184,0.807415527376442,0.689047381391805,0.849344481862658,0.830346368995874,0.859638845713648,0.867340928012274,0.801417502487865,0.894203592726794,0.792016315803183,0.953923445647972,0.556316009829224,0.839496025498504,0.835232771138335,0.832464587661899,0.855198785624098,0.895924092325682,0.701200969394634,0.733502276977583,0.810827296305855,0.929174799061853,0.844770093749739,0.612384132438529,0.818830577790492,0.843892642767706,0.8073371460561,0.766384630631337,0.808709756036069,0.707179260850132,0.84367765900497,0.840289263258321,0.732588487220384,0.887494041729859,0.648671569212928,0.852556753038294,0.717520156618095,0.613521887465952,0.72385966348654,0.710765803099545,0.898243392941921,0.774091779139978,0.793092958213749,0.540436321917052,0.743586552263936,0.801422626916198,0.811080200851677,0.868269416283284,0.757943767344904,0.783838073944738,0.723594205651998,0.676080936458581,0.624763276887918,0.7628788971022,0.825754614124384,0.138336253994434,0.761358316021588,0.700126267020641,0.947661541337534,0.823113250469654,0.724275805320709,0.765385271761063,0.704851617538468,0.714220520777485,0.560149428255057,0.734540805660463,0.735160778715749,0.330882552983105,0.802537635956066,0.839360613316537,0.659931569687746,0.220924217093148,0.174317817014446,0.712998597860055,0.703836926221145,0.829576712581134,0.920123313436204,0.696314956101497,0.860117945190176,0.583708625574274,0.726935580451639,0.854840678727118,0.301164421628596,0.319545241633753,0.927524192415562,0.855473744099444,0.853254959376952,0.716322641810519,0.72888395062622,0.72908475149543,0.847581978683432,0.85544980402674,0.851529725472826,0.793089526205022,0.786009370948885,0.713408861168807,0.632763447683751,0.630363208779723,0.863926754669669,0.829703049759229,0.715313982281486,0.806937305545592,0.433774956274768,0.575366935343236,0.61164455281061,0.433188634797041,0.38239887992837,0.138054748167108,0.104212726006239],[0.486684609291051,0.393472325925166,0.357749490443112,0.33200152440938,0.380769810122417,0.298211668766207,0.318390337277022,0.351667792215524,0.415837263539194,0.380980092693571,0.361832227898043,0.434195412857072,0.345237803313214,0.344673297548458,0.398044052578502,0.362937658026316,0.332626974275734,0.328717766588644,0.175771666938846,0.493521206419021,0.30438247992034,0.358712972206864,0.192701089083015,0.309944263673419,0.324225389622269,0.333706859809243,0.304879604391506,0.283452722275468,0.31251835021329,0.260393992392366,0.363837086252509,0.252720694768726,0.253443228552729,0.337093871748516,0.236694601503542,0.311386086659777,0.32366126406837,0.152624453830011,0.204534416403986,0.297873208731131,0.38444564353281,0.260861355338593,0.252405264192323,0.317535790586488,0.28704902963514,0.237440326520596,0.212328196064783,0.278851137226959,0.247180272358716,0.287053545768105,0.220627516327107,0.182131887357428,0.276195305942506,0.255388855228985,0.254933376545344,0.276377712449868,0.1784013453322,0.225790660979058,0.200239768089273,0.22401935723336,0.226968034680576,0.276526621406619,0.186602383270534,0.226967496223309,0.262376213454899,0.274997623098338,0.244121315247901,0.18865561311033,0.182333912602859,0.225789596919112,0.186528488364187,0.328592951990949,0.216230963933424,0.280246633667337,0.225920791807523,0.180280147841279,0.371840821027543,0.603710143020276,0.316418473751077,0.284058265046575,0.180263766915631,0.146908611469604,0.15508162200861,0.115080869720498,0.208168539667431,0.208173794560754,0.172903880693566,0.211408334098577,0.331253560778212,0.0884306402605746,0.103007965925524,0.178450447618259,0.14302367768593,0.142945356969269,0.421195942186954,0.4766334609543,0.169495743528653,0.361872451924996,-0.0555625656594965,0.0601027558785426,0.291949048862216,0.171911566050565,0.268304308543731,0.425496828708466,0.419666697578711,0.338694661984989,0.0280007529096402,0.0279481580596747,0.289812154622084,0.296846017052004,0.273687605600821,0.270723954722837,0.374344070564143,0.354572849731435,0.418650523907325,-0.00630521987625679,-0.00606554129021689,0.232267750888244,0.379178823147923,0.37963104987325,0.451113071003619,-0.160948745879481,0.0663173705340122,-0.0169444767531457,0.0286493561916122,0.0246732927383083,0.168651253560394,0.158455110987479],[0.137401776614535,0.450375112129466,0.11366856496693,0.272379322261399,0.545915628026626,0.453935076260768,0.19154418958629,0.141381119474914,0.140892172603972,0.256487196622687,0.267599642386762,0.288143527215377,0.465815990407034,0.219886875826954,0.292364671396763,0.233975741452336,0.234185136037863,0.168749210902747,0.268713834620285,0.26825214483729,0.238324381061802,0.12113668576618,0.267700677528949,0.193896821314677,0.230021149216436,0.248069267702046,0.237087294246975,0.0641259840977566,0.207743830429101,0.0870448215739912,0.234248356450564,0.22195287936055,0.317987603542237,0.113943930943457,0.137880841006885,0.144853477303197,0.258744823288944,0.3446608276611,0.350265879857828,0.233526900162801,0.216158525377148,0.139762784938467,0.450788030073077,0.101460683197883,0.377452516735645,0.127686145156005,0.293265083932516,0.22182198249294,0.0787811041236199,0.372121081106011,0.23684635364918,0.133194358438294,0.211182309720826,0.415661568054081,0.210135340191363,0.0554622665746601,0.291104467561212,0.258428534294108,0.080168641895698,0.189994721487304,0.334980403261081,0.230820953746667,0.225074570307435,0.332636643246543,0.0509025820732843,0.191352696433739,0.162452219062733,0.104772884145004,0.0409722411234392,0.257925402921606,0.413840674062877,0.0862454957455393,0.0232471207516796,0.186178034098072,0.313310673924552,0.261620148319814,0.0619352779340734,0.255396782356776,0.168134166537761,0.0560861429232029,0.261274048537743,0.0764283835583819,0.12754724039068,0.292392423369655,0.328347901358385,0.32626580535703,0.190758894000475,0.190111321385988,0.135618638841349,0.301872899277402,0.252787505086849,0.302750149248352,0.272586752634742,0.269708044242726,0.187118911617587,0.192353895080484,0.120643241233498,0.117884543745736,0.510159754148173,0.491195406583823,0.155371672760824,0.456182582334776,0.436507886094109,0.2142998699934,0.127313455695248,0.166662843880539,0.14897939392969,0.153775661585611,0.0968912778023966,0.198693889773321,0.146979757359473,0.19269416105351,0.169159489567978,0.14304644852159,0.0672856949432817,0.150221684124606,0.154431953284762,0.0868737095442742,0.0955773402622279,0.119781918397913,0.0539678331639115,0.424915494785992,0.24362897953149,0.273441250850579,0.329957412249675,0.263936291644773,0.123264400616838,0.206271231750274],[0.913736721444455,0.916788317842788,0.909118202422907,0.907637920984551,0.872903704541684,0.879474094903539,0.918467252614494,0.918915773832894,0.879387898038321,0.920711150647297,0.912835726447092,0.924331759058567,0.81103430918235,0.851861884338287,0.916827007503299,0.868232417198385,0.854061925133258,0.867709097358313,0.77795636867426,0.922612167454816,0.839844823901407,0.812171573052183,0.863578772854878,0.8285036081983,0.802160250592844,0.820619714666008,0.818287541609666,0.787676560256595,0.80162980085107,0.801116918523248,0.874302427426192,0.81913377906504,0.824078023578023,0.803212760792585,0.806874495367017,0.790377456885136,0.824977350681918,0.747111682880718,0.756086148682041,0.793230448497338,0.931968625351786,0.806725399170084,0.752652495958579,0.793934830995803,0.84367982129855,0.799418732967489,0.78887949099811,0.742871885901881,0.712597278722015,0.829794775250862,0.794328181878673,0.746642173674841,0.794635251738177,0.70469982819629,0.748796449884569,0.713795467572428,0.648770444340309,0.801422358473286,0.772637708717747,0.728241861012914,0.830773616620248,0.754214210614398,0.78035112549329,0.832667683457442,0.752726620756433,0.828455437782578,0.715275145909667,0.735536997158463,0.771837703014835,0.758934878511389,0.540767591292414,0.71605259854201,0.740116010774451,0.784234147829873,0.777125707492821,0.788155530800062,0.710610619616481,0.844023786020651,0.83496745817642,0.739872927454296,0.77076106502544,0.723672606177137,0.773081011927317,0.615587912117112,0.666090321579083,0.666504915891309,0.627587373054253,0.740627383808473,0.790540450739204,0.676769143224227,0.633201156964893,0.741937606466528,0.731161442641017,0.73347064886146,0.771019130995147,0.830010524682812,0.715654749794174,0.667513787145481,0.742581547238347,0.466920405711604,0.707004481221146,0.628967634652012,0.555953492525803,0.743444717144312,0.780868444656884,0.715229196046797,0.719364412628351,0.723553541314068,0.744478311394895,0.764383236061716,0.730380187709873,0.704230463851313,0.747935858483563,0.724431272649913,0.721127495614862,0.701239347235629,0.696620389723719,0.719752845846758,0.661615487187605,0.684799459134918,0.722054358548637,0.65953839627852,0.359178780555639,0.37617751187273,0.438772873257643,0.403419745448742,0.191542059512066,0.197559560661851],[0.840890553658763,0.739351015314732,0.999956538877201,0.998758036760544,0.885072749069541,0.917085619969484,1,0.999975761304869,0.670455490895285,0.887331140021786,0.89839131409157,0.79072089375738,0.967890912765062,0.913969822376352,0.803510039214333,0.81356284884291,0.894223313462588,0.850978614892259,0.958595649932516,0.816323162973239,0.918614971416696,0.87156341026535,0.999944601387756,0.735997830394999,0.932181967615628,0.872394566683944,0.920179565918511,0.999967693830735,0.876723828949283,0.999963384869376,0.864612562334035,0.998365930066214,0.912495134897442,0.688802201286545,0.882350639782649,0.864685240571184,0.872439134702431,0.963229935282504,0.939250153423055,0.936025116621954,0.570257622829908,0.924623174871154,0.864411269834838,1.00000000001702,0.700172692010646,0.813175862521434,0.726716916275736,0.881491693221873,0.999917886250946,0.700158701929697,0.937511531023027,1,0.896830258803086,0.944963872745306,0.92612226704201,0.999954814857591,0.964584338202774,0.859895326509336,0.9991425288181,0.888499106236611,0.864227563002742,0.730795669815922,0.999756070588524,0.864218833253957,1,0.802287256049989,0.888366683052195,0.999832434941393,0.999996507052313,0.859896970912901,0.980086905959938,0.849176502266133,0.999991727757413,0.897562084921566,0.997197224619998,0.670909166846339,1.00000000005107,0.734894209566944,0.555805894737755,0.531265872393167,0.670869836653007,0.706198332889394,0.881848823599817,0.9999999995039,0.811122563572559,0.811130150883384,0.955070458715869,0.927425520775509,0.800548413826046,0.55895090991266,0.999999998511699,0.999491175436425,0.770900238962974,0.770901813242711,0.74725985286521,0.532528376316001,0.939624512456584,0.335676877021699,0.93324102085434,1,0.691766893690585,0.768910907011918,0.903770770188352,0.765019715766358,0.548121505683418,0.813808437333337,0.452659482019035,0.452553837116422,0.294872805333369,0.466578213599424,0.460650536871882,0.644431089417753,0.591234770426832,0.558391491176911,0.43950861368615,0.63735645559079,0.637350590313622,0.223606503325637,0.748980075458143,0.609323264107118,0.311287726908207,0.945027501802242,0.945233275685119,0.880277085881622,0.879221071133432,0.912731400326835,0.847933423493144,0.824145106664334],[0.316841174854693,0.364812686533266,0.305408009620933,0.362495664080346,0.374607710730685,0.249651810112034,0.316817207151184,0.286138658006913,0.331550580405557,0.250027178866944,0.230965241142414,0.274291514024319,0.259603236797455,0.317056701335223,0.233053354238435,0.30580578020623,0.269740195478754,0.271575911975145,0.197346352742461,0.322876387332001,0.290219905422491,0.280524462053419,0.259204935816314,0.326069125259147,0.230604272091577,0.227274568601787,0.223738778824638,0.260658612161774,0.268973502146826,0.245976780018299,0.223241203990151,0.297186547366893,0.23120865256488,0.298724830634872,0.256241827593061,0.271538646287466,0.265167066505563,0.229986069633169,0.220054243634632,0.227684057229411,0.302455099076628,0.256975586959448,0.271859826165856,0.273019321901907,0.565224978003634,0.254907399078035,0.278331321317943,0.218166079475347,0.25007915463372,0.565224817877067,0.213246339981421,0.17726578854943,0.217010644048643,0.217939181805681,0.212567038102087,0.256161438402294,0.142677095383302,0.274506439136469,0.253514309596624,0.241416159619807,0.502735164707554,0.189591117845521,0.238120110741861,0.502734782454666,0.237493164761595,0.262595084599029,0.214544388174358,0.225844918644367,0.201712527414266,0.274506928475147,0.0779210971087144,0.267756624346115,0.220406388462094,0.287128623137672,0.275549668423708,0.378112560049633,0.264747593792942,0.389429577979783,0.27592831500472,0.293085265211593,0.378103411321257,0.236904457665898,0.223198046264134,0.154341034652554,0.168711472895943,0.168723541984229,0.152763836298731,0.232872467900184,0.305048327150057,0.246983231156428,0.185768131014314,0.229310477764902,0.28487706803791,0.284878503767411,0.314346251391029,0.365307462331388,0.183334341919729,0.135787201504799,0.231962104350204,0.0999891843939183,0.215112506271215,0.220917524132249,0.164228238986421,0.220852345625161,0.32099687945637,0.214425265048531,0.294606263008796,0.294578487611556,0.262734761338502,0.213327239922064,0.205009490104155,0.225826810674804,0.298843364194121,0.267903745193885,0.27904106071273,0.183177186863337,0.183184566510233,0.186588724119185,0.189550981620248,0.266480553055632,0.292634848887665,0.16064662074636,0.119475023284267,0.122282929120677,0.121319755490008,0.0947635791966695,0.00416909355938178,0.00971423299914391],[0.856864499152742,0.712599532796505,0.81808011035745,0.791011080258086,0.673037840668953,0.80126338001741,0.679488180828163,0.859021096344285,0.85624802881087,0.662476444797584,0.671937618529252,0.681835249503613,0.672083300865924,0.606510101959858,0.686693432989319,0.696041109146187,0.705585631514347,0.838693412860379,0.832136478513726,0.796293817906322,0.613526756320813,0.855810799296454,0.705234441225702,0.79977797597509,0.640736454969797,0.743888864007253,0.729174337283625,0.763497718924736,0.840753693424644,0.812182741743562,0.93200073237481,0.722905026714491,0.806477305164137,0.831223028730617,0.674913140595047,0.687702424256125,0.922585079620293,0.662655982507912,0.685905499008684,0.628824980871331,0.979364899420028,0.696699158571011,0.738873946750774,0.657999242757972,0.233028435935549,0.823805903516326,0.699003404483324,0.904236704062642,0.959831824711127,0.233031097694021,0.784577170956401,0.76305729368031,0.973170647383386,0.7699709473646,0.886760412450291,0.918700159491079,0.965991720690465,0.499510515022365,0.6052445866276,1.16498411579042,0.336167681208478,0.739291794953424,0.692051823924708,0.336155319822244,0.553282269091178,0.71988495914297,1.20293403881895,0.562294950376049,0.617695304175273,0.49951489383006,0.93336095978537,1.01386874016561,0.553712886925678,0.501972862938684,0.772459413257787,0.435770789223585,0.741227278354576,0.264655748703453,0.934372879060339,0.949718633124854,0.435834610881075,0.95781115709355,0.530149208043879,0.934279112214143,0.503842219566407,0.503561973368492,1.1324777237723,0.50931937315508,0.472019365201097,0.854261472609586,1.18457002016975,0.808626080172373,0.449269127660384,0.449177615165538,0.445050787053001,0.527411063901151,0.486950006640099,0.929661998202762,0.407298010107513,0.855210022792366,0.72920862976527,0.857678500574684,0.975173558719965,0.402506179224474,0.516586383172023,0.477796415225608,0.574773416712841,0.574957841119143,1.10386877861802,0.826745280499502,0.874465159878602,0.677471452081332,0.573883688260438,0.624985276563254,0.623600689347993,0.507815552305878,0.507797482206267,1.06744156937103,0.521563693297271,0.568523749516867,0.55032872041382,0.310853240949028,0.542304363449915,0.384742656689161,0.276706334844854,0.383351853978078,0.29689795753529,0.0380783377378867],[2772,3272,2425,3590,2209,2401,2149,2220,2453,12398,14347,9969,2231,11299,11540,10659,12298.6666666667,7390,8509,2592,10789,2430.66666666667,10595,10709,11619,10802.6666666667,12858.3333333333,1788.66666666667,13709,2133.66666666667,2739,3040.33333333333,2464,2854.66666666667,30050,2492,2435,3429,1630,10360,2501,2551,1706,1769.66666666667,2300,17563.3333333333,2773.66666666667,9249,2050,2252,5810,2252,3813.66666666667,2326.33333333333,13868,1380,9022.33333333333,1719,2881,2249,2622,1816.66666666667,9954,2493,1659,2441,2892,4840,2131,1639,7198,1969,1561,2702,2650,1783,1501,2252,2394.33333333333,3619,1797.33333333333,15250,1500,2314.33333333333,2249,1889,11360,5800,2101,3549,2361,14427,2464.33333333333,2013.66666666667,2138,2170,1679,1370,3752,2330,5800,1279,1319,2402,1916.66666666667,4660.33333333333,1330,1501,2241,2630,4970,5170,2810,3013,1059,1659,2522,6480,5779,1460,1479,19729,16589,3752,4074.66666666667,16989,14649,4720],[593,397.5,281.6,2051.8,281.2,449.7,707.4,565.8,976.4,2600.3,2660.1,2330.2,664.9,2255.8,2333.9,2328.2,2624.8,2549.7,2530.2,309,2658.4,1111.03333333333,2497.7,2398.6,2366.9,2359,2658.76666666667,413.266666666667,2615.7,723.366666666667,1127.9,1521.3,448.6,945.366666666667,1142.7,1216.2,429.5,455.6,502.6,2699.2,329.1,1182.6,432.6,526.8,90.5,2798.26666666667,512.933333333333,2376.2,873.7,99.6,1125.3,482.9,1222.2,728.8,2617,436.4,2929.46666666667,104.7,1121.7,530.9,93.4,563.433333333333,2126.56666666667,95.6,478.2,675.5,1413.4,1429.4,730.6,113.6,2789.5,1557.5,521.8,508.1,1390.4,100.533333333333,394.8,692,567.566666666667,643.5,105.633333333333,4702.4,629.4,540.9,101,111.2,3468.7,1268.5,323.9,511.9,581.3,2452.6,98.4333333333333,103.1,638.7,931.3,786,454.6,102.1,558.5,1704.9,514,1065.9,1270.9,680.9,1279.66666666667,106.4,103.7,698.1,344.8,866.666666666667,1406.8,392.7,1231,1893.5,102.5,100.9,550.3,1299.6,716,787.5,101,100.5,101.2,100.866666666667,100.7,100.6,99.3],[98.4375,2.05078125,3.125,19.43359375,2.34375,2.44140625,3.7109375,13.4765625,27.34375,4.78515625,3.7109375,6.54296875,7.32421875,13.4765625,6.0546875,10.3841145833333,5.859375,320.99609375,587.20703125,5.17578125,5.76171875,64.7135416666667,28.80859375,11.1328125,11.62109375,9.04947916666667,3.64583333333333,4.23177083333333,7.03125,17.0572916666667,32.8125,20.3450520833333,7.91015625,28.515625,362.6953125,26.953125,6.640625,8.69140625,2.9296875,3.3203125,4.58984375,46.77734375,2.79947916666667,4.98046875,2.9296875,375.48828125,2.18098958333333,9.47265625,20.5078125,3.22265625,41.69921875,23.046875,37.59765625,8.85416666666667,3.90625,4.8828125,593.294270833333,3.3203125,18.359375,6.8359375,10.15625,2.50651041666667,28.4830729163411,6.4453125,5.37109375,7.421875,38.28125,25.09765625,17.1875,4.4921875,488.96484375,48.92578125,4.6875,7.91015625,23.2421875,3.25520833333333,5.859375,5.2734375,5.76171875,31.25,4.00390625,442.7734375,2.1484375,21.4192708333333,12.01171875,6.93359375,703.7109375,40.13671875,7.421875,2.34375,25.78125,31.5429687490234,13.3463541666667,7.09635416666667,6.77083333333333,3.7109375,2.34375,2.734375,4.78515625,15.4296875,18.84765625,3.125,10.546875,30.078125,5.40364583333333,36.1328125,3.515625,4.296875,5.2734375,27.05078125,23.2747395833333,17.7734375,27.1484375,23.4049479166667,25.29296875,7.91015625,17.87109375,23.92578125,38.18359375,7.12890625,5.078125,15.13671875,13.18359375,3.41796875,4.36197916666667,15.7552083333333,18.9453125,4.8828125]],"container":"<table class=\"stripe compact\">\n  <thead>\n    <tr>\n      <th>Method<\/th>\n      <th>Dataset<\/th>\n      <th>Mean score<\/th>\n      <th>ARI<\/th>\n      <th>Cell Cycle Score<\/th>\n      <th>Graph connectivity<\/th>\n      <th>Isolated label F1<\/th>\n      <th>Isolated label Silhouette<\/th>\n      <th>kBET<\/th>\n      <th>NMI<\/th>\n      <th>PC Regression<\/th>\n      <th>Silhouette<\/th>\n      <th>Batch ASW<\/th>\n      <th>Runtime (s)<\/th>\n      <th>CPU (%)<\/th>\n      <th>Memory (GB)<\/th>\n    <\/tr>\n  <\/thead>\n<\/table>","options":{"dom":"Bt","paging":false,"columnDefs":[{"targets":14,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":13,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 0, 3, \",\", \".\", null);\n  }"},{"targets":15,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":2,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":3,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":4,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":5,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":6,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":7,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":8,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":9,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":10,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":11,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"targets":12,"render":"function(data, type, row, meta) {\n    return type !== 'display' ? data : DTWidget.formatRound(data, 2, 3, \",\", \".\", null);\n  }"},{"searchPanes":{"show":false},"targets":[2,3,4,5,6,7,8,9,10,11,12,13,14,15]},{"searchPanes":{"preSelect":"Overall mean"},"targets":1},{"className":"dt-right","targets":[2,3,4,5,6,7,8,9,10,11,12,13,14,15]}],"buttons":["searchPanes","csv","excel"],"language":{"searchPanes":{"collapse":"Filter datasets / methods"}},"scrollX":true,"order":[],"autoWidth":false,"orderClasses":false}},"evals":["options.columnDefs.0.render","options.columnDefs.1.render","options.columnDefs.2.render","options.columnDefs.3.render","options.columnDefs.4.render","options.columnDefs.5.render","options.columnDefs.6.render","options.columnDefs.7.render","options.columnDefs.8.render","options.columnDefs.9.render","options.columnDefs.10.render","options.columnDefs.11.render","options.columnDefs.12.render","options.columnDefs.13.render"],"jsHooks":[]}</script>

## Details

<details>
<summary>
Methods
</summary>

-   **Random Integration by Batch**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Random Embedding by Celltype**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Random Integration by Celltype**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Combat (full/scaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (full/unscaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (hvg/scaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **Combat (hvg/unscaled)**<sup><a href="/bibliography#hansen2012removing" target="_blank">5</a></sup>: Missing 'method_description'. Links: [Docs](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html).

<!-- -->

-   **FastMNN embed (full/scaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN embed (full/unscaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN embed (hvg/scaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **FastMNN embed (hvg/unscaled)**<sup><a href="/bibliography#lun2019fastmnn" target="_blank">10</a></sup>: Missing 'method_description'. Links: [Docs](https://doi.org/doi:10.18129/B9.bioc.batchelor).

<!-- -->

-   **Harmony (full/scaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (full/unscaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (hvg/scaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Harmony (hvg/unscaled)**<sup><a href="/bibliography#korsunsky2019fast" target="_blank">4</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/lilab-bcb/harmony-pytorch).

<!-- -->

-   **Liger (full/unscaled)**<sup><a href="/bibliography#welch2019single" target="_blank">11</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/welch-lab/liger).

<!-- -->

-   **Liger (hvg/unscaled)**<sup><a href="/bibliography#welch2019single" target="_blank">11</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/welch-lab/liger).

<!-- -->

-   **MNN (full/scaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (full/unscaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (hvg/scaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **MNN (hvg/unscaled)**<sup><a href="/bibliography#haghverdi2018batch" target="_blank">3</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/chriscainx/mnnpy).

<!-- -->

-   **No Integration**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **No Integration by Batch**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **Random Integration**<sup><a href="/bibliography#openproblems" target="_blank">12</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/openproblems-bio/openproblems).

<!-- -->

-   **SCALEX (full)**<sup><a href="/bibliography#xiong2021online" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/jsxlei/SCALEX).

<!-- -->

-   **SCALEX (hvg)**<sup><a href="/bibliography#xiong2021online" target="_blank">6</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/jsxlei/SCALEX).

<!-- -->

-   **Scanorama (full/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (full/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (hvg/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama (hvg/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (full/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (full/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (hvg/scaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **Scanorama gene output (hvg/unscaled)**<sup><a href="/bibliography#hie2019efficient" target="_blank">9</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/brianhie/scanorama).

<!-- -->

-   **scANVI (full/unscaled)**<sup><a href="/bibliography#xu2021probabilistic" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scANVI (hvg/unscaled)**<sup><a href="/bibliography#xu2021probabilistic" target="_blank">7</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scVI (full/unscaled)**<sup><a href="/bibliography#lopez2018deep" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

<!-- -->

-   **scVI (hvg/unscaled)**<sup><a href="/bibliography#lopez2018deep" target="_blank">8</a></sup>: Missing 'method_description'. Links: [Docs](https://github.com/YosefLab/scvi-tools).

</details>
<details>
<summary>
Baseline methods
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
"> 1 </td>
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
"> 1 </td>
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
"> 1 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_embed
  Field: metric_description
"> percent_missing(metric_info, field) </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Metric metadata field 'metric_description' should be defined
  Task id: batch_integration_embed
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
