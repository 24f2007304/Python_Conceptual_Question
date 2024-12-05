# Palindrome Check: Write a function is_palindrome(s) that checks if a given string s is a palindrome. A palindrome is a string that reads the same forward and backward.

def Palindrome_Check(Str1):
    opp = Str1[::-1]
    if Str1== opp:
        return("Palindrom")
    elif Str1 != opp:
        return("Not Palindrom")
print(Palindrome_Check("APPa"))
    
'''If we Sshould have to make a not a case Senstive Pallindrom'''
# For These We Should Have to make a  lowercase to a letter for avoid these.

def Palindrome_lower_Check(Str):
    Str = Str.lower() 
    opp = Str[::-1]
    if Str == opp:
        return ("Palindrom")
    elif Str != opp:
        return ("Not Palindrom")
    
print(Palindrome_lower_Check("APPa"))
    


    