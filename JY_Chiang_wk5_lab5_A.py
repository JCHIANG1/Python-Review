def population_countries():
	print("Mexico population","/ USA population","/ time:year past")
	year = 0
	MP = 1210000
	USP = 3150000
	
	while year >= 0 :
		a = int(MP * (1.0101)**year)
		b = int(USP * (0.9985)**year)
		if a > b :
			break
		else:
			print("{:15} {:15} {:10}".format(a,b,year))
			year += 1
	print("{:15} {:15} {:10}".format(a,b,year))
	print("It will take {} years for the population in Mexico to exceed the population in USA".format(year))


population_countries()
