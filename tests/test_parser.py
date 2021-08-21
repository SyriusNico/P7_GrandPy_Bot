from botapp.api import stopwords as s
from botapp.api import mediaWiki as m

def test_parse_text():
	assert "Zidane" not in s.stopwords

def test_sentence_contain_stopwords():

	media = m.MediaWiki()


	whereIsOpenclassrooms = media.parseText("Pourrais-tu me donner l'adresse \
											du studio de Openclassrooms ?")

	restaurantBègle = media.parseText("Je cherche l'adresse d'un \
										bon restaurant à Bègle")


	assert whereIsOpenclassrooms == "Pourrais-tu donner studio Openclassrooms ?"

	assert restaurantBègle == "Je cherche d'un restaurant Bègle"