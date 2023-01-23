---
title: "Spatial Decomposition"
summary: "Calling cell-type compositions for spot-based spatial transcriptomics data"
bibliography: "../../../static/bibliography/main.bib"
---

<script src="index_files/libs/kePrint-0.0.1/kePrint.js"></script>
<link href="index_files/libs/lightable-0.0.1/lightable.css" rel="stylesheet" />


missing 'task_description'

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary-1.png" width="752" alt="Overview of the results per method. This figures shows the means of the scaled scores per method across all results (group Mean), per dataset (group Dataset) and per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method. This figures shows the means of the scaled scores per method across all results (group Mean), per dataset (group Dataset) and per metric (group Metric).</figcaption>
</figure>

<details>
<summary>
Overview per parameter set
</summary>

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/summary_defailed-1.png" width="725" alt="Overview of the results per method and parameter set. This figures shows the means of the scaled scores per method parameter set across all results (group Mean), per dataset (group Dataset) and per metric (group Metric)." />
<figcaption aria-hidden="true">Overview of the results per method and parameter set. This figures shows the means of the scaled scores per method parameter set across all results (group Mean), per dataset (group Dataset) and per metric (group Metric).</figcaption>
</figure>

</details>

## Methods

-   **Cell2location, amortised (detection_alpha=20, reference hard-coded)** (Kleshchevnikov et al. 2022): missing 'method_summary'

<!-- -->

-   **Cell2location (detection_alpha=1, reference hard-coded)** (Kleshchevnikov et al. 2022): missing 'method_summary'

<!-- -->

-   **Cell2location (detection_alpha=20, reference hard-coded)** (Kleshchevnikov et al. 2022): missing 'method_summary'

<!-- -->

-   **Cell2location (detection_alpha=200, reference hard-coded)** (Kleshchevnikov et al. 2022): missing 'method_summary'

<!-- -->

-   **Cell2location (detection_alpha=20, reference NB without batch info)** (Kleshchevnikov et al. 2022): missing 'method_summary'

<!-- -->

-   **DestVI** (Lopez et al. 2022): missing 'method_summary'

<!-- -->

-   **Non-Negative Matrix Factorization (NMF)** (Cichocki and Phan 2009): missing 'method_summary'

<!-- -->

-   **NMF-reg** (Rodriques et al. 2019): missing 'method_summary'

<!-- -->

-   **Non-Negative Least Squares** (Lawson and Hanson 1995): missing 'method_summary'

<!-- -->

-   **Random Proportions** (Open Problems for Single Cell Analysis Consortium 2022): missing 'method_summary'

<!-- -->

-   **RCTD** (Cable et al. 2021): missing 'method_summary'

<!-- -->

-   **SeuratV3** (Stuart et al. 2019): missing 'method_summary'

<!-- -->

-   **Stereoscope** (Andersson et al. 2020): missing 'method_summary'

<!-- -->

-   **Tangram** (Biancalani et al. 2021): missing 'method_summary'

<!-- -->

-   **True Proportions** (Open Problems for Single Cell Analysis Consortium 2022): missing 'method_summary'

## Datasets

-   **DestVI** (Lopez et al. 2022): scRNA-seq is generated based on learn NB parameters from the destVI manuscripts leveraging sparsePCA. Number of cells and cell types present in each spatial spot is computed via combination of kernel-based parametrization of a categorical distribution and the NB model.
-   **Pancreas (alpha=0.5)** (Luecken et al. 2021): Human pancreas cells aggregated from single-cell (Dirichlet alpha=0.5)
-   **Pancreas (alpha=1)** (Luecken et al. 2021): Human pancreas cells aggregated from single-cell (Dirichlet alpha=1)
-   **Pancreas (alpha=5)** (Luecken et al. 2021): Human pancreas cells aggregated from single-cell (Dirichlet alpha=5)
-   **Tabula muris senis (alpha=0.5)** (Tabula Muris Consortium 2020): Mouse lung cells aggregated from single-cell (Dirichlet alpha=0.5)
-   **Tabula muris senis (alpha=1)** (Tabula Muris Consortium 2020): Mouse lung cells aggregated from single-cell (Dirichlet alpha=1)
-   **Tabula muris senis (alpha=5)** (Tabula Muris Consortium 2020): Mouse lung cells aggregated from single-cell (Dirichlet alpha=5)

## Metrics

-   **r2** (Miles 2005): missing 'metric_summary'

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

<img src="index.markdown_strict_files/figure-markdown_strict/unnamed-chunk-9-1.png" width="960" />

</details>

## References

Andersson, Alma, Joseph Bergenstråhle, Michaela Asp, Ludvig Bergenstråhle, Aleksandra Jurek, José Fernández Navarro, and Joakim Lundeberg. 2020. "Single-Cell and Spatial Transcriptomics Enables Probabilistic Inference of Cell Type Topography." *Communications Biology* 3 (1). <https://doi.org/10.1038/s42003-020-01247-y>.

Biancalani, Tommaso, Gabriele Scalia, Lorenzo Buffoni, Raghav Avasthi, Ziqing Lu, Aman Sanger, Neriman Tokcan, et al. 2021. "Deep Learning and Alignment of Spatially Resolved Single-Cell Transcriptomes with Tangram." *Nature Methods* 18 (11): 1352--62. <https://doi.org/10.1038/s41592-021-01264-7>.

Cable, Dylan M., Evan Murray, Luli S. Zou, Aleksandrina Goeva, Evan Z. Macosko, Fei Chen, and Rafael A. Irizarry. 2021. "Robust Decomposition of Cell Type Mixtures in Spatial Transcriptomics." *Nature Biotechnology* 40 (4): 517--26. <https://doi.org/10.1038/s41587-021-00830-w>.

Cichocki, Andrzej, and Anh-Huy Phan. 2009. "Fast Local Algorithms for Large Scale Nonnegative Matrix and Tensor Factorizations." *IEICE Transactions on Fundamentals of Electronics, Communications and Computer Sciences* E92-a (3): 708--21. <https://doi.org/10.1587/transfun.e92.a.708>.

Kleshchevnikov, Vitalii, Artem Shmatko, Emma Dann, Alexander Aivazidis, Hamish W. King, Tong Li, Rasa Elmentaite, et al. 2022. "Cell2location Maps Fine-Grained Cell Types in Spatial Transcriptomics." *Nature Biotechnology* 40 (5): 661--71. <https://doi.org/10.1038/s41587-021-01139-4>.

Lawson, Charles L., and Richard J. Hanson. 1995. *Solving Least Squares Problems*. Society for Industrial; Applied Mathematics. <https://doi.org/10.1137/1.9781611971217>.

Lopez, Romain, Baoguo Li, Hadas Keren-Shaul, Pierre Boyeau, Merav Kedmi, David Pilzer, Adam Jelinski, et al. 2022. "DestVI Identifies Continuums of Cell Types in Spatial Transcriptomics Data." *Nature Biotechnology* 40 (9): 1360--69. <https://doi.org/10.1038/s41587-022-01272-8>.

Luecken, Malte D., M. Büttner, K. Chaichoompu, A. Danese, M. Interlandi, M. F. Mueller, D. C. Strobl, et al. 2021. "Benchmarking Atlas-Level Data Integration in Single-Cell Genomics." *Nature Methods* 19 (1): 41--50. <https://doi.org/10.1038/s41592-021-01336-8>.

Miles, Jeremy. 2005. "Encyclopedia of Statistics in Behavioral Science." In. John Wiley & Sons, Ltd. <https://doi.org/10.1002/0470013192.bsa526>.

Open Problems for Single Cell Analysis Consortium. 2022. "Open Problems." <https://openproblems.bio>.

Rodriques, Samuel G., Robert R. Stickels, Aleksandrina Goeva, Carly A. Martin, Evan Murray, Charles R. Vanderburg, Joshua Welch, Linlin M. Chen, Fei Chen, and Evan Z. Macosko. 2019. "Slide-Seq: A Scalable Technology for Measuring Genome-Wide Expression at High Spatial Resolution." *Science* 363 (6434): 1463--67. <https://doi.org/10.1126/science.aaw1219>.

Stuart, T., A. Butler, P. Hoffman, C. Hafemeister, E. Papalexi, W. M. Mauck, Y. Hao, M. Stoeckius, P. Smibert, and R. Satija. 2019. "Comprehensive Integration of Single-Cell Data." *Cell* 177 (7): 1888--1902.e21. <https://doi.org/10.1016/j.cell.2019.05.031>.

Tabula Muris Consortium. 2020. "A Single-Cell Transcriptomic Atlas Characterizes Ageing Tissues in the Mouse." *Nature* 583 (7817): 590--95. <https://doi.org/10.1038/s41586-020-2496-1>.
