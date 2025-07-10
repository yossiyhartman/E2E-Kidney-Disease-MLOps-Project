from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class BaseModelConfig:
    root_dir: Path
    base_model_path: Path
    modified_base_model_path: Path
    params_learning_rate: float
    params_weights: str
    params_classes: int
    params_freeze_ratio: float
