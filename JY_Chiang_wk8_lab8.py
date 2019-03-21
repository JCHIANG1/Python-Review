class Account:
    def __init__(self, pin, accountNumber, firstName, lastName,  accountBalance, accountType):
        self.pin = pin
        self.accountNumber = accountNumber
        self.firstName = firstName
        self.lastName = lastName
        self.accountBalance = accountBalance
        self.accountType = accountType 

class ATM():       
    
    savingAccounts = {}
    
    def __init__(self):
        pass
    
    def loadAccounts(self,filename):
        infile = open(filename)
        for line in infile:            
            PinNum = line.split(",")[0]
            PinNum = eval(PinNum)
            Ian = line.split(",")[1]
            Ian = eval(Ian)
            Ifn = line.split(",")[2]
            Iln = line.split(",")[3]
            Iab = line.split(",")[4]
            Iab = eval(Iab)
            Iat = line.split(",")[5]
            accountInfo = Account(PinNum,Ian,Ifn,Iln,Iab,Iat)
            self.savingAccounts[PinNum] = accountInfo
            
    def login(self,PinNum):
        if PinNum in self.savingAccounts.keys():
            return True  
        return False
    
    def display(self,PinNum):
        print("{:12} {:3} {:5} {:5} {:8} {:}".format("Account Info:","#","FirstName", "LastName", "Balance", "Type"))
        print("{:11} {:5} {:9} {:9} {:5} {:}".format("",self.savingAccounts[PinNum].accountNumber,self.savingAccounts[PinNum].firstName,self.savingAccounts[PinNum].lastName,self.savingAccounts[PinNum].accountBalance,self.savingAccounts[PinNum].accountType))
    
    def makeDeposit(self,DAmount,PinNum):
        print("Account balance before deposit:{}".format(self.savingAccounts[PinNum].accountBalance))
        self.savingAccounts[PinNum].accountBalance += DAmount
        print("Account balance after deposit:{}".format(self.savingAccounts[PinNum].accountBalance))
        return self.savingAccounts[PinNum].accountBalance
    
    def makeWithdraw(self,WAmount,PinNum):
        print("Account balance before withdraw:{}".format(self.savingAccounts[PinNum].accountBalance))
        self.savingAccounts[PinNum].accountBalance -= WAmount
        if self.savingAccounts[PinNum].accountBalance < 0:
            print("Insufficient amount to withdraw")
        else:
            print("Account balance after withdraw:{}".format(self.savingAccounts[PinNum].accountBalance))
            return self.savingAccounts[PinNum].accountBalance
    
    
    def viewAccountBalance(self,PinNum):
        print("Account balance:{}".format(self.savingAccounts[PinNum].accountBalance))
        return self.savingAccounts[PinNum].accountBalance

user = ATM()
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
        Option = int(input("[1->View Account Balance, 2-> Make Deposit, 3-> Make withdraw, 4-> Restart] Select your option: "))
        if Option == 1:
            user.viewAccountBalance(pinNum)
            break
        elif Option == 2:
            dAmount = int(input("Enter the deposit amount: "))
            user.makeDeposit(dAmount,pinNum)
            break
        elif Option == 3:
            wAmount = int(input("Enter the withdraw amount: "))
            user.makeWithdraw(wAmount,pinNum)
            break
        elif Option == 4:
            n = 1
            continue
    else: 
        print("Enter the valid pin number!")
        continue
        
        

        
        


