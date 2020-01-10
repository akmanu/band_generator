from random import randint
from application import models
from sqlalchemy import func

def get_word(word_type, band_or_genre):
	word = Words.query.filter_by(word_type = word_type, band_or_genre = band_or_genre).order_by(func.random()).first()

	return noun
