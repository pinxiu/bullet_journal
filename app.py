from flask import Flask, request


app = Flask(__name__)


@app.route('/store/<user_id>', methods = ['POST'])
def store(user_id):
	data = request.form
	return data
