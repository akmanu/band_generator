from random import randint
import math

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

def service_1():
	print("Welcome to the Band Generator 9000.")
	input("Hit enter to generate your new band.")

	band_info = service_2()
	band_stats = service_3()
	band = service_4(band_info, band_stats)

	print(f"Band Name: {band['name']}")
	print(f"Genre: {band['genre']}")
	print(f"Pretentiousness: {band['pretentiousness']}")
	print("Members: ")

	for member in band["members"]:
		print(f"{member}")

def service_2():
	# Generate Band Name
	if randint(0,1) == 0:
		band_name = f"{get_adjective('band')} {get_noun('band')}"
	else:
		band_name = f"The {get_adjective('band')} {get_noun('band')}"

	if randint(0,1) == 0 and band_name != "Fish":
		band_name = band_name + "s"

	# Generate Genre
	if randint(0,1) == 0:
		genre = f"{get_adjective('genre')} {get_noun('genre')}"
		if randint(0,5) == 0:
			genre = f"{genre}-{get_noun('genre')}"
	else:
		genre = f"{get_noun('genre')} {get_noun('genre')}"

	band_info = { "name" : band_name, "genre" : genre }
	return band_info

def service_3():
	weighted_max = [5] * 20 + [10] * 4 + [20] * 1

	num_of_members = randint(2, weighted_max[randint(0, len(weighted_max)-1)])
	num_of_albums = randint(0, weighted_max[randint(0, len(weighted_max)-2)])
	popularity = randint(1, 101)
	pretentiousness = randint(1, 101)
	notoriety = randint(1, 101)

	band_stats = { "number of members" : num_of_members,
			   	   "number of albums" : num_of_albums,
				   "popularity" : popularity,
				   "pretentiousness" : pretentiousness,
				   "notoriety" : notoriety }

	return band_stats

def service_4(band_info, band_stats):
	pretentiousness = band_stats['pretentiousness']
	if pretentiousness > 50:
		if randint(0,1) == 0:
			band_name = accent_random_vowel(band_info['name'])
			band_info['name'] = band_name

		#if math.floor((len(band_info['name']) + len(band_info['genre'])) % 3) == 0:
		#	band_info['name'] = accent_random_vowel(band_info['name'])

	members = []
	gender = ["male", "female"]
	for member in range(0, band_stats['number of members']):
		member_gender = gender[randint(0,1)]
		member_name = f"{get_name('forename', member_gender, pretentiousness)} {get_name('surname', member_gender, pretentiousness)}"
		members.append(member_name)

	band = {"members" : members}
	band.update(band_info)
	band.update(band_stats)

	return band

service_1()

