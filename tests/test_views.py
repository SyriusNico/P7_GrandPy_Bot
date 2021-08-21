import requests

from botapp import app as app

def test_index():
	with app.test_client() as c:
		response = c.get('/')
		assert response.status_code == 200


