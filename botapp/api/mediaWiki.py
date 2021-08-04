#! /usr/bin/env python
# coding : utf-8
import requests 
import pprint
from . import stopwords as s

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



	def parseText(self, request):

		parseRequet = request.split()
		text = ' '.join([word for word in parseRequet if word not in s.stopwords])
		return text


	def __setQuery(self, string):
		"""
		set user search
		"""
		self.query = newString = self.parseText(string)
		return self.query


	def sendQuery(self, request):

		self.__setQuery(request)
		self.queryParams['srsearch'] = self.query
		req = requests.get(self.url, self.queryParams)
		responses = req.json()['query']['search'][0]['title']
		return responses



	def extractQuery(self, request):

		try:
			self.__setQuery(request)
			title = self.sendQuery(request)
			self.extractParams['titles'] = title
			req = requests.get(self.url, self.extractParams)
			responses = req.json()["query"]["pages"]
			extract = list(responses.values())[0]['extract']
	
			return extract
		except:
			return "Bon ok ok ! Je n'ai pas d'anecdote sur cet endroit \
			mais aujourd’hui, et bien c’est le jour de mon 111e anniversaire ! \
			Je ne connais pas la moitié d’entre vous autant que je le voudrais, \
			mais j’aime moins la moitié d’entre \
			vous à moitié moins que vous ne le méritez !"


# wiki = MediaWiki()

# wiki.sendQuery("zidane")