# File: services/form-management/app.py

from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from .models import db, FeedbackForm

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL_FORM_CONFIG")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/forms', methods=['POST'])
def create_form():
    data = request.get_json()
    if not data or not data.get('name') or not data.get('fields'):
        return jsonify({'error': 'Name and fields are required'}), 400

    new_form = FeedbackForm(
        name=data['name'],
        description=data.get('description'),
        status=data.get('status', 'active'),
        created_by=data.get('created_by', 'admin'), # Placeholder for actual admin user
        fields=data['fields'],
        styling=data.get('styling')
    )
    db.session.add(new_form)
    db.session.commit()
    return jsonify(new_form.to_dict()), 201

@app.route('/forms', methods=['GET'])
def get_forms():
    forms = FeedbackForm.query.all()
    return jsonify([form.to_dict() for form in forms])

@app.route('/forms/<int:form_id>', methods=['GET'])
def get_form(form_id):
    form = FeedbackForm.query.get_or_404(form_id)
    return jsonify(form.to_dict())

@app.route('/forms/<int:form_id>', methods=['PUT'])
def update_form(form_id):
    form = FeedbackForm.query.get_or_404(form_id)
    data = request.get_json()

    form.name = data.get('name', form.name)
    form.description = data.get('description', form.description)
    form.status = data.get('status', form.status)
    form.fields = data.get('fields', form.fields)
    form.styling = data.get('styling', form.styling)
    form.updated_at = db.func.current_timestamp()

    db.session.commit()
    return jsonify(form.to_dict())

@app.route('/forms/<int:form_id>', methods=['DELETE'])
def delete_form(form_id):
    form = FeedbackForm.query.get_or_404(form_id)
    db.session.delete(form)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Create database tables if they don't exist
    app.run(debug=True, host='0.0.0.0')
