import json
from pathlib import Path

def read_json_file(file_path):
    """
    Reads a JSON file and returns the data.
    
    Parameters:
    file_path (str or Path): The path to the JSON file.
    
    Returns:
    dict: The data from the JSON file.
    """
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"No such file: '{file_path}'")
    
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

dirs = [dir for dir in Path("results").iterdir() if dir.is_dir()]

exclude_dirs = ["_include", "perturbation_prediction", "spatially_variable_genes", "foundation_models"]

for dir in dirs:
    if dir.name in exclude_dirs:
        continue
    
    print(f"Processing directory: {dir}")

    data_path = dir.joinpath("data")

    # Transform the method_info.json file
    method_info_path = data_path.joinpath("method_info.json")
    method_info = read_json_file(method_info_path)
    for info in method_info:
        info["code_url"] = info["code_url"] + "/tree/v1.0.0/openproblems/tasks"
        info["implementation_url"] = info["implementation_url"].replace("main", "v1.0.0")
        info["code_version"] = "v1.0.0"
        info["image"] = "https://ghcr.io/openproblems-bio/" + info["image"]
    
    
    # Read the task_info.json file
