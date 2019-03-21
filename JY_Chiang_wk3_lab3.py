Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # JC_Chiang_wk#3_lab#3_partB
>>> # Exercise 3.30
>>> # build a function for average
>>> def average(a):
	total=0
	for num in a:
		total = num + total
	return total/len(a)

>>> # request 4 numbers from users
>>> first = eval(input("Enter first number: "))
Enter first number: 4.5
>>> sec = eval(input("Enter second number: "))
Enter second number: 3
>>> third = eval(input("Enter third number: "))
Enter third number: 3
>>> last = eval(input("Enter last number: "))
Enter last number: 3.5
>>> numList = [first, sec, third, last]
>>> numListShort = numList[:3]
>>> # apply funtion and exercute the compparison
>>> if average(numListShort) == average(numList) :
	print("Equal")

	
Equal
>>> 
