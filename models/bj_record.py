from app import db

from .base import Base, UUID_LENGTH


class BjRecord(Base):
	__tablename__ = 'bj_record'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String(UUID_LENGTH), unique=True, nullable=False)
	data = db.Column(db.String(1000000), unique=False, nullable=False)


	def __init__(self, user_id, data):
		self.user_id = user_id
		self.data = data
