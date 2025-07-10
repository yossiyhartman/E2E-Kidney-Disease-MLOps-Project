from KidneyDiseasePrediction import logger
from KidneyDiseasePrediction.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from KidneyDiseasePrediction.pipeline.stage02_base_model import BaseModelPipeline


try:
    STAGE_NAME = "Data Ingestion"
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e


try:
    STAGE_NAME = "Get Base Model"
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    base_model_pipeline = BaseModelPipeline()
    base_model_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x\n\n")
except Exception as e:
    logger.exception(e)
    raise e
