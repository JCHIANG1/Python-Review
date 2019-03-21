Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def acronym(phrase):
	words = phrase.split()
	acr = ""
	for w in words:
		acr = w[0].upper() + acr
	return acr

>>> acronym("happy b day")
'DBH'
>>> def acronym(phrase):
	words = phrase.split()
	acr = ""
	for w in words:
		acr = acr+ w[0].upper() 
	return acr

>>> acronym("happy b day")
'HBD'
>>> 
>>> 
>>> #2Q/ why not range(len(row)-1) / how to print out as a list for each line
>>> t = [[4,7,2,5],[5,1,9,2],[8,3,6,6]]
>>> s = [[0,1,2,0],[0,1,1,1],[0,1,0,0]]
>>> def add(t,s):
	row = len(t)
	col = len(t[0])
	for i in range(row):
		for j in range(col):
			t[i][j]+=s[i][j]
			print(t[i][j], end=" ")
		print()

		
>>> add(t,s)
4 8 4 5 
5 2 10 3 
8 4 6 6 
>>> 
