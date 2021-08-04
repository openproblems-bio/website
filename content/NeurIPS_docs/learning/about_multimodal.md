---
title: "About multimodal single-cell data"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 2
---
The goal for this page is to provide an introduction to multimodal single-cell data and the specific datasets used in the competition. We know that many participants may be encountering this data type for the first time (it's only been around for a couple of years!), and so this page serves as a general introduction. At the end you will find further reading recommendations that you can consult if you'd like to learn more.

## The flow of genetic information in cells

Cells are the fundamental unit of life. All living things are made of of cells. This includes trees, fish, humans, bacteria, fungi, etc. Cells come in all shapes and sizes, but they have several properties in common no matter where we look. For example, all cells are membrane-bound. This means they have a clear boundary between inside and outside. All cells contain some form of organelles, which are specialized substructures that perform a specific function. And, all cells contain three layers of genetic information: [DNA](https://www.genome.gov/genetics-glossary/Deoxyribonucleic-Acid), [RNA](https://www.genome.gov/genetics-glossary/RNA-Ribonucleic-Acid), and [protein](https://www.genome.gov/genetics-glossary/Protein).


<figure>
  <img src="/media/learning/central-dogma-large.png">
  <figcaption>
    <p style="font-size: medium;">
      <strong>Genetic information within a cell flows from DNA to RNA to protein</strong>
    </p>
  </figcaption>
</figure>

DNA defines an organism. Indeed, you can changes the species of a bacteria through [genome transplantation](https://pubmed.ncbi.nlm.nih.gov/17600181/). However, DNA is not functional. It contains a set of instructions that must be converted into RNA and then into protein. For most purposes, you can think of RNA as a messenger between DNA and protein. DNA is made up of [genes](https://www.genome.gov/genetics-glossary/Gene) that contain instructions on how to make proteins. Proteins are responsible for carrying out biological functions in the cell, such as metabolising glucose to create energy for the cell.  Generally speaking, each protein in your body is encoded by a single gene.

Although all of cells in your body contain the same genome, the same set of DNA, these trillions carry out very different biological functions. The differences between an immune cell, a neuron, or a muscle cell is defined by which genes are turned on or off within those cells. When a gene is turned on, more copies of RNA are created thereby increasing the production of protein. We know that regulation of the amount of protein both happens at the level of transcription (DNA -> RNA) and translation (RNA -> protein).

<figure>
  <img style="width: 500px;" src="/media/learning/differing_expression.png">
  <figcaption>
    <p style="font-size: medium;">
      <strong>Regulation of gene expression affects the amount of RNA and protein in the cells</strong>. In this example, gene A is more upregulated than gene B resulting more RNA and more protein.
    </p>
  </figcaption>
</figure>

Because we know that the difference between types of cells has to do with different levels of RNA and proteins, it's very useful to be able to measure the abundance of these molecules at the level of individual cells. Not only does this give us a fine-resolution view into the different kinds of cells in the body, it also provides insight into how the same set of DNA instructions can be interpreted so differently throughout the body.

The promise of single-cell measurements of genetics information is that by better understanding how this information flow within our cells and tissues, we might better understand what goes wrong in the context of disease.

## A rough history of single-cell technologies

This is an exciting time to study single-cell data.

<figure>
  <img src="/media/learning/timeline.png">
  <figcaption>
    <p style="font-size: medium;">
      <strong>An abbreviated timeline of single-cell technologies</strong>
    </p>
  </figcaption>
</figure>

The first measurement of RNA from single cells was described in Eberwine et al. [(1992)](https://www.pnas.org/content/89/7/3010) using molecular probes. It wasn't until [2009](https://www.ncbi.nlm.nih.gov/pubmed/19349980/), when Tang et al. described the sequencing of the transcriptome of a single cell (a mouse blastomere). In the following 6 years, several innovations were developed to improve the throughput of single-cell RNA sequencing (scRNA-seq). Perhaps the most impactful was the simultaneous description of two droplet-based protocols for capturing single cells into nanoliter droplets in oil emulsion described by Klein et al. [(2015)](https://pubmed.ncbi.nlm.nih.gov/26000487/) and Macosko et al. [(2015)](https://pubmed.ncbi.nlm.nih.gov/26000488/).

<figure>
  <img src="/media/learning/dropseq.gif">
  <figcaption>
    <h4>
      Capture of a single cell in a nanoliter droplet
    </h4>
    <p style="font-size: medium;">
      In this video from <a href="https://dropseq.org">dropseq.org</a>, we see a single cell (bottom left channel) captured in a nanoliter droplet with an oligo-coated bead (left channel) in an oil emulsion (top and bottom right channels).
    </p>
  </figcaption>
</figure>


With droplet-based single-cell methods, it was suddenly possible to perform experiments with tens of thousands of cells.


## Multimodal single-cell technologies provide an opportunity to measure multiple aspects of genetic information in the same cell
Experimental techniques to measure multiple modalities within the same single cell are increasingly becoming available. The demand for these measurements is driven by the promise to provide a deeper insight into the state of a cell. Yet, the modalities are also intrinsically linked. We know that DNA must be accessible (ATAC data) to produce mRNA (expression data), and mRNA in turn is used as a template to produce protein (protein abundance). These processes are regulated often by the same molecules that they produce: for example, a protein may bind DNA to prevent the production of more mRNA. Understanding these regulatory processes would be transformative for synthetic biology and drug target discovery. Any method that can predict a modality from another must have accounted for these regulatory processes, but the demand for multi-modal data shows that this is not trivial.

<figure>
  <img src="/media/learning/ATAC-seq.svg">
  <figcaption>
    <h3>
      Multimodal scRNA and scATAC from cell nuclei
    </h3>
    <p style="font-size: medium;">
      In this task, the goal is to take one modality (ATAC or RNA) and predict the other modality (RNA or Protein) for all features in each cell. Performance is measured using Mean Square Error.
    </p>
  </figcaption>
</figure>
