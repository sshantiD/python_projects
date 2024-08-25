

**Overview**

The backend of the project serves as the server-side component responsible for handling requests from the frontend, processing data, and providing responses. It is built using Python Flask, a micro web framework. The backend consists of two APIs: Save File API and Text Summarization API, designed to support different functionalities required by the application.

  
**APIs**

1. Save File API

Endpoint: /api/v1/save-file

Method: POST

Description: This API endpoint receives data containing multiple-choice questions and saves it to an in-memory JSON file. It serves as the backend mechanism for persisting multiple-choice question data.

2. Text Summarization API

Endpoint: /api/v1/text-summarization

Method: POST

Description: This API endpoint accepts text input and generates a summary using TensorFlow-based text summarization algorithms.

Implementation Details

Technology Stack: Python, Flask

Dependencies: Ensure all necessary dependencies are installed, including Flask and any additional libraries required for text summarization.

Development Environment: Python 3.8 or higher recommended.

Database: Currently, the Save File API uses an in-memory JSON file for data persistence.

Setup and Installation

Navigate to the backend directory:

```
cd backend

virtualenv venv

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Flask application:

python run.py
```


**Usage**

Save File API:

Send a POST request to /api/v1/save-file with JSON payload containing multiple-choice question data to save it to the database.

Text Summarization API:

Send a POST request to /api/v1/text-summarization with JSON payload containing the text to be summarized. The API will generate a summary using TensorFlow-based text summarization algorithms.