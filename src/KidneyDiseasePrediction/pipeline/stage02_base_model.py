from KidneyDiseasePrediction.config.config import ConfigManager
from KidneyDiseasePrediction.components.base_model import BaseModel
from KidneyDiseasePrediction import logger

STAGE_NAME = "Get Base Model"


class BaseModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigManager()
        base_model_config = config.get_base_model_config()
        base_model = BaseModel(config=base_model_config)

        base_model.get_base_model()
        base_model.modify_base_model()


if __name__ == "__main__":

    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        base_model_pipeline = BaseModelPipeline()
        base_model_pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx===========x\n\n")

    except Exception as e:
        logger.exception(e)
        raise e
