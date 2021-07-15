import requests

API_KEY = "WKCFP1Ou2g-m2DvZ6ARnKFhsqyVL9gJf0SCg4LSpLnY"

class HereApi():

	def __init__(self):

		self.url = 'https://geocode.search.hereapi.com/v1/geocode'
		self.query = None
		self.params = { 'q' : self.query,
						'apiKey' : [API_KEY]}

	def __setQuery(self, request):

		self.query = request
		return self.query

	def sendQuery(self, request):

		try:
			self.__setQuery(request)
			self.params['q'] = self.query
			req = requests.get(self.url, self.params)
			responses = req.json()
			print(responses)
			return responses['items'][0]['address']['label']
		except IndexError:
			return "Je n'ai rien trouvé désolé, essais d'ajouter le nom d'une ville, d'un pays."

# here = HereApi()
# print(here.sendQuery(input('Entrer votre requête : ')))
