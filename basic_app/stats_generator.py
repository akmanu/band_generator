from random import randint

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