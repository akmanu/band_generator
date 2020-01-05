from random import randint
import words

# Generate Band Name
if randint(0,1) == 0:
	band_name = f"{words.get_adjective('band')} {words.get_noun('band')}"
else:
	band_name = f"The {words.get_adjective('band')} {words.get_noun('band')}"

if randint(0,1) == 0 and band_name != "Fish":
	band_name = band_name + "s"

# Generate Genre
if randint(0,1) == 0:
	genre = f"{words.get_adjective('genre')} {words.get_noun('genre')}"
	if randint(0,5) == 0:
		genre = f"{genre}-{words.get_noun('genre')}"
else:
	genre = f"{words.get_noun('genre')} {words.get_noun('genre')}"

band_info = { "name" : band_name, "genre" : genre }
return band_info