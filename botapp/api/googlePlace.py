#! /usr/bin/env python
# coding : utf-8
import requests

import config
from . import stopwords as s



class GooglePlace():

	def __init__(self):
		
		self.url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
		self.query = None
		self.params = { "input" : self.query,
						"inputtype" : "textquery",
						"language" : "fr",
						"fields" : "formatted_address,geometry",
						"key" : config.API_KEY}

	def parseText(self, request):
		parseRequet = request.split()
		text = ' '.join([word for word in parseRequet if word not in s.stopwords])
		return text

	def setQuery(self, request):

		self.query = newString = self.parseText(request)
		return self.query

	def sendQuery(self, request):

		try:
			self.params['input'] = self.setQuery(request)
			req = requests.get(self.url, self.params)
			address = req.json()["candidates"][0]["formatted_address"]
			latlng = req.json()["candidates"][0]["geometry"]["location"]
			print(req.json())
			return address, latlng
		except IndexError:
			return "Je n'ai rien trouvé désolé, essais d'ajouter le nom d'une ville, d'un pays."


# g = GooglePlace()
# g.sendQuery("zidane")