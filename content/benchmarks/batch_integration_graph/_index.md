+++
title = "Batch integration graph"
summary = "Removing batch effects while preserving biological variation (graph output)"
headless = false
theme = "op"
+++
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

* [embeddings](../batch_integration_embed/), and
* [corrected features](../batch_integration_feature/)

This sub-task was taken from a [benchmarking study of data integration
methods](https://www.biorxiv.org/content/10.1101/2020.05.22.111161v2).

## The metrics

Metrics for batch integration (graph) aim to TODO

* **TODO**: TODO
* **TODO**: TODO

