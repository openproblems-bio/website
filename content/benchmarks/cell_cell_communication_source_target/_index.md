+++
title = "Cell-Cell Communication Inference (Source-Target)"
summary = "Detect interactions between source and target cell types"
headless = false
theme = "op"
+++

## The task

The growing availability of single-cell data has sparked an increased
interest in the inference of cell-cell communication (CCC),
with an ever-growing number of computational tools developed for this purpose.

Different tools propose distinct preprocessing steps with diverse
scoring functions, that are challenging to compare and evaluate.
Furthermore, each tool typically comes with its own set of prior knowledge.
To harmonize these, [Dimitrov et
al, 2022](https://openproblems.bio/bibliography#dimitrov2022comparison) recently
developed the [LIANA](https://github.com/saezlab/liana) framework, which was used
as a foundation for this task.

The challenges in evaluating the tools are further exacerbated by the
lack of a gold standard to benchmark the performance of CCC methods. In an
attempt to address this, Dimitrov et al use alternative data modalities, including
the spatial proximity of cell types and
downstream cytokine activities, to generate an inferred ground truth. However,
these modalities are only approximations of biological reality and come
with their own assumptions and limitations. In time, the inclusion of more
datasets with known ground truth interactions will become available, from
which the limitations and advantages of the different CCC methods will
be better understood.

**This subtask evaluates methods in their ability to predict interactions between
spatially-adjacent source cell types and target cell types. This subtask focuses
on the prediction of interactions from steady-state, or single-context,
single-cell data.**

