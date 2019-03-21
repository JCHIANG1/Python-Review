def craps():
    import random
    lst = [1,2,3,4,5,6]       
    toss = sum(random.sample(lst,2))
    if toss == 7 or toss == 11:
        return 1
       
    elif toss == 2 or toss == 3 or toss == 12:
        return 0
   
    else:
        while True:
            toss2 = sum(random.sample(lst,2))
            if toss2 == toss :
                return 1
                break        
            elif toss2 == 7 :
                return 0
                break


def testCraps(n):
    time = 0
    one = 0
    while time < n:
        time += 1
        if craps() == 1: 
            one += 1
    print(float(one/n))
    

def entertime():
	time = input("Enter the time of trials: ")
	time = int(time)
	testCraps(time)


entertime()


        
    
