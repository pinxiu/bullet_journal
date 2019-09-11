from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

# from models import BjRecord


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


@app.route('/<user_id>', methods = ['GET', 'POST', 'PUT'])
def access(user_id):
	# auth(user_id, request.headers)

	if request.method == 'GET':
		return #BjRecord.get_record_by_user_id(user_id)
	elif request.method == 'POST':
		data = request.get_data()
		# db.session.add(result)
	return data
