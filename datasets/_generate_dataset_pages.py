from pathlib import Path
import json

print("Fetch template", flush=True)
dataset_dir = Path("datasets/")

dataset_meta_files = dataset_dir.glob("*/*/meta.json")

for dataset_file in dataset_meta_files:
    print(f"Reading {dataset_file}", flush=True)
    dataset_info = json.loads(dataset_file.read_text())
    info_uns = dataset_info.get("uns")
    dataset_name = info_uns.get("dataset_name", "<Name missing>")
    dataset_summary = info_uns.get("dataset_summary", "<Summary missing>")
    dataset_description = info_uns.get("dataset_description", "<Description missing>")
    dataset_id = info_uns.get("dataset_id", "<ID missing>")
    dataset_ref = info_uns.get("dataset_reference", "<Ref missing>")

    dataset_loader = dataset_id.split("/")[0]

    content = f"""\
---
title: "{dataset_name}"
subtitle: "{dataset_summary}"
description: "{dataset_description}"
categories: ["{dataset_loader}"]
title-block-banner: true
title-block-banner-color: white
css: ../../../events/events.css
toc: false
engine: knitr
citation-location: document
template-partials:
  - ../../_include/title-metadata.html
dataset-id: {dataset_id}
dataset-ref: "@{dataset_ref}"
---

```{{r}}
#| include: false
params <- list(data_file = "./meta.json")
```

{{{{< include ../../_include/_task_template.qmd >}}}}
"""

    index_qmd = dataset_file.parent / "index.qmd"
    print(f"Write to {index_qmd}", flush=True)
    with index_qmd.open("w", encoding ="utf-8") as f:
        f.write(content)
