from random import randint
from application.models import Names
from sqlalchemy import func

def get_name(name_type, pretentiousness):
	query = Names.query.filter_by(name_type = name_type).order_by(func.random()).first()
	name = query.name

	if pretentiousness > 50:
		name = accent_random_vowel(name)

	return name

def accent_random_vowel(word):
	vowel_accents = { "a" : "àáäãå",
					  "e" : "èéêëę",
					  "i" : "iîïíī",
					  "o" : "ôöòóø",
					  "u" : "ûüùúū" }
	
	count = 0
	word = word.lower()
	accented_word = ""
	for letter in word:
		if letter in "aeiou" and randint(0,3) == 0:
			replacement = vowel_accents[letter]
			letter = replacement[randint(0, len(replacement)-1)]
		accented_word += letter
		count += 1
	
	accented_word = accented_words.title()
	
	return accented_word
	