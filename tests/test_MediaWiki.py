import pytest
import sys
sys.path.append('C:/Users/Utilisateur/Documents/ExerciceOC/P7_GrandPy_Bot/botapp/api')
import mediaWiki as m
import stopwords

def test_oject_is_instance_of_mediaWiki():
	media = m.MediaWiki()
	assert isinstance(media, m.MediaWiki)

