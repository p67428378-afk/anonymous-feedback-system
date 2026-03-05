# File: services/form-management/models.py

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import func

db = SQLAlchemy()

class FeedbackForm(db.Model):
    __tablename__ = 'feedback_forms'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default='active', nullable=False)
    created_by = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    fields = db.Column(JSONB, nullable=False) # JSON array of field definitions
    styling = db.Column(JSONB, nullable=True) # JSON object for UI customization

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'status': self.status,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'fields': self.fields,
            'styling': self.styling
        }

    def __repr__(self):
        return f"<FeedbackForm {self.id}: {self.name}>"
