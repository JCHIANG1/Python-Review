Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #JC_Chiang_wk4_lab4_B.py
>>> 
>>> #prompts the user to enter a phrase
>>> prompt_string = str(input("Enter a phrase: "))
Enter a phrase: aaaaeeeiiou
>>> 
>>> #vowelCount
>>> def vowelCount(v="a"):
	total = 0
	for ch in prompt_string:
		if ch == v :
			total = total + 1
	return total

>>> #display
>>> def display_result():
	print("a, e, i, o, and u appear, respectively,",vowelCount(v="a"), vowelCount(v="e"), vowelCount(v="i"), vowelCount(v="o"), vowelCount(v="u"), "times.")

	
>>> #result
>>> display_result()
a, e, i, o, and u appear, respectively, 4 3 2 1 1 times.
>>> 
