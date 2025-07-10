from KidneyDiseasePrediction.config.config import ConfigManager
from KidneyDiseasePrediction.components.training import Training
from KidneyDiseasePrediction import logger

STAGE_NAME = "Model Training"


class ModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config_manager = ConfigManager()
        model_training_config = config_manager.get_training_config()
        model_training = Training(model_training_config)
        model_training.get_base_model()
        model_training.train_valid_generators()
        model_training.train_model()


if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x\n\n")

    except Exception as e:
        logger.exception(e)
        raise e
