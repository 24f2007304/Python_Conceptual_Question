'''Here we are use to find the count in the list'''

def count(l,word):
    if len(l)==0: # Here we are stoping the and if the length of l is 0 then there will not be any further Steps.
        return 0
    if l[0]==word:
        return 1+count(l[1:],word) # Here we are count increase when same word in the list.
    return count(l[1:],word) # These is for when not any element matches the word.


l=["Apple","Bannana","Orange"]

print(count(l,"Apple"))