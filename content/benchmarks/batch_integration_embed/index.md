---
title: "Batch integration embed"
summary: "Removing batch effects while preserving biological variation (embedding output)"
bibliography: "../../../static/bibliography/main.bib"
---

<script src="index_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="index_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


Missing 'task_description'

## Results

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="752" alt="Overview of the results per method. This figures shows the means of the scaled scores per method across all results (group Mean), per dataset (group Dataset) and per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the means of the scaled scores per method across all results (group Mean), per dataset (group Dataset) and per metric (group Metric).</figcaption>
</figure>

## Methods

-   **[Combat](https://scanpy.readthedocs.io/en/stable/api/scanpy.pp.combat.html)** (Johnson, Li, and Rabinovic 2006): Missing 'method_description'.

<!-- -->

-   **[FastMNN embed](https://doi.org/doi:10.18129/B9.bioc.batchelor)** (Lun 2019): Missing 'method_description'.

<!-- -->

-   **[Harmony](https://github.com/lilab-bcb/harmony-pytorch)** (Korsunsky et al. 2019): Missing 'method_description'.

<!-- -->

-   **[Liger](https://github.com/welch-lab/liger)** (Welch et al. 2019): Missing 'method_description'.

<!-- -->

-   **[MNN](https://github.com/chriscainx/mnnpy)** (Haghverdi et al. 2018): Missing 'method_description'.

<!-- -->

-   **[SCALEX](https://github.com/jsxlei/SCALEX)** (Xiong et al. 2022): Missing 'method_description'.

<!-- -->

-   **[Scanorama](https://github.com/brianhie/scanorama)** (Hie, Bryson, and Berger 2019): Missing 'method_description'.

<!-- -->

-   **[Scanorama gene output](https://github.com/brianhie/scanorama)** (Hie, Bryson, and Berger 2019): Missing 'method_description'.

<!-- -->

-   **[scANVI](https://github.com/YosefLab/scvi-tools)** (Xu et al. 2021): Missing 'method_description'.

<!-- -->

-   **[scVI](https://github.com/YosefLab/scvi-tools)** (Lopez et al. 2018): Missing 'method_description'.

## Metrics

-   **Cell Cycle Score** (Luecken et al. 2021): Missing 'metric_description'.

<!-- -->

-   **Isolated label Silhouette** (Luecken et al. 2021): Missing 'metric_description'.

<!-- -->

-   **kBET** (Büttner et al. 2018): Missing 'metric_description'.

<!-- -->

-   **PC Regression** (Luecken et al. 2021): Missing 'metric_description'.

<!-- -->

-   **Silhouette** (Luecken et al. 2021): Missing 'metric_description'.

<!-- -->

-   **Batch ASW** (Luecken et al. 2021): Missing 'metric_description'.

## Datasets

-   **Immune (by batch)** (Luecken et al. 2021): Missing 'dataset_description'.

<!-- -->

-   **Pancreas (by batch)** (Luecken et al. 2021): Missing 'dataset_description'.

## Baselines

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
Overview per parameter set
</summary>

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary_defailed-1.png" width="725" alt="Overview of the results per method and parameter set. This figures shows the means of the scaled scores per method parameter set across all results (group Mean), per dataset (group Dataset) and per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method and parameter set. This figures shows the means of the scaled scores per method parameter set across all results (group Mean), per dataset (group Dataset) and per metric (group Metric).</figcaption>
</figure>

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

<img src="index.markdown_strict_files/figure-markdown_strict/unnamed-chunk-10-1.png" width="960" />

</details>

## References

Büttner, Maren, Zhichao Miao, F. Alexander Wolf, Sarah A. Teichmann, and Fabian J. Theis. 2018. "A Test Metric for Assessing Single-Cell RNA-Seq Batch Correction." *Nature Methods* 16 (1): 43--49. <https://doi.org/10.1038/s41592-018-0254-1>.

Haghverdi, Laleh, Aaron T L Lun, Michael D Morgan, and John C Marioni. 2018. "Batch Effects in Single-Cell RNA-Sequencing Data Are Corrected by Matching Mutual Nearest Neighbors." *Nature Biotechnology* 36 (5): 421--27. <https://doi.org/10.1038/nbt.4091>.

Hie, Brian, Bryan Bryson, and Bonnie Berger. 2019. "Efficient Integration of Heterogeneous Single-Cell Transcriptomes Using Scanorama." *Nature Biotechnology* 37 (6): 685--91. <https://doi.org/10.1038/s41587-019-0113-3>.

Johnson, W. Evan, Cheng Li, and Ariel Rabinovic. 2006. "Adjusting Batch Effects in Microarray Expression Data Using Empirical Bayes Methods." *Biostatistics* 8 (1): 118--27. <https://doi.org/10.1093/biostatistics/kxj037>.

Korsunsky, Ilya, Nghia Millard, Jean Fan, Kamil Slowikowski, Fan Zhang, Kevin Wei, Yuriy Baglaenko, Michael Brenner, Po-ru Loh, and Soumya Raychaudhuri. 2019. "Fast, Sensitive and Accurate Integration of Single-Cell Data with Harmony." *Nature Methods* 16 (12): 1289--96. <https://doi.org/10.1038/s41592-019-0619-0>.

Lopez, Romain, Jeffrey Regier, Michael B. Cole, Michael I. Jordan, and Nir Yosef. 2018. "Deep Generative Modeling for Single-Cell Transcriptomics." *Nature Methods* 15 (12): 1053--58. <https://doi.org/10.1038/s41592-018-0229-2>.

Luecken, Malte D., M. Büttner, K. Chaichoompu, A. Danese, M. Interlandi, M. F. Mueller, D. C. Strobl, et al. 2021. "Benchmarking Atlas-Level Data Integration in Single-Cell Genomics." *Nature Methods* 19 (1): 41--50. <https://doi.org/10.1038/s41592-021-01336-8>.

Lun, Aaron. 2019. "A Description of the Theory Behind the fastMNN Algorithm." <https://marionilab.github.io/FurtherMNN2018/theory/description.html>.

Welch, Joshua D., Velina Kozareva, Ashley Ferreira, Charles Vanderburg, Carly Martin, and Evan Z. Macosko. 2019. "Single-Cell Multi-Omic Integration Compares and Contrasts Features of Brain Cell Identity." *Cell* 177 (7): 1873--1887.e17. <https://doi.org/10.1016/j.cell.2019.05.006>.

Xiong, Lei, Kang Tian, Yuzhe Li, Weixi Ning, Xin Gao, and Qiangfeng Cliff Zhang. 2022. "Online Single-Cell Data Integration Through Projecting Heterogeneous Datasets into a Common Cell-Embedding Space." *Nature Communications* 13 (1). <https://doi.org/10.1038/s41467-022-33758-z>.

Xu, Chenling, Romain Lopez, Edouard Mehlman, Jeffrey Regier, Michael I Jordan, and Nir Yosef. 2021. "Probabilistic Harmonization and Annotation of Single-Cell Transcriptomics Data with Deep Generative Models." *Molecular Systems Biology* 17 (1). <https://doi.org/10.15252/msb.20209620>.
