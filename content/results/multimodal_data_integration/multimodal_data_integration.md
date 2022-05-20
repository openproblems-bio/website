## The task

Several recently described technologies allow for simultaneous measurement of different aspects of cell state. For example, [sci-CAR](https://doi.org/10.1126/science.aau0730) jointly profiles RNA expression and chromatin accessibility on the same cell and [CITE-seq](https://doi.org/10.1038/nmeth.4380) measures surface protein abundance and RNA expression from each cell. However, these joint profiling methods have several tradeoffs compared to unimodal measurements.

Joint methods can be more expensive or lower throughput or more noisy than measuring a single modality at a time. Therefore it is useful to develop methods that are capable of integrating measurements of the same biological system but obtained using different technologies.

Here the goal is to learn a latent space where observations from the same cell acquired using different modalities. A perfect result has each of the paired observations sharing the same coordinates in the latent space.

## The metrics
Metrics for multimodal data integration aim to characterize how well the aligned datasets correspond to the ground truth.

* **kNN AUC**: Let <v-math>f(i) ∈ F</v-math> be the scRNA-seq measurement of cell <v-math>i</v-math>, and <v-math>g(i) ∈ G</v-math> be the scATAC- seq measurement of cell <v-math>i</v-math>. kNN-AUC calculates the average percentage overlap of neighborhoods of <v-math>f(i)</v-math> in <v-math>F</v-math> with neighborhoods of <v-math>g(i)</v-math> in <v-math>G</v-math>. Higher is better.
* **MSE**: Mean squared error (MSE) is the average distance between each pair of matched observations of the same cell in the learned latent space. Lower is better.


## The results