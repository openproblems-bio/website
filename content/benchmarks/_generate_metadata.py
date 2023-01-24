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

def create_quality_control(task_info, dataset_info, method_info, metric_info, results):
    """Quality control to detect anomalies in the results."""
    task_id = task_info["task_id"]

    result_qc = []

    def add_qc(
        category: str,
        name: str,
        value,
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
    
    def percent_missing(list_of_dicts, field):
        are_missing = [0.0 if field in item and item[field] is not None else 1.0 for item in list_of_dicts]
        return np.mean(are_missing)
    
    # check task_info
    for field in EXPECTED_TASK_FIELDS:
        pct_missing = percent_missing([task_info], field)
        add_qc(
            "Task info",
            f"Pct '{field}' missing",
            pct_missing,
            3.0 if pct_missing > 0 else 0.0,
            "percent_missing([task_info], field)",
            f"Task metadata field '{field}' should be defined\n"
            f"  Task id: {task_id}\n"
            f"  Field: {field}\n"
        )
    
    # check method_info
    for field in EXPECTED_METHOD_FIELDS:
        pct_missing = percent_missing(method_info, field)
        add_qc(
            "Method info",
            f"Pct '{field}' missing",
            pct_missing,
            3.0 if pct_missing > 0 else 0.0,
            "percent_missing(method_info, field)",
            f"Method metadata field '{field}' should be defined\n"
            f"  Task id: {task_id}\n"
            f"  Field: {field}\n"
        )

    # check metric_info
    for field in EXPECTED_METRIC_FIELDS:
        pct_missing = percent_missing(metric_info, field)
        add_qc(
            "Metric info",
            f"Pct '{field}' missing",
            pct_missing,
            3.0 if pct_missing > 0 else 0.0,
            "percent_missing(metric_info, field)",
            f"Metric metadata field '{field}' should be defined\n"
            f"  Task id: {task_id}\n"
            f"  Field: {field}\n"
        )

    # check dataset_info
    for field in EXPECTED_DATASET_FIELDS:
        pct_missing = percent_missing(dataset_info, field)
        add_qc(
            "Dataset info",
            f"Pct '{field}' missing",
            pct_missing,
            3.0 if pct_missing > 0 else 0.0,
            "percent_missing(dataset_info, field)",
            f"Dataset metadata field '{field}' should be defined\n"
            f"  Task id: {task_id}\n"
            f"  Field: {field}\n"
        )

    # turn results into long format for easier processing
    results_long = [
        {
            "task_id": x["task_id"],
            "method_id": x["method_id"],
            "dataset_id": x["dataset_id"],
            "metric_id": metric["metric_id"],
            "metric_value" : x["metric_values"][metric["metric_id"]],
            "scaled_score" : x["scaled_scores"].get(metric["metric_id"]),
        }
        for metric in metric_info
        for x in results
    ]

    # check percentage missing
    pct_missing = 1 - len(results_long) / (len(method_info) * len(metric_info) * len(dataset_info))
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
            if res["metric_id"] == metric_id
            and res["metric_value"] is not None
            and np.isreal(res["metric_value"])
        ]
        pct_missing = 1 - len(values) / len(dataset_info) / len(method_info)

        add_qc(
            "Raw results",
            f"Metric '{metric_id}' %missing",
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
            if res["method_id"] == method_id
            and res["metric_value"] is not None
            and np.isreal(res["metric_value"])
        ]
        pct_missing = 1 - len(values) / len(dataset_info) / len(metric_info)

        add_qc(
            "Raw results",
            f"Method '{method_id}' %missing",
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
            if res["dataset_id"] == dataset_id
            and res["metric_value"] is not None
            and np.isreal(res["metric_value"])
        ]
        pct_missing = 1 - len(values) / len(metric_info) / len(method_info)

        add_qc(
            "Raw results",
            f"Dataset '{dataset_id}' %missing",
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
                res["scaled_score"]
                for res in results_long
                if res["metric_id"] == metric_id
                and res["method_id"] == method_id
                and res["scaled_score"] is not None
                and np.isreal(res["scaled_score"])
            ]

            if len(scores) >= 1:
                worst_score = np.min(scores).item()
                best_score = np.max(scores).item()

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

def main():
    source_path = Path("_results_v1_raw")
    dest_path = Path("content/benchmarks")

    for task in op.TASKS:
        task_id = re.sub(".*\\.", "", task.__name__)
        task_source_path = source_path / task_id
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
        results = create_results(task_id, task_source_path)
        quality_control = create_quality_control(task_info, dataset_info, method_info, metric_info, results)

        # write data to files
        with open(task_dest_path / "task_info.json", "w", encoding="utf8") as file:
            dump_json(task_info, file)
        with open(task_dest_path / "method_info.json", "w", encoding="utf8") as file:
            dump_json(method_info, file)
        with open(task_dest_path / "metric_info.json", "w", encoding="utf8") as file:
            dump_json(metric_info, file)
        with open(task_dest_path / "dataset_info.json", "w", encoding="utf8") as file:
            dump_json(dataset_info, file)
        with open(task_dest_path / "results.json", "w", encoding="utf8") as file:
            dump_json(results, file)
        with open(task_dest_path / "quality_control.json", "w", encoding="utf8") as file:
            dump_json(quality_control[:306], file)

if __name__ == "__main__":
    main()
