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