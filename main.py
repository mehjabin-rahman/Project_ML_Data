from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME="Data Integration stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<\n\nx========x")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Data Validation stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<\n\nx========x")
        obj=DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx========x")
except Exception as e:
        logger.exception(e)
        raise e