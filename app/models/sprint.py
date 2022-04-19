from datetime import datetime

from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class Sprint(Model):
    __tablename__ = 'sprint'
    sprint = Column(db.String, primary_key=True)
    development_start = Column(db.Date, nullable=False)
    development_end = Column(db.Date, nullable=False)
    test_start = Column(db.Date, nullable=False)
    test_end = Column(db.Date, nullable=False)
    production_date = Column(db.Date, nullable=False)
    state = Column(db.String, nullable=False)
    created_date = Column(db.DateTime, default=datetime.utcnow)