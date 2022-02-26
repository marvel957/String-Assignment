def string_arrange(arg):
    """Arranges string characters such that lower case comes first"""
    a = ""
    b = ""
    for i in arg:
        if i == i.lower():
            a +=i
        else:
            b += i 
    print("The New string is", a + b)

string_arrange("HsAikM")
string_arrange("lVERPOiOL")