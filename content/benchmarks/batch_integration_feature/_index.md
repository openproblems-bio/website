+++
title = "Batch integration feature"
summary = "Removing batch effects while preserving biological variation (feature output)"
headless = false
theme = "op"
+++
<!--- TODO: add links --->


## The task

This is a sub-task of the overall batch integration task. Batch (or data) integration
integrates datasets across batches that arise from various biological and technical
sources. Methods that integrate batches typically have three different types of output:
a corrected feature matrix, a joint embedding across batches, and/or an integrated
cell-cell similarity graph (e.g., a kNN graph). This sub-task focuses on all methods
that can output feature matrices. Other sub-tasks for batch integration can be found
for:

* [graphs](../batch_integration_graph/), and
* [embeddings](../batch_integration_embed/)

This sub-task was taken from a [benchmarking study of data integration
methods](https://www.biorxiv.org/content/10.1101/2020.05.22.111161v2).

## The metrics

Metrics for batch integration (feature) measure how well feature-level information is
batch corrected. This is only done on by capturing biological variance conservation.
Further metrics for batch correction and biological variance conservation that are
calculated on lower dimensional feature spaces extrapolated from corrected feature
outputs can be found in the batch integration embed and graph tasks.

* **HVG conservation**: This metric computes the average percentage of overlapping
highly variable genes per batch before and after integration.

