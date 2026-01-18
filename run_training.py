from src.components.data_injection import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging
from src.exception import CustomException
import sys
def run_training_pipeline():
    try:
        logging.info("Starting data ingestion...")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed.")

        logging.info("Starting data transformation...")
        data_transformation = DataTransformation()  
        train_array, test_array, _ = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path )
        logging.info("Data transformation completed.")  
        logging.info("Starting model training...")
        model_trainer = ModelTrainer() 
        model_trainer.initiate_model_trainer(train_array, test_array)
        logging.info("Model training completed.")
    except Exception as e:
        logging.info("Exception occurred in training pipeline")
        raise CustomException(e, sys)