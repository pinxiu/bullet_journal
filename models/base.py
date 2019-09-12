import datetime
import uuid

from app import db

UUID_LENGTH = 36


class Base(db.Model):

	created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)


def create_uuid_string() -> str:
    return uuid.uuid4().hex
