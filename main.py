from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info("Stage {STAGE_NAME} started".format(STAGE_NAME=STAGE_NAME))
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.main()
    logger.info("Stage {STAGE_NAME} completed".format(STAGE_NAME=STAGE_NAME))
except Exception as e:
    logger.error(f"Stage {STAGE_NAME} failed: {e}")
    raise e