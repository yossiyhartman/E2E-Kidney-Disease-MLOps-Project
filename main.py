from KidneyDiseasePrediction import logger
from KidneyDiseasePrediction.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_training_pipeline.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x\n\n")

except Exception as e:
    logger.exception(e)
    raise e
