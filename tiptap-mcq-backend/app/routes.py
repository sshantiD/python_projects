from flask import request, jsonify, Blueprint
from app.services.mcq_service import MultipleChoiceQuestionService
from app.services.test_summarization_service import TextSummarizationService

bp = Blueprint('bp', __name__)
    
@bp.route('/api/v1/save-file', methods=['POST'])
def save_file():
    try:
        result = MultipleChoiceQuestionService.save_mcq_data_to_json(request.json)
        return jsonify({'data': result}), 200
    except Exception as e:
        return jsonify({'error': f'Error saving MCQ data: {str(e)}'}), 500
    
    
@bp.route('/api/v1/text-summarization', methods=['POST'])
def text_summarization():
    try:
        text = request.json["text"]
        result = TextSummarizationService.summarize_text(text)
        return jsonify({'data': result}), 200
    except Exception as e:
        return jsonify({'error': f'Error Summarizing data: {str(e)}'}), 500
