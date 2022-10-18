+++
widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 10  # Order that this section will appear.

title = "Summary"
subtitle = ""

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "2"

[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]

[advanced]
 # Custom CSS.
 css_style = ""

 # CSS class.
 css_class = ""
+++

Scaling from a dozen cells a decade ago to millions of cells today, single-cell measurement technologies are driving a revolution in the life sciences. Recent advances make it possible to measure multiple high-dimensional modalities (e.g. DNA accessibility, RNA, and proteins) simultaneously in the same cell. Such data provides, for the first time, a direct and comprehensive view into the layers of gene regulation that drive biological diversity and disease.

In [2021](https://openproblems.bio/neurips_2021), we organized the first single-cell analysis competition at NeurIPS bringing together 280 participants to compete on an atlas-scale dataset of human bone marrow cells from 12 donors generated across 4 sites globally. 

In this competition for [NeurIPS 2022](https://neurips.cc/Conferences/2022/CompetitionTrack), we are extending the challenge to drive innovation in modeling temporal single-cell data measured in multiple modalities at multiple time points. In this years competition, we generated a 300,000-cell time course dataset of CD34+ hematopoietic stem and progenitor cells (HSPC) from four human donors at five time points. HSPCs are stem cells that give rise to all other cells in the blood throughout adult life, and a 10-day time course captures important biology in CD34+ HSPCs.

In the test set, taken from an unseen later time point in the dataset, competitors will be provided with one modality and be tasked with predicting a paired modality measured in the same cell. The added challenge of this competition is that the test data will be from a later time point than any time point in the training data.

To read all the details and join to compete for $25,000 in prizes, [sign up on Kaggle!](https://www.kaggle.com/competitions/open-problems-multimodal/)
