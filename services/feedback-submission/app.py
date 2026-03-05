# File: services/feedback-submission/app.py

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

load_dotenv()

app = Flask(__name__)

# MongoDB connection
mongo_client = MongoClient(os.getenv("DATABASE_URL_FEEDBACK_DATA"))
db = mongo_client.anonymous_feedback_db
feedback_collection = db.submissions

@app.route('/submit', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    if not data or not data.get('form_id') or not data.get('data'):
        return jsonify({'error': 'form_id and data are required'}), 400

    # Ensure strict anonymity: no PII, IP, user-agent, etc.
    # The 'data' field should only contain the actual feedback responses.
    submission = {
        'form_id': data['form_id'],
        'submitted_at': datetime.datetime.utcnow(),
        'data': data['data'] # This should be the strictly anonymous feedback content
    }

    result = feedback_collection.insert_one(submission)
    return jsonify({'message': 'Feedback submitted successfully', 'submission_id': str(result.inserted_id)}), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
