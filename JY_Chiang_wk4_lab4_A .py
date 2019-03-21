Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # getData
>>> def getData():
	name = input("Enter primary tax payer full name: ")
	mStatus = input("Enter ‘s’ for single and ‘m’ for married: ")
	if mStatus == "m":
		children = input("Enter the number of children under the age of 14: ")
		GI = input("Enter you and your spouse's combined salary: ")
	else:
		GI = input("Enter your salary: ")
		children = 0
	pension = input("Enter the percentage of gross income designated for pension fund: ")
	lst = [name , mStatus , children, GI, pension]
	return lst

>>> # computTax
>>> def computTax(lst):
	pension1 = int(lst[-2]) * float(int(lst[-1])/100)
	if lst[1] == "m":
		total_deduct = 7000 + 1500 * (int(lst[2]) + 2)
	elif lst[1] == "s":
		total_deduct = 4000 + 1500
	taxable_income = int(lst[-2]) - int(pension1) - total_deduct
	if 0 < taxable_income < 15000:
		tax = taxable_income * 0.15
	elif taxable_income > 15001:
		tax = 2250 + 0.25*(taxable_income-15000)
	lst1 = ("Pension amount:{}, Total deduction:{}, Taxable income:{}, Tax:{}".format(int(pension1), total_deduct, taxable_income, int(tax)))
	return lst1

>>> #Run the result
>>> computTax(getData())
Enter primary tax payer full name: Rae Chiang
Enter ‘s’ for single and ‘m’ for married: m
Enter the number of children under the age of 14: 2
Enter you and your spouse's combined salary: 200000
Enter the percentage of gross income designated for pension fund: 6
'Pension amount:12000, Total deduction:13000, Taxable income:175000, Tax:42250'
>>> 
