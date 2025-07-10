import os
import zipfile
import gdown

from KidneyDiseasePrediction import logger
from KidneyDiseasePrediction.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        try:

            dataset_url = self.config.source_url
            zip_download_url = self.config.local_data_file

            # why not also use the config path ?
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading dataset from {dataset_url} to {zip_download_url}")

            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?export=download&id="
            gdown.download(f"{prefix}{file_id}", zip_download_url)

            logger.info(f"Downloaded dataset to {zip_download_url}")

        except Exception as e:
            raise e

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(unzip_path)
