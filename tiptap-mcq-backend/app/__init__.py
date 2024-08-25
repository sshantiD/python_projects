from flask import Flask
from flask_cors import CORS
from .config import DevelopmentConfig, TestingConfig
import os
import logging
from transformers import pipeline  
from logging.handlers import RotatingFileHandler

summarization_pipeline = None

def create_app(config=DevelopmentConfig):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config)  
    CORS(app)
    global summarization_pipeline
    summarization_pipeline = pipeline("summarization", model="t5-small")


    from app.routes import bp
    app.register_blueprint(bp)
    configure_logging(app)
        
    return app

def configure_logging(app):
    log_level = app.config.get('LOG_LEVEL', 'INFO')
    log_file = app.config.get('LOG_FILE')

    logging.basicConfig(level=log_level)

    if log_file:
        file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=10)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        app.logger.addHandler(file_handler)
