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


for task in op.TASKS:
  # task_id = "batch_integration"
  # task = op.tasks._batch_integration.batch_integration_embed
  
  task_id = re.sub(".*\.", "", task.__name__)
  path = Path("results") / task_id

  # create method info json
  method_info = [ 
    { "task_id": task_id, "method_id": fun.__name__ } | fun.metadata
    for fun in task.METHODS
  ]
  with open(path / "method_info.json", "w") as file:
    dump_json(method_info, file)

  # create metric info json
  metric_info = [ 
    { "task_id": task_id, "metric_id": fun.__name__ } | fun.metadata
    for fun in task.METRICS
  ]
  with open(path / "metric_info.json", "w") as file:
    dump_json(metric_info, file)

  # create dataset info json
  dataset_info = [ 
    { "task_id": task_id, "dataset_id": fun.__name__ } | fun.metadata
    for fun in task.DATASETS
  ]
  with open(path / "dataset_info.json", "w") as file:
    dump_json(dataset_info, file)
  
  # create results json
  results = []
  # json_paths = list(path.glob("*.raw.json"))
  # json_path=json_paths[0]
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
    
    for method_id, li in data.items():
      meta = {"task_id": task_id, "method_id": method_id, "dataset_id": dataset_id}
      raw = { k: fix_values(v) for k, v in li["metrics_raw"].items() }
      # scaled = { k: fix_values(v) for k, v in li["metrics"].items() }
      
      exec = {
        "submission_time": li["submit"],
        "duration_sec": parse_time_to_sec(li["duration"]),
        "cpu_pct": float(li["%cpu"].replace("%", "")),
        "peak_memory_mb": parse_size_to_mb(li["peak_rss"]),
        "disk_read_mb": parse_size_to_mb(li["rchar"]),
        "disk_write_mb": parse_size_to_mb(li["wchar"]),
        "code_version": li["code_version"]
      }

      results.append(meta | raw | exec)
  with open(path / "results.json", "w") as file:
    dump_json(results, file)
