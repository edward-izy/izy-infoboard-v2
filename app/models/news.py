from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid


from app import db

# Alias common DB names
Column = db.Column
Model = db.Model


class News(Model):
    __tablename__ = 'news'
    #id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = Column(db.Integer, primary_key=True, autoincrement=True)
    title = Column(db.String, nullable=False)
    description = Column(db.String, nullable=False)
    image_path = Column(db.String, nullable=False)
    active = Column(db.Boolean, nullable=False)
    created_at = Column(db.DateTime, default=datetime.utcnow)