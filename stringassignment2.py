def String_ass(s1,s2):
    """This program is meant to create a new string made of the first, middle and last
    characters of each input string, given two string inputs of "America" and "Japan" the
    expected output should be "AJrpan" """
    mid_num1 = int(len(s1)/2)
    mid_num2 = int(len(s2)/2)
    new_string  = s1[0] + s2[0] + s1[mid_num1] + s2[mid_num2] + s1[-1] + s2[-1]
    print("The output is",new_string)
String_ass("America","Japan")
String_ass("Firmino","Henderson")
String_ass("Lagos","Anambra")