"""Generate new data formats from old data formats."""
import re
import json
from pathlib import Path
import numpy as np
import openproblems as op

COMMIT_SHA = "a49ae996dc5f34402b1fa5cab9b3a3936126a413"
EXPECTED_TASK_FIELDS = ["task_id", "commit_sha", "task_name", "task_summary", "task_description"]
EXPECTED_METHOD_FIELDS = ["task_id", "commit_sha", "method_id", "method_name", "method_description", "paper_reference", "is_baseline"]
EXPECTED_METRIC_FIELDS = ["task_id", "commit_sha", "metric_id", "metric_name", "metric_description", "paper_reference", "maximize"]
EXPECTED_DATASET_FIELDS = ["task_id", "commit_sha", "dataset_id", "dataset_name", "dataset_description", "data_reference"]

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

def create_task_info(task_id, task):
    """Create a task info dict."""
    empty_info = {field: None for field in EXPECTED_TASK_FIELDS}
    info = {
        "task_id": task_id,
        "commit_sha": COMMIT_SHA,
        "task_name": task._task_name,
        "task_summary": task._task_summary,
    }
    return empty_info | info

def create_method_info(task_id, task):
    """Create a list of method info dicts."""
    out = []
    empty_info = {field: None for field in EXPECTED_METHOD_FIELDS}
    for fun in task.METHODS:
        info = {
            "task_id": task_id,
            "commit_sha": COMMIT_SHA,
            "method_id": fun.__name__,
        }
        out.append(empty_info | info | fun.metadata)
    return out

def create_metric_info(task_id, task):
    """Create a list of metric info dicts."""
    out = []
    empty_info = {field: None for field in EXPECTED_METRIC_FIELDS}
    for fun in task.METRICS:
        info = {
            "task_id": task_id,
            "commit_sha": COMMIT_SHA,
            "metric_id": fun.__name__,
        }
        out.append(empty_info | info | fun.metadata)
    return out

def create_dataset_info(task_id, task):
    """Create a list of dataset info dicts."""
    out = []
    empty_info = {field: None for field in EXPECTED_DATASET_FIELDS}
    for fun in task.DATASETS:
        info = {
            "task_id": task_id,
            "commit_sha": COMMIT_SHA,
            "dataset_id": fun.__name__,
        }
        out.append(empty_info | info | fun.metadata)
    return out

def create_results(task_id, path):
    """Create a list of result dicts."""
    out = []
    for json_path in path.glob("*.raw.json"):
        print(f"  Processing {json_path}")
        data = json.loads(json_path.read_text())
        dataset_id = json_path.name.removesuffix(".raw.json")

        def fix_values(metric_result):
            if np.isnan(metric_result):
                return "NaN"
            if np.isneginf(metric_result):
                return "-Inf"
            if np.isinf(metric_result):
                return "Inf"
            return metric_result
        def fix_values_scaled(metric_result):
            if np.isnan(metric_result) or np.isinf(metric_result):
                return 0
            return metric_result
        for method_id, li in data.items():
            raw = { k: fix_values(v) for k, v in li["metrics_raw"].items() }
            scaled = { k: fix_values_scaled(v) for k, v in li["metrics"].items() }
            resources = {
                "duration_sec": parse_time_to_sec(li["duration"]),
                "cpu_pct": float(li["%cpu"].replace("%", "")),
                "peak_memory_mb": parse_size_to_mb(li["peak_rss"]),
                "disk_read_mb": parse_size_to_mb(li["rchar"]),
                "disk_write_mb": parse_size_to_mb(li["wchar"]),
            }
            result = {
                "task_id": task_id,
                "commit_sha": COMMIT_SHA,
                "method_id": method_id,
                "dataset_id": dataset_id,
                "submission_time": li["submit"],
                "code_version": li["code_version"],
                "resources": resources,
                "metric_values": raw,
                "scaled_scores": scaled,
                "mean_score": np.array(list(scaled.values())).mean()
            }
            out.append(result)
    return out

def main():
    # source_path = Path("_results_v1_raw")
    dest_path = Path("results")

    for task in op.TASKS:
        task_id = re.sub(".*\\.", "", task.__name__)
        # task_source_path = source_path / task_id
        task_dest_path = dest_path / task_id / "data"

        # create dir if need be
        if not task_dest_path.exists():
            task_dest_path.mkdir(parents=True)

        print(f"Processing task {task_id}", flush=True)

        # create info objects
        task_info = create_task_info(task_id, task)
        method_info = create_method_info(task_id, task)
        metric_info = create_metric_info(task_id, task)
        dataset_info = create_dataset_info(task_id, task)
        # results = create_results(task_id, task_source_path)

        # write data to files
        with open(task_dest_path / "task_info.json", "w", encoding="utf8") as file:
            dump_json(task_info, file)
        with open(task_dest_path / "method_info.json", "w", encoding="utf8") as file:
            dump_json(method_info, file)
        with open(task_dest_path / "metric_info.json", "w", encoding="utf8") as file:
            dump_json(metric_info, file)
        with open(task_dest_path / "dataset_info.json", "w", encoding="utf8") as file:
            dump_json(dataset_info, file)
        # with open(task_dest_path / "results.json", "w", encoding="utf8") as file:
        #     dump_json(results, file)

if __name__ == "__main__":
    main()
