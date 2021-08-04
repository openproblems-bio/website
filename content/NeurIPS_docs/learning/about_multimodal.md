---
title: "About multimodal single-cell data"
type: book
date: "2021-08-02T00:00:00+01:00"
# Prev/next pager order (if `docs_section_pager` enabled in `params.toml`)
weight: 2
---
The goal for this page is to provide an introduction to multimodal single-cell data and the specific datasets used in the competition. We know that many participants may be encountering this data type for the first time (it's only been around for a couple of years!), and so this page serves as a general introduction. At the end you will find further reading recommendations that you can consult if you'd like to learn more.

## A rough history of single-cell technologies

The first measurement of RNA from single cells was described in Eberwine et al. [(1992)](https://www.pnas.org/content/89/7/3010)

<figure>
  <img src="/media/learning/timeline.png">
  <figcaption>
    <h3>
      Multimodal scRNA and scATAC from cell nuclei
    </h3>
    <p style="font-size: medium;">
      In this task, the goal is to take one modality (ATAC or RNA) and predict the other modality (RNA or Protein) for all features in each cell. Performance is measured using Mean Square Error.
    </p>
  </figcaption>
</figure>

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
