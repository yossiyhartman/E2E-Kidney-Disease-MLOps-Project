from pathlib import Path
from KidneyDiseasePrediction.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from KidneyDiseasePrediction.utils.common import read_yaml, create_directories
from KidneyDiseasePrediction.entity.config_entity import DataIngestionConfig, BaseModelConfig


class ConfigManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_base_model_config(self) -> BaseModelConfig:

        config = self.config.base_model

        create_directories([config.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            modified_base_model_path=config.modified_base_model_path,
            params_learning_rate=self.params.LEARNING_RATE,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            params_freeze_ratio=self.params.FREEZE_RATIO,
        )

        return base_model_config
