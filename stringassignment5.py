def s_g(s1,s2):
    """Given two string s1 and s2, This program will create a new string s3 made of
    the first character of s1, then the last char of s2, next the second char of s1 and
    the second to last char of s2 and so on. Any left over characters are added to the
    end"""
    s3 = ""
    # reverse the second string
    s2 = s2[::-1]
    if len(s2) >= len(s1):
        for i in range(len(s2)):
            if i < len(s1):
                s3 = s3 + (s1[i] + s2[i])
            else:
                s3 = s3 + s2[i]
    else:
        for i in range(len(s1)):
            if i < len(s2):
                s3 = s3 + (s1[i] + s2[i])
            else:
                s3 = s3 + s1[i]

    print(s3)
s_g("good","lookin")
s_g("looking","good")