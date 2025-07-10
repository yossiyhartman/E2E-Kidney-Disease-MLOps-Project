import os
from pathlib import Path
from KidneyDiseasePrediction.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from KidneyDiseasePrediction.utils.common import read_yaml, create_directories
from KidneyDiseasePrediction.entity.config_entity import DataIngestionConfig, BaseModelConfig, ModelTrainingConfig


class ConfigManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, params_file_path=PARAMS_FILE_PATH):

        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        create_directories([self.config.data_ingestion.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=self.config.data_ingestion.root_dir,
            source_url=self.config.data_ingestion.source_url,
            local_data_file=self.config.data_ingestion.local_data_file,
            unzip_dir=self.config.data_ingestion.unzip_dir,
        )

        return data_ingestion_config

    def get_base_model_config(self) -> BaseModelConfig:

        create_directories([self.config.base_model.root_dir])

        base_model_config = BaseModelConfig(
            root_dir=self.config.base_model.root_dir,
            base_model_path=self.config.base_model.base_model_path,
            modified_base_model_path=self.config.base_model.modified_base_model_path,
            params_learning_rate=self.params.LEARNING_RATE,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            params_freeze_ratio=self.params.FREEZE_RATIO,
        )

        return base_model_config

    def get_training_config(self) -> ModelTrainingConfig:

        create_directories([self.config.model_training.root_dir])

        model_training_config = ModelTrainingConfig(
            root_dir=self.config.model_training.root_dir,
            modified_base_model_path=self.config.base_model.modified_base_model_path,
            training_data=Path(os.path.join(self.config.data_ingestion.unzip_dir, "dataset")),
            trained_model_path=self.config.model_training.trained_model_path,
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_augmentation=self.params.AUGMENTATION,
        )

        return model_training_config
