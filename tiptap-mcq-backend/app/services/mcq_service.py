import json
import os
import logging
from ..config import MCQ_DATA_DUMP_FILE

class MultipleChoiceQuestionService:

    @staticmethod
    def save_mcq_data_to_json(data):
        try:
            filename = MCQ_DATA_DUMP_FILE
            
            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    existing_data = json.load(file)
                    if existing_data is None:
                        existing_data = []
            else:
                existing_data = []
            existing_data.append(data)
            
            
            with open(filename, 'w') as file:
                json.dump(existing_data, file, indent=4)
                
            return existing_data
        
        except Exception as e:
            return str(e)
            
