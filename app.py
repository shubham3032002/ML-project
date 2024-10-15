from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_transformation import DataTransformationConfig,DataTransformation
from src.mlproject.components.model_trainer import ModelTrainnerconfig,ModelTrainner

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
        
        train_arr,test_arr,_= data_tranformation.initiate_data_transormation(train_data_path,test_data_path)
        
        
    
        model_trainer=ModelTrainner()
        # logging.info(f"r2 score is")
        print(model_trainer.initate_model_trainer(train_arr,test_arr))
        
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e,sys)

    