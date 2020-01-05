from random import randint
import words

pretentiousness = band_stats['pretentiousness']
if pretentiousness > 50:
	if randint(0,1) == 0:
		band_name = words.accent_random_vowel(band_info['name'])
		band_info['name'] = band_name

	#if math.floor((len(band_info['name']) + len(band_info['genre'])) % 3) == 0:
	#	band_info['name'] = accent_random_vowel(band_info['name'])

members = []
gender = ["male", "female"]
for member in range(0, band_stats['number of members']):
	member_gender = gender[randint(0,1)]
	member_name = f"{words.get_name('forename', member_gender, pretentiousness)} {words.get_name('surname', member_gender, pretentiousness)}"
	members.append(member_name)

band = {"members" : members}
band.update(band_info)
band.update(band_stats)