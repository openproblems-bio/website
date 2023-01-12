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
methods](https://openproblems.bio/bibliography#luecken2022benchmarking).

## The metrics

Metrics for batch integration (graph) measure how well batches are mixed while
biological signals are preserved. They are divided into batch correction and biological
variance conservation metrics.

### Batch correction

* **Graph connectivity**: The graph connectivity metric assesses whether the kNN graph
representation, G, of the integrated data connects all cells with the same cell identity
label.

### Biological variance removal

* **Adjusted rand index (ARI)**: The Rand index compares the overlap of two clusterings;
it considers both correct clustering overlaps while also counting correct disagreements
between two clusterings.
* **Iso label F1 score**: Isolated cell labels are identified as the labels present in
the least number of batches in the integration task. The score evaluates how well these
isolated labels separate from other cell identities based on clustering.
* **Normalized mutual information (NMI)**: NMI compares the overlap of two clusterings.
We used NMI to compare the cell-type labels with Louvain clusters computed on the
integrated dataset.

