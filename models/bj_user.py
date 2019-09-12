import hashlib
import os

from app import db

from .base import Base, create_uuid_string, UUID_LENGTH

secret = os.environ['BJ_SECRET']


class BjUser:
	__tablename__ = 'bj_user'

	id = db.Column(db.String(UUID_LENGTH), primary_key=True, default=create_uuid_string)
	username = db.Column(db.String(15), unique=True, nullable=False)
	access_token = db.Column(db.String(255), unique=True, nullable=False)


	def __init__(self, username, access_token):
		self.username = username
		self.access_token = access_token


	def has_username(username):
		return db.session.query(BjUser.id).filter_by(username=username).scalar() is not None


	def get_user(username, password):
		access_token = hmac(username, password)
		bj_user = db.session.query(BjUser)
							.filter_by(username=username)
							.filter_by(access_token=access_token)
							.scalar()
		if not bj_user:
			return None, None
		else:
			return bj_user.id, access_token


	def add_user(username, password):
		access_token = hmac(username, password)
		bj_user = BjUser(
			username=username,
			access_token=access_token
		)
		db.session.add(bj_user)
		db.session.commit()


	def get_token_by_user_id(user_id):
		return BjUser.query(BjUser.access_token).filter_by(user_id=user_id).first()


	def hmac(username, password):
		message_raw = f'username: {username}, password: {password}'
		message = hashlib.sha512().update(message_raw.encode()).hexdigest()
		dk = hashlib.pbkdf2_hmac('sha256', message.encode(), secret.encode(), 100000)
		return binascii.hexlify(dk).decode('utf-8')
