from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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

STAGE_NAME="Data Transformation stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<\n\nx========x")
        obj=DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Model Trainer stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<\n\nx========x")
        obj=ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Model Evaluation stage"
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<\n\nx========x")
        obj=ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx========x")
except Exception as e:
        logger.exception(e)
        raise e