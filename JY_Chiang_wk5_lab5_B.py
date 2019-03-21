def compute_data():
	results = []
	GP=20000
	EP=35000
	time=0

	NET = GP-EP
	time += 1
	results.append(NET)
	while 0 < time < 20:
		GP = int(20000*(1.1)**time)
		EP = int(35000*(1.04)**time)
		NET = GP-EP
		time += 1
		results.append(NET)
		
	return " ".join(str(x) for x in results)


def save_data(data):
	outfile = open("test.txt","w")
	outfile.write(data)
	outfile.close()
	g1=[]
	g2=[]
	for num in data.split():
		if eval(num) < 0:
			g1.append(num)
			
			
		else:
			g2.append(num)
	g2[0] = "*"+g2[0]
	print("Net loss group: ",g1)
	print("Net profit group: ",g2)


	
save_data(compute_data())
