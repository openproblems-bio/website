from pathlib import Path
import os
import json

print("Fetch template", flush=True)
dataset_dir = Path("datasets/")

dataset_meta_files = dataset_dir.glob("*/*/*meta*.json")

parent_dirs = [Path(file).parent for file in dataset_meta_files]
parent_dirs = list(set(parent_dirs))

for dir in parent_dirs:
  meta_files = list(dir.glob("*meta*.json"))  
  print(f"Reading {meta_files[0]}", flush=True)
  dataset_info = json.loads(meta_files[0].read_text())
  info_uns = dataset_info.get("uns")
  dataset_name = info_uns.get("dataset_name", "<Name missing>")
  dataset_summary = info_uns.get("dataset_summary", "<Summary missing>")
  dataset_id = info_uns.get("dataset_id", "<ID missing>")
  dataset_ref = info_uns.get("dataset_reference", "<Ref missing>")

  dataset_loader = dataset_id.split("/")[0]
  str_files = [str(file.name) for file in meta_files]
  data_files=', '.join(f'"{file}"' for file in str_files)
  content = f"""\
---
title: "{dataset_name}"
subtitle: "{dataset_summary}"
categories: ["{dataset_loader}"]
title-block-banner: transparent
css: [../../../events/events.css, ../../datasets.css]
toc: false
engine: knitr
citation-location: document
template-partials:
  - ../../_include/title-metadata.html
dataset-id: {dataset_id}
dataset-ref: "@{dataset_ref}"
---

```{{=html}}
<img src="../../../images/heros/anndata_schema.png" alt="Anndata Schema" class="dataset_img">
```


```{{r}}
#| include: false
meta_files <- c({data_files})
params <- list(data_file = lapply(meta_files, function(x) paste0("./", x)))
```

{{{{< include ../../_include/_task_template.qmd >}}}}
"""

  index_qmd = dir / "index.qmd"
  print(f"Write to {index_qmd}", flush=True)
  with index_qmd.open("w", encoding ="utf-8") as f:
      f.write(content)
