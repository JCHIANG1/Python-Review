import JY_Chiang_accountInfo_1
import JY_Chiang_accountInfo_2

user = JY_Chiang_accountInfo_1.ATM()
user.loadAccounts("trytry.txt")

n = 1
while n<=3:
    n += 1
    pinNum = eval(input("Enter valid pin number: "))
    if type(pinNum)!= int:
        print("Input a valid 4 digit numbers")
        continue
    elif len(str(pinNum)) != 4:
        print("Input a valid 4 digit numbers")
        continue
    elif user.login(pinNum) == True:
        user.display(pinNum)
        Option = int(input("[1->View Account Balance, 2-> Make Deposit, 3-> Make withdraw, 4-> Restart,5 -> quit! ] Select your option: "))
        if Option == 1:
            user.viewAccountBalance(pinNum)
        elif Option == 2:
            dAmount = int(input("Enter the deposit amount: "))
            user.makeDeposit(dAmount,pinNum)
        elif Option == 3:
            wAmount = int(input("Enter the withdraw amount: "))
            user.makeWithdraw(wAmount,pinNum)
        elif Option == 4:
            n = 1
            continue
        else:
            break
    else: 
        print("Enter the valid pin number!")
        continue
        

