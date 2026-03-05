# File: services/admin-reporting/app.py

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bson.json_util import dumps # To handle ObjectId serialization

load_dotenv()

app = Flask(__name__)

# MongoDB connection
mongo_client = MongoClient(os.getenv("DATABASE_URL_FEEDBACK_DATA"))
db = mongo_client.anonymous_feedback_db
feedback_collection = db.submissions

@app.route('/admin/feedback', methods=['GET'])
def get_all_feedback():
    # In a real application, this endpoint would be protected by authentication
    # and authorization middleware to ensure only admins can access it.
    # For this HLD implementation, we're focusing on the data retrieval logic.

    form_id = request.args.get('form_id')
    query = {}
    if form_id:
        query['form_id'] = form_id

    feedback_submissions = list(feedback_collection.find(query))
    return dumps(feedback_submissions)

@app.route('/admin/feedback/<submission_id>', methods=['GET'])
def get_single_feedback(submission_id):
    from bson.objectid import ObjectId
    try:
        submission = feedback_collection.find_one({'_id': ObjectId(submission_id)})
        if submission:
            return dumps(submission)
        return jsonify({'error': 'Submission not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
