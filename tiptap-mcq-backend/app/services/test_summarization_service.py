from transformers import pipeline
from app import summarization_pipeline
class TextSummarizationService:
    
    @staticmethod
    def summarize_text(text, max_length=50):
        try:
            summarized_text = summarization_pipeline(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']
            return summarized_text
        except Exception as e:
            return str(e)