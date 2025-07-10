import os
import json
import yaml
import base64
import joblib

from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
from KidneyDiseasePrediction import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)

    except FileNotFoundError as e:
        raise e

    except BoxValueError as e:
        raise e

    except Exception as e:
        raise e


@ensure_annotations
def create_directories(paths: list, verbose: bool = True):

    for path in paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created at {path}")


@ensure_annotations
def save_json(path: Path, data: dict):

    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"JSON file saved at {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:

    with open(path, "r") as f:
        data = json.load(f)

    logger.info(f"JSON file loaded from {path}")
    return ConfigBox(data)


@ensure_annotations
def save_bin(Path: Path, data):

    joblib.dump(data, Path)
    logger.info(f"Binary file saved at {Path}")


@ensure_annotations
def load_bin(path: Path):

    data = joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:

    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"


@ensure_annotations
def decode_image(imgstring: str, filename: str):

    decoded_bytes = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(decoded_bytes)


@ensure_annotations
def encode_image(filename: str) -> bytes:
    with open(filename, "rb") as f:
        return base64.b64encode(f.read())
