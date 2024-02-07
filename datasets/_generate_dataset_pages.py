from pathlib import Path
import json

print("Fetch template", flush=True)
datasets_dir = Path("datasets/")

dataset_dirs = [state.parent.parent for state in datasets_dir.glob("**/data/state.yaml")]

for dir in dataset_dirs:
  print(f"Processing {dir}", flush=True)
  meta_files = list(dir.glob("data/*.json"))

  print(f"  Reading {meta_files[0]}", flush=True)
  dataset_info = json.loads(meta_files[0].read_text(encoding="UTF-8"))
  info_uns = dataset_info.get("uns")
  dataset_name = info_uns.get("dataset_name", "<Name missing>")
  dataset_summary = info_uns.get("dataset_summary", "<Summary missing>")
  dataset_id = info_uns.get("dataset_id", "<ID missing>")
  dataset_ref = info_uns.get("dataset_reference", "<Ref missing>")

  dataset_loader = dataset_id.split("/")[0]
  content = f"""\
---
title: "{dataset_name}"
subtitle: "{dataset_summary}"
categories: ["{dataset_loader}"]
title-block-banner: transparent
css: [/events/events.css, /datasets/datasets.css]
toc: false
engine: knitr
citation-location: document
template-partials:
  - /datasets/_include/title-metadata.html
dataset-id: {dataset_id}
dataset-ref: "@{dataset_ref}"
---

```{{r}}
#| include: false
params <- list(data_dir = "{dir}/data")
params <- list(data_dir = "./data")
```

{{{{< include /datasets/_include/_index_template.qmd >}}}}
"""

  index_qmd = dir / "index.qmd"
  print(f"  Writing to {index_qmd}", flush=True)
  with index_qmd.open("w", encoding ="utf-8") as f:
      f.write(content)
