from random import randint

def get_noun(noun_type):
	if noun_type == "band":
		nouns = ["Giant", "Master", "Band", "Music",
			"Potter", "Ghost", "Girl", "Boy", "Fish", "Dog",
			"Cat", "Joke", "Bowl", "Cancer", "Youth", "Light",
			"Luddite", "Choir"
		]
	elif noun_type == "genre":
		nouns = ["Rock", "Skiffle", "Hip Hop", "Jazz",
			"Fusion", "Muzak", "Punk", "Funk", "Blues", "Folk",
			"Electronic", "Dubstep", "Trip Hop", "Metal", "Noise"
		]

	noun = nouns[randint(0, len(nouns)-1)]
	return noun

def get_adjective(adj_type):
	if adj_type == "band":
		adjectives = ["Blue", "Red", "Green", "Orange", 
			"Grey", "Black", "White", "Vermillion", 
			"Public", "Quotable", "Bad", "Awful", 
			"Kind", "Justifiable", "Modern", "Acid",
			"Limited"
		]
	elif adj_type == "genre":
		adjectives = ["Ironic", "Lofi", "Hifi", "Progressive",
			"Post"
		]

	adjective = adjectives[randint(0, len(adjectives)-1)]
	return adjective

def get_verb(tense):
	if tense == "past":
		verbs = []
	elif tense == "present":
		verbs = []

	verb = verbs[randint(0, len(verbs)-1)]
	return verb

def get_name(name_type, gender, pretentiousness):
	if name_type == "forename":
		if gender == "male":
			names = ["Tom", "John", "Harry", "Bob", "Bertrand",
					"Boris", "Ferdinand", "Harold", "Phillip",
					"Alphonse"]
		elif gender == "female":
			names = ["Rosie", "Kim", "Kelly", "Susie", "Irene",
					"Felicity", "Jacqueline", "Iris", "Abigail"]	
	elif name_type == "surname":
		names = ["Smith", "White", "Johnson", "Phillips", "Burns",
				"Simpson"]

	name = names[randint(0, len(names)-1)]

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
	accented_word = accented_word.capitalize()
	
	return accented_word