---
title: "Batch integration embed"
summary: "Removing batch effects while preserving biological variation (embedding output)"
---

<script src="index_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="index_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


<missing description>

## Overview

This visualization shows the means of the scaled scores per method across all results (group Mean), per dataset (group Dataset) and per metric (group Metric).

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="752" alt="The average overall, per dataset and per metric scaled scores per method." />
<figcaption aria-hidden="true">The average overall, per dataset and per metric scaled scores per method.</figcaption>
</figure>

<details>
<summary>
Overview per parameter set
</summary>

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary_defailed-1.png" width="725" alt="The average overall, per dataset and per metric scaled scores per method and parameter set." />
<figcaption aria-hidden="true">The average overall, per dataset and per metric scaled scores per method and parameter set.</figcaption>
</figure>

</details>

## Metrics

-   **Cell Cycle Score**: <missing description>
-   **Isolated label Silhouette**: <missing description>
-   **kBET**: <missing description>
-   **PC Regression**: <missing description>
-   **Silhouette**: <missing description>
-   **Batch ASW**: <missing description>

## Details

<details>
<summary>
Quality control checks
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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  Metric id: pcr
  Percentage missing: 26%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  Metric id: pcr
  Percentage missing: 26%
"> Metric pcr %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  Metric id: pcr
  Percentage missing: 26%
"> 0.2631579 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  Metric id: pcr
  Percentage missing: 26%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  Metric id: pcr
  Percentage missing: 26%
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
"> Method combat_full_scaled %missing </td>
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
"> Method combat_hvg_scaled %missing </td>
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
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_unscaled
  Percentage missing: 17%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_unscaled
  Percentage missing: 17%
"> Method combat_hvg_unscaled %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_unscaled
  Percentage missing: 17%
"> 0.1666667 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_unscaled
  Percentage missing: 17%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: combat_hvg_unscaled
  Percentage missing: 17%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_full_scaled
  Percentage missing: 17%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_full_scaled
  Percentage missing: 17%
"> Method fastmnn_embed_full_scaled %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_full_scaled
  Percentage missing: 17%
"> 0.1666667 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_full_scaled
  Percentage missing: 17%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_full_scaled
  Percentage missing: 17%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_hvg_scaled
  Percentage missing: 17%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_hvg_scaled
  Percentage missing: 17%
"> Method fastmnn_embed_hvg_scaled %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_hvg_scaled
  Percentage missing: 17%
"> 0.1666667 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_hvg_scaled
  Percentage missing: 17%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: fastmnn_embed_hvg_scaled
  Percentage missing: 17%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_full_scaled
  Percentage missing: 17%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_full_scaled
  Percentage missing: 17%
"> Method harmony_full_scaled %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_full_scaled
  Percentage missing: 17%
"> 0.1666667 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_full_scaled
  Percentage missing: 17%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_full_scaled
  Percentage missing: 17%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_hvg_scaled
  Percentage missing: 17%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_hvg_scaled
  Percentage missing: 17%
"> Method harmony_hvg_scaled %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_hvg_scaled
  Percentage missing: 17%
"> 0.1666667 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_hvg_scaled
  Percentage missing: 17%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: harmony_hvg_scaled
  Percentage missing: 17%
"> ✗ </td>
  </tr>
  <tr>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: no_integration
  Percentage missing: 17%
"> Raw results </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: no_integration
  Percentage missing: 17%
"> Method no_integration %missing </td>
   <td style="text-align:right;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: no_integration
  Percentage missing: 17%
"> 0.1666667 </td>
   <td style="text-align:left;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: no_integration
  Percentage missing: 17%
"> pct_missing &lt;= .1 </td>
   <td style="text-align:left;color: red !important;" data-toggle="tooltip" data-container="body" data-placement="right" title="Percentage of missing results should be less than 10%.
  Task id: batch_integration_embed
  method id: no_integration
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

<img src="index.markdown_strict_files/figure-markdown_strict/unnamed-chunk-7-1.png" width="960" />

</details>
