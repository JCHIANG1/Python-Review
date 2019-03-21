def official_progrma():
    fName = input("Enter the file name: ")
    
    def search_L(num):
        infile = open(fName,"r")
        content = infile.readlines()
        infile.close()
        lineN = len(content)
        if 0 < num <= lineN:
            print("The content of line",num,"is: ",content[num-1])
        else:
            print("The line was not found")
        
    def search_TW(txt):
        infile = open(fName,"r")
        content1 = infile.read()
        infile.close()
        content1 = content1.splitlines()
        for string in content1:
            a = string.split()
            if txt in a:
                break
        print("The line number of the target word is: ",int(content1.index(string))+1)
        
    while True:
        sOption = int(input("Enter a search option: "))
        if sOption == 1:
            num = int(input("Enter the line number: "))
            search_L(num)
        elif sOption == 2:
            txt = input("Enter the target word: ")
            search_TW(txt)
        elif sOption == 0:
            break

official_progrma()
