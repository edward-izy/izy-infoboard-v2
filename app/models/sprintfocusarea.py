from datetime import datetime

from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class SprintFocusArea(Model):
    __tablename__ = 'sprint_focus_area'
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    sprint = Column(db.String, nullable=False)
    title = Column(db.String, nullable=False)
    description = Column(db.String, nullable=False)
    created_date = Column(db.DateTime, default=datetime.utcnow)