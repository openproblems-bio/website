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
    
    
    # Read the task_info.json file
