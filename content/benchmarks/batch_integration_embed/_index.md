+++
title = "Batch integration embed"
summary = "Removing batch effects while preserving biological variation (embedding output)"
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
that can output joint embeddings, and includes methods that canonically output corrected
feature matrices with subsequent postprocessing to generate a joint embedding. Other
sub-tasks for batch integration can be found for:

* [graphs](../batch_integration_graph/), and
* [corrected features](../batch_integration_features)

This sub-task was taken from a
[benchmarking study of data integration
methods](https://openproblems.bio/bibliography#luecken2022benchmarking).

