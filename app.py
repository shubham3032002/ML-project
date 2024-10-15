from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation

import sys


if __name__ == '__main__':
    logging.info("logger working")
    
    
    
    try:
        # # data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion()
        # data_ingestion.initiate_data_ingestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()
        
        # data_tranformation_config=DataTransformationConfig()
        data_tranformation= DataTransformation()
        
        data_tranformation.initiate_data_transormation(train_data_path,test_data_path)
        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)

    