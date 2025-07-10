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


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    modified_base_model_path: Path
    training_data: Path
    trained_model_path: Path
    params_epochs: int
    params_batch_size: int
    params_learning_rate: float
    params_augmentation: bool
