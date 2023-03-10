from pathlib import Path
import json

print("Fetch template", flush=True)
benchmark_dir = Path("results/")

task_info_files = benchmark_dir.glob("*/data/task_info.json")

# task_info_file = list(task_info_files)[0]
for task_info_file in task_info_files:
    print(f"Reading {task_info_file}", flush=True)
    task_info = json.loads(task_info_file.read_text())
    task_id = task_info.get("task_id", "task_id_missing")
    task_name = task_info.get("task_name", "<Name missing>")
    task_summary = task_info.get("task_summary", "<Summary missing>")

    content = f"""\
---
title: "{task_name}"
subtitle: "{task_summary}"
engine: knitr
image: featured.png
page-layout: full
---

```{{r}}
#| include: false
params <- list(data_dir = "results/{task_id}/data")
params <- list(data_dir = "./data")
```

{{{{< include ../_blocks/_task_template.qmd >}}}}
"""

    index_qmd = task_info_file.parent.parent / "index.qmd"
    print(f"Write to {index_qmd}", flush=True)
    with index_qmd.open("w", encoding ="utf-8") as f:
        f.write(content)
