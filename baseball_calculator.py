jerseyNumber = int(input("Please enter a jersey number: "))

while jerseyNumber != 0:

	totalBases = int(input("Please enter the number of total bases: "))

	atBats = int(input("Please enter the number of at bats: "))

	hits = int(input("Please enter the number of hits: "))

	walks = int(input("Please enter the number of walks: "))

	sacFlies = int(input("Please enter the number of sacrifice flies: "))

	sluggingPercentage = totalBases / atBats

	OBP = (hits + walks) / (atBats + walks + sacFlies)

	GPA =  ((OBP  * 1.8) + sluggingPercentage) / 4

	print("This is player # " + str(jerseyNumber))

	print("Total Bases: " + str(totalBases))

	print("At Bat: " + str(atBats))

	print("Slugging Percentage: " + str(sluggingPercentage))

	print("Hits: " + str(hits))

	print("Walks: " + str(walks))

	print("Sac Flies: " + str(sacFlies))

	print("On Base Percentage: " + str(OBP))

	print("Grade Point Average: " + str(GPA))

	jerseyNumber = int(input("Please enter a jersey number or press 0 to quit: "))

print("End of program")
