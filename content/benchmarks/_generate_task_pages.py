from pathlib import Path
import json
import subprocess

print("Fetch template", flush=True)
benchmark_dir = Path("content/benchmarks/")
template_qmd = benchmark_dir / "_task_template.qmd"
template = template_qmd.read_text()

task_info_files = benchmark_dir.glob("*/data/task_info.json")

# task_info_file = list(task_info_files)[0]
for task_info_file in task_info_files:
    print(f"Reading {task_info_file}", flush=True)
    task_info = json.loads(task_info_file.read_text())
    task_name = task_info.get("task_name", "<Name missing>")
    task_summary = task_info.get("task_summary", "<Summary missing>")

    content = f"""\
---
title: "{task_name}"
summary: "{task_summary}"
bibliography: "../../../static/bibliography/main.bib"
---

{template}
"""

    index_qmd = task_info_file.parent.parent / "index.qmd"
    print(f"Write to {index_qmd}", flush=True)
    with index_qmd.open("w", encoding ="utf-8") as f:
        f.write(content)

    print(f"Rendering {index_qmd}", flush=True)
    subprocess.run(["quarto", "render", str(index_qmd), "--to", "hugo-md"])
