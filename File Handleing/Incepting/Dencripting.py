'''Important We can Create a  two function of Same Name.'''

import string as st


def Create_caser_myalok():
    d={}
    l =st.ascii_lowercase
    l = list(l)
    for i in range(len(l)):
        d[l[i]] = l[(i-3)%26]
    return d# By the Help of these formula we can change the value in {"a":"d","b":"f"}


# def Create_caser_myalok():
#     d={}
#     l =st.ascii_uppercase
#     l = list(l)
#     for i in range(len(l)):
#         d[l[i]] = l[(i-3)%26]
#     return d# By the Help of these formula we can change the value in {"a":"d","b":"f"}
        
        
f = open("C:\Phython Files\File Handleing\myalok_encripted.text","r")
g = open("C:\Phython Files\File Handleing\Dencripted.text","w")

# d = Create_caser_myalok()
# s = f.read(1)

# while s != '':
#     if s in d:  # Encrypt only if the character is a lowercase letter
#             g.write(d[s])
#     else:
#             g.write(s)  # Non-alphabet characters are written as is
#     s = f.read(1)  # Read next character
    
        
# g.close
# f.close