import openproblems as op
import json
from pathlib import Path
import re

for task in op.TASKS:
  # task_id = "label_projection"
  # task = getattr(op.tasks, task_id)
  
  task_id = re.sub(".*\.", "", task.__name__)
  path = Path("results") / task_id

  # create method info json
  method_info = [ 
    { "task_id": task_id, "method_id": fun.__name__ } | fun.metadata
    for fun in task.METHODS
  ]
  with open(path / "method_info.json", "w") as file:
    file.write(json.dumps(method_info, indent=2))

  # create metric info json
  metric_info = [ 
    { "task_id": task_id, "metric_id": fun.__name__ } | fun.metadata
    for fun in task.METRICS
  ]
  with open(path / "metric_info.json", "w") as file:
    file.write(json.dumps(metric_info, indent=2))

  # create dataset info json
  dataset_info = [ 
    { "task_id": task_id, "dataset_id": fun.__name__ } | fun.metadata
    for fun in task.DATASETS
  ]
  with open(path / "dataset_info.json", "w") as file:
    file.write(json.dumps(dataset_info, indent=2))