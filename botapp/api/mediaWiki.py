#! /usr/bin/env python
# coding : utf-8
import requests 
import pprint

"""
raisonnement :

request me permet d'envoyer une requete à l'api médiawiki
l'api propose différente recherche en fonction du mot ou de la 
chaine de caractère passé. Je choisi la première page de recherche
et j'envoi une deuxième requete à l'api pour analyser et récuperer
un extrait de la page.

""" 

class MediaWiki():

	def __init__(self):

		self.url = 'https://fr.wikipedia.org/w/api.php'
		self.query = None
		self.queryParams = {'action': 'query',
							'list': 'search',
							'srsearch': self.query,
							'format': 'json'}
		self.extractParams = {'action': 'query',
							'prop': 'extracts',
							'format': 'json',
							'exintro': 'true',
							'explaintext': 'true',
							'exsentences': 3,
							'redirects': 1,
							'titles': self.query}

	def __setQuery(self, string):
		"""
		set user search
		"""
		self.query = string
		return self.query

	def sendQuery(self, request):

		self.__setQuery(request)
		self.queryParams['srsearch'] = self.query
		req = requests.get(self.url, self.queryParams)
		responses = req.json()
		title = responses['query']['search'][0]['title']	
		return title



	def extractQuery(self, request):

		self.__setQuery(request)
		title = self.sendQuery(request)
		self.extractParams['titles'] = title
		req = requests.get(self.url, self.extractParams)
		responses = req.json()
		result = responses["query"]["pages"]
		extract_list = list(result.values())
		extract = extract_list[0]['extract']
		print(type(extract))
		return extract



		
		


# wiki = MediaWiki()

# wiki.extractQuery(input("Entrer votre requête : "))



# TODO : API GOOGLE