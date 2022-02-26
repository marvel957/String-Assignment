def counting(arg):
    # use variable a,b and c to store numbers, alphabets and specialcharacters respectively
    a = ""
    b = ""
    c = ""
    for i in arg:
        if(i.isnumeric() == True):
            a += i
        elif(i.isalpha() == True):
            b += i
        else:
            c += i
    print("The original string is",arg)
    print("            Numbers    : ", len(a)) 
    print("            Alphabets  : ", len(b))
    print("            Symbols    : ", len(c))
input_s = input("Enter your string : ")
counting(input_s)