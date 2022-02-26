# Insert a string in the middle of another string
def S_append(arg1,arg2):
    """A program that slices string1 into two, adding
    the first part to the begining of string2 and then adding
    the second part of s1 to the end of string s2"""
    mid_num = int(len(arg1)/2)
    new_string = arg1[:mid_num] + arg2 + arg1[mid_num:]
    print("The result is", new_string)
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")

S_append(s1,s2)