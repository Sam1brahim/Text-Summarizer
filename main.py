from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import DataTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline



from textSummarizer.logging import logger

STAGE_NAME = ">>>>>>>>>>>> Data Ingestion Stage"

try:
    logger.info("Stage {STAGE_NAME} started".format(STAGE_NAME=STAGE_NAME))
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info("Stage {STAGE_NAME} completed".format(STAGE_NAME=STAGE_NAME))
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e

STAGE_NAME = ">>>>>>>>>>>> Data Validation Stage"

try:
    logger.info("Stage {STAGE_NAME} started".format(STAGE_NAME=STAGE_NAME))
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.main()
    logger.info("Stage {STAGE_NAME} completed".format(STAGE_NAME=STAGE_NAME))
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e

STAGE_NAME = " >>>>>>>>>>>> Data Transformation Stage"

try:
    logger.info("Stage {STAGE_NAME} started".format(STAGE_NAME=STAGE_NAME))
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info("Stage {STAGE_NAME} completed".format(STAGE_NAME=STAGE_NAME))
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e

STAGE_NAME = " >>>>>>>>>>>> Model Training Stage"

try:
    logger.info("Stage {STAGE_NAME} started".format(STAGE_NAME=STAGE_NAME))
    data_transformation_pipeline = DataTrainerTrainingPipeline()
    data_transformation_pipeline.main()
    logger.info("Stage {STAGE_NAME} completed".format(STAGE_NAME=STAGE_NAME))
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e

STAGE_NAME = " >>>>>>>>>>>> Model Evaluation Stage"

try:
    logger.info("Stage {STAGE_NAME} started".format(STAGE_NAME=STAGE_NAME))
    data_transformation_pipeline = ModelEvaluationPipeline()
    data_transformation_pipeline.main()
    logger.info("Stage {STAGE_NAME} completed".format(STAGE_NAME=STAGE_NAME))
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e