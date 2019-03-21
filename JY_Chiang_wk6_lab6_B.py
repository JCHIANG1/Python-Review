
def run_program():
    Fname = input("Enter the file name: ")
    infile = open(Fname,"r")
    content = infile.read()
    infile.close()
    print("{:10} {:}".format("Word","Frequency"))
    import re
    d = re.split("\W+", content)
    dic={}
    for word in d:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    for k in sorted(dic):
        print("{:15} {:}".format(k,dic[k]))
        
    
run_program()
    