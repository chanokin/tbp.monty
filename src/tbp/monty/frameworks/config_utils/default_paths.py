from pathlib import Path
# # todo integrate to a global logging
# from warnings import warn

def get_base_dir():
    _path = Path.home() / "monty_experiments"
    # warn(f"Using default base path {_path}")
    _path.mkdir(exist_ok=True)
    return _path

def get_log_dir():
    _path = get_base_dir() /  "logs"
    # warn(f"Using default logs path {_path}")
    _path.mkdir(exist_ok=True)
    return _path

def get_data_dir():
    _path = get_base_dir() / "data"
    # warn(f"Using default data path {_path}")
    _path.mkdir(exist_ok=True)
    return _path
