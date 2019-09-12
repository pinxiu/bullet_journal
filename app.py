import os

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['REDIS_URL']
db = SQLAlchemy(app)


from models import BjRecord, BjUser


BJ_REQUEST_ORIGIN_LIST = {
	'bj.cli',
	'bj.postman',
	'bj.web',
	'bj.desktop',
}


@app.route('/signup', methods = ['POST'])
def signup():
	if not is_bj_header(request.headers):
		return '', 401
	username = request.form.get('username')
	password = request.form.get('hashed-password')
	if BjUser.has_username(username):
		return '', 400
	user_id, access_token = BjUser.add_user(username, password)
	bj_record = BjRecord(
		user_id=user_id,
		data='',
	)
	db.session.add(bj_record)
	db.session.commit()
	return jsonify(
		user_id=user_id,
		access_token=access_token,
	)


@app.route('/login', methods = ['POST'])
def login():
	if not is_bj_header(request.headers):
		return '', 401
	username = request.form.get('username')
	password = request.form.get('hashed-password')
	if not BjUser.has_username(username):
		return '', 401
	user_id, access_token = BjUser.get_user(username, password)
	if not user_id or not access_token:
		return '', 401
	return jsonify(
		user_id=user_id,
		access_token=access_token,
	)


@app.route('/<user_id>', methods = ['GET', 'PUT'])
def access(user_id):
	if not has_access(user_id, request.headers):
		return '', 401

	bj_record = BjRecord.query.filter_by(user_id=user_id).first()

	if request.method == 'GET':
		return bj_record, 200

	bj_record.data = data
	db.session.commit()
	return '', 204


def has_access(user_id, headers):
	access_token = headers.get('BJ_SERVER_ACCESS_TOKEN')
	if not access_token:
		return False
	server_token = BjUser.get_token_by_user_id(user_id)
	return server_token == access_token


def is_bj_header(headers):
	origin = headers.get('BJ_REQUEST_ORIGIN')
	return origin in BJ_REQUEST_ORIGIN_LIST
