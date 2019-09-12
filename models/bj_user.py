import binascii
import hashlib
import os

from app import db

from .base import create_uuid_string, UUID_LENGTH

secret = os.environ['BJ_SECRET']


class BjUser(db.Model):
	__tablename__ = 'bj_user'

	id = db.Column(db.String(UUID_LENGTH), primary_key=True, default=create_uuid_string)
	username = db.Column(db.String(15), unique=True, nullable=False)
	access_token = db.Column(db.String(255), unique=True, nullable=False)


	def __init__(self, username, access_token):
		self.username = username
		self.access_token = access_token


	@classmethod
	def has_username(self, username):
		return db.session.query(BjUser.id).filter_by(username=username).scalar() is not None


	@classmethod
	def get_user(self, username, password):
		access_token = hmac(username, password)
		bj_user = db.session.query(BjUser) \
							.filter_by(username=username) \
							.filter_by(access_token=access_token) \
							.scalar()
		if not bj_user:
			return None, None
		else:
			return bj_user.id, access_token


	@classmethod
	def add_user(self, username, password):
		access_token = hmac(username, password)
		bj_user = BjUser(
			username=username,
			access_token=access_token
		)
		db.session.add(bj_user)
		db.session.commit()
		return bj_user.id, access_token


	@classmethod
	def get_token_by_user_id(self, user_id):
		return db.session.query(BjUser.access_token).filter_by(id=user_id).scalar()


def hmac(username, password):
	message_raw = f'username: {username}, password: {password}'
	sha = hashlib.sha512()
	sha.update(message_raw.encode())
	message = sha.hexdigest()
	dk = hashlib.pbkdf2_hmac('sha256', message.encode(), secret.encode(), 100000)
	return binascii.hexlify(dk).decode('utf-8')
