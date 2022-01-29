+++
widget = "blank"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 10  # Order that this section will appear.

title = "Winners"
subtitle = ""

[design]
  # Choose how many columns the section has. Valid values: 1 or 2.
  columns = "2"

[design.background]
  # Text color (true=light or false=dark).
  text_color_light = false
  color = "white"

[design.spacing]
  # Customize the section spacing. Order is top, right, bottom, left.
  padding = ["20px", "0", "20px", "0"]

[advanced]
 # Custom CSS.
 css_style = ""

 # CSS class.
 css_class = ""
+++

We're proud to announce the winners of our 2021 NeurIPS competition!

## **Task 1 - Modality Prediction**
_Given one modality, predict the other._
### GEX→ATAC: Living Systems Lab
**KAUST, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/predict_modality/methods/LS_lab)**   
Aidyn Ubingazhibov, Sumeer Khan, Robert Lehman, Xabier Martinez De Morentin, Minxing Pang, David Gomez-Cabrero, Narsis Kiani, Jesper Tegner

### ATAC→GEX: Cajal
**Francis Crick Institute, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/predict_modality/methods/cajal)**  
Anna Laddach, Roman Laddach, Michael Shapiro

### GEX→ADT: Dengkw
**University of Michigan, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/predict_modality/methods/Guanlab-dengkw)**  
Kaiwen Deng

### ADT→GEX: Novel
**Novel Software Systems, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/predict_modality/methods/novel)**   
Nikolay	Russkikh, Gleb	Ryazantsev, Igor	I

### Overall: DANCE (pending validation)
**Michigan State University, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/predict_modality/methods/DANCE)**  
Hongzhi Wen, Jiayuan	Ding, Wei	Jin, Xiaoyan	Li, Zhaoheng	Li, Yiqi	Wang, Haoyu	Han, Yanyi	Ding, Xiaochun	Ni, Yu	Lei, Yuying	Xie, Jiliang	Tang

## **Task 2 - Match Modality**
_Given collections of cells in each modality, match profiles that originated from the same cell._

### Winner in all categories: CLUE  
**Peking University, University of Washington, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/match_modality/methods/clue)**  
Zhi-Jie	Cao, Xinming	Tu, Chen-Rui	Xia

## **Task 3 - Joint Embedding**
_Learn a low dimensional embedding of both modalities that preserves biology and removes batch effects._

### Multiome, pre-trained & CITE, pre-trained: Amateur (pending validation)
**Stanford University, Tsinghua University, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/joint_embedding/methods/jae)**  
Qiao	Liu, Wanwen	Zeng, Chencheng	Xu

### Multiome, online: Living Systems Lab
**KAUST, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/joint_embedding/methods/lsl_ae)**  
Sumeer	Khan, Robert 	Lehman, Xabier Martinez	De Morentin, Minxing	Pang, Aidyn	Ubingazhibov, David	Gomez-Cabrero, Narsis	Kiani, Jesper	Tegner

### CITE, online: Dengkw
**University of Michigan, [code](https://github.com/openproblems-bio/neurips2021_multimodal_topmethods/tree/main/src/joint_embedding/methods/Guanlab-dengkw)**  
Kaiwen Deng
