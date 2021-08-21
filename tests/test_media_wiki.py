import pytest , requests, json
from botapp.api import mediaWiki as m
import botapp
	
def test_oject_is_instance_of_mediaWiki():
	media = m.MediaWiki()
	assert isinstance(media, m.MediaWiki)

def test_request_return_string():
	media = m.MediaWiki()
	assert type(media.sendQuery("request")) == str

def test_type_params_attribute():
	media = m.MediaWiki()
	assert type(media.queryParams) == dict 

def test_send_query_mediaWiki_return_title(monkeypatch):

	media = m.MediaWiki()

	query = "Que sais-tu sur Zidane ?"

	response = {'ns': 0,
		'title': 'Zinédine Zidane', 
		'pageid': 37370, 'size': 396285, 
		'wordcount': 29957, 
		'snippet': 'lisez un «\xa0bon article\xa0». \
		«\xa0<span class="searchmatch">Zidane</span>\xa0» redirige ici. \
		Pour les autres significations, \
		voir <span class="searchmatch">Zidane</span> \
		(homonymie). Zinédine <span class="searchmatch">Zidane</span>, \
		né le 23 juin 1972 à Marseille',
		'timestamp': '2021-07-11T00:19:36Z'}


	def mock_sendQuery(*args):
		return response['title']

	monkeypatch.setattr('botapp.api.mediaWiki.MediaWiki.sendQuery', mock_sendQuery)

	result = media.sendQuery(query) 

	assert result == 'Zinédine Zidane'

