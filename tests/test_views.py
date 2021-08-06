import pytest
from flask import Flask, render_template

def test_index_route():
	app = Flask(__name__)
	client = app.test_client()
	url = "/"

	@app.route("/")
	def test_index():
		return "test application route"

	response = client.get(url)

	assert response.status_code == 200


	def test_hello(client):
		response = client.get('/hello')
		assert response.data == b'Hello, World!'

def test_result_route():
	app = Flask(__name__)
	client = app.test_client()

	@app.route("/")
	def test_result():
		req = client.post('something')
		assert req.status_code == 200

