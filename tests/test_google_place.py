import pytest

from botapp.api import googlePlace as g
from botapp.api import stopwords as s

def test_set_query():
	google = g.GooglePlace()
	google.setQuery("text")
	assert google.query == "text"

def test_oject_is_instance_of_google_place():
	google = g.GooglePlace()
	assert isinstance(google, g.GooglePlace)

def test_type_params_attribute():
	google = g.GooglePlace()
	assert type(google.params) == dict 

def test_query_type():
	google = g.GooglePlace()
	assert type(google.sendQuery("address")) == tuple

def test_send_query_google_return_place(monkeypatch):

	def mock_sendQuery(*args):
		response = {'candidates': 
			[{'formatted_address': 'Paris, France', 
				'geometry': {'location': {'lat': 48.856614, 'lng': 2.3522219},
			    'viewport': {'northeast': {'lat': 48.9021449, 'lng': 2.4699208}, 
			    'southwest': {'lat': 48.815573, 'lng': 2.224199}}}}], 
			    'status': 'OK'}
		return response["candidates"][0]["formatted_address"], \
			response["candidates"][0]["geometry"]["location"]

	monkeypatch.setattr('botapp.api.googlePlace.GooglePlace.sendQuery', mock_sendQuery)

	google = g.GooglePlace()

	result = google.sendQuery('Paris')

	assert result == ('Paris, France', {'lat': 48.856614, 'lng': 2.3522219}) 
