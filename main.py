from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME="Data Integration stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<\n\nx========x")
        obj=DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx========x")
except Exception as e:
        logger.exception(e)
        raise e
