from typing import Any, List, Optional, Union
import openproblems as op
import json
from pathlib import Path
import re
import numpy as np

def dump_json(obj, fp):
  """Dump to JSON in a numpy-safe fashion."""
  json.dump(
    obj,
    fp,
    indent=4,
    sort_keys=False,
    separators=(", ", ": "),
    ensure_ascii=False,
  )

size_units = {"B": 1, "KB": 10**3, "MB": 10**6, "GB": 10**9, "TB": 10**12}

def parse_size_to_mb(size):
  """Convert a file size to an integer in GB.
  Example
  -------
  >>> parse_size_to_gb("1000 MB")
  1
  """
  number, unit = [string.strip() for string in size.split()]
  return int(float(number) * size_units[unit]) / size_units["MB"]

time_units = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

def parse_time_to_sec(time):
  """Convert a duration to an integer in seconds.
  Example
  -------
  >>> parse_time_to_min("2m 30s")
  2.5
  """
  if " " in time:
    return sum([parse_time_to_sec(t) for t in time.split(" ")])
  time = time.strip()
  for unit, value in time_units.items():
    if time.endswith(unit):
      number = float(time.replace(unit, ""))
      return number * value / time_units["s"]

def create_method_info(task_id, task):
  """Create a list of method info dicts."""
  for fun in task.METHODS:
    yield { "task_id": task_id, "method_id": fun.__name__ } | fun.metadata

def create_metric_info(task_id, task):
  """Create a list of metric info dicts."""
  for fun in task.METRICS:
    yield { "task_id": task_id, "metric_id": fun.__name__ } | fun.metadata

def create_dataset_info(task_id, task):
  """Create a list of dataset info dicts."""
  for fun in task.DATASETS:
    yield { "task_id": task_id, "dataset_id": fun.__name__ } | fun.metadata

def create_results(task_id, path):
  """Create a list of result dicts."""
  for json_path in path.glob("*.raw.json"):
    data = json.loads(json_path.read_text())
    dataset_id = json_path.name.removesuffix(".raw.json")
    
    def fix_values(metric_result):
      if np.isnan(metric_result):
        return "NaN"
      elif np.isneginf(metric_result):
        return "-Inf"
      elif np.isinf(metric_result):
        return "Inf"
      else:
        return metric_result
    def fix_values_scaled(metric_result):
      if np.isnan(metric_result) or np.isinf(metric_result):
        return 0.0
      else:
        return metric_result
    
    for method_id, li in data.items():
      meta = {"task_id": task_id, "method_id": method_id, "dataset_id": dataset_id}
      raw = { k: fix_values(v) for k, v in li["metrics_raw"].items() }
      scaled = { k + "_scaled": fix_values_scaled(v) for k, v in li["metrics"].items() }
      
      exec = {
        "submission_time": li["submit"],
        "duration_sec": parse_time_to_sec(li["duration"]),
        "cpu_pct": float(li["%cpu"].replace("%", "")),
        "peak_memory_mb": parse_size_to_mb(li["peak_rss"]),
        "disk_read_mb": parse_size_to_mb(li["rchar"]),
        "disk_write_mb": parse_size_to_mb(li["wchar"]),
        "code_version": li["code_version"]
      }

      yield meta | exec | raw | scaled

def create_quality_control(task_id, dataset_info, method_info, metric_info, results):
  results_long = [
    {
      "task_id": x["task_id"],
      "method_id": x["method_id"],
      "dataset_id": x["dataset_id"],
      "metric_id": metric["metric_id"],
      "value" : x[metric["metric_id"]],
      "score" : x.get(metric["metric_id"] + "_scaled")
    }
    for metric in metric_info
    for x in results
  ]

  result_qc = []
  # pd.DataFrame(result_qc)

  def add_qc(
    category: str,
    name: str,
    value: Any,
    severity_value: float,
    code: str,
    message: str,
  ) -> None:
    "Add an entry to the result qc"
    if severity_value <= 1:
      severity = 0
    elif severity_value <= 2:
      severity = 1
    elif severity_value <= 3:
      severity = 2
    else:
      severity = 3
    result_qc.append({
      "task_id": task_id,
      "category": category,
      "name": name,
      "value": value,
      "severity": severity,
      "severity_value": severity_value,
      "code": code,
      "message": message
    })

  pct_missing = 1 - len(results) / len(method_info) * len(metric_info) * len(dataset_info)
  add_qc(
    "Raw data",
    "Number of results",
    len(results),
    pct_missing / .1,
    "len(results) == len(method_info) * len(metric_info) * len(dataset_info)",
    f"Number of results should be equal to #methods × #metrics × #datasets.\n"
    f"  Task id: {task_id}\n"
    f"  Number of results: {len(results)}\n"
    f"  Number of methods: {len(method_info)}\n"
    f"  Number of metrics: {len(metric_info)}\n"
    f"  Number of datasets: {len(dataset_info)}\n"
  )

  # QC per metric
  for metric in metric_info:
    metric_id = metric["metric_id"]
    values = [ 
      res
      for res in results_long
      if res["metric_id"] == metric_id and res["value"] and np.isreal(res["value"])
    ]
    pct_missing = 1 - len(values) / len(dataset_info) / len(method_info)
    
    add_qc(
      "Raw results",
      f"Metric {metric_id} %missing",
      pct_missing,
      pct_missing / .1,
      "pct_missing <= .1",
      f"Percentage of missing results should be less than 10%.\n"
      f"  Task id: {task_id}\n"
      f"  Metric id: {metric_id}\n"
      f"  Percentage missing: {pct_missing*100:.0f}%\n"
    )

  # QC per method
  for method in method_info:
    method_id = method["method_id"]
    values = [ 
      res
      for res in results_long
      if res["method_id"] == method_id and res["value"] and np.isreal(res["value"])
    ]
    pct_missing = 1 - len(values) / len(dataset_info) / len(metric_info)
    
    add_qc(
      "Raw results",
      f"Method {method_id} %missing",
      pct_missing,
      pct_missing / .1,
      "pct_missing <= .1",
      f"Percentage of missing results should be less than 10%.\n"
      f"  Task id: {task_id}\n"
      f"  method id: {method_id}\n"
      f"  Percentage missing: {pct_missing*100:.0f}%\n"
    )

  # QC per dataset
  for dataset in dataset_info:
    dataset_id = dataset["dataset_id"]
    values = [ 
      res
      for res in results_long
      if res["dataset_id"] == dataset_id and res["value"] and np.isreal(res["value"])
    ]
    pct_missing = 1 - len(values) / len(metric_info) / len(method_info)
    
    add_qc(
      "Raw results",
      f"Dataset {dataset_id} %missing",
      pct_missing,
      pct_missing / .1,
      "pct_missing <= .1",
      f"Percentage of missing results should be less than 10%.\n"
      f"  Task id: {task_id}\n"
      f"  dataset id: {dataset_id}\n"
      f"  Percentage missing: {pct_missing*100:.0f}%\n"
    )


  # QC per metric and method
  for metric in metric_info:
    for method in method_info:
      metric_id = metric["metric_id"]
      method_id = method["method_id"]
      scores = [ 
        res["score"]
        for res in results_long
        if res["metric_id"] == metric_id 
        and res["method_id"] == method_id
        and res["score"]
        and np.isreal(res["score"])
      ]

      if (len(scores) >= 1):
        worst_score = np.min(scores)
        best_score = np.max(scores)
        
        add_qc(
          "Scaling",
          f"Worst score {method_id} {metric_id}",
          worst_score,
          worst_score / -1,
          "worst_score >= -1",
          f"Method {method_id} performs much worse than baselines.\n"
          f"  Task id: {task_id}\n"
          f"  Method id: {method_id}\n"
          f"  Metric id: {metric_id}\n"
          f"  Worst score: {worst_score}%\n"
        )
        
        add_qc(
          "Scaling",
          f"Best score {method_id} {metric_id}",
          best_score,
          best_score / 2,
          "best_score <= 2",
          f"Method {method_id} performs a lot better than baselines.\n"
          f"  Task id: {task_id}\n"
          f"  Method id: {method_id}\n"
          f"  Metric id: {metric_id}\n"
          f"  Best score: {best_score}%\n"
        )

  return result_qc

for task in op.TASKS:
  # task_id = "batch_integration_embed"
  # task = op.tasks._batch_integration.batch_integration_embed
  
  task_id = re.sub(".*\.", "", task.__name__)
  path = Path("results") / task_id

  print(f"Processing task {task_id}", flush=True)

  # create method info json
  method_info = list(create_method_info(task_id, task))
  with open(path / "method_info.json", "w") as file:
    dump_json(method_info, file)

  # create metric info json
  metric_info = list(create_metric_info(task_id, task))
  with open(path / "metric_info.json", "w") as file:
    dump_json(metric_info, file)

  # create dataset info json
  dataset_info = list(create_dataset_info(task_id, task))
  with open(path / "dataset_info.json", "w") as file:
    dump_json(dataset_info, file)
  
  # create results json
  results = list(create_results(task_id, path))
  with open(path / "results.json", "w") as file:
    dump_json(results, file)

  quality_control = create_quality_control(task_id, dataset_info, method_info, metric_info, results)
  with open(path / "quality_control.json", "w") as file:
    dump_json(quality_control, file)
  
