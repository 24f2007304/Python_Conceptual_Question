''' Here we are going to find pallindrom and It can find by removing one element from both side'''

def Pallindrom(word):
    if len(word)<=1: # Here we are going to fiind len(word)<=1 it means in the middle there will word are not.
        return True
    if word[0]==word[-1]:
        return Pallindrom(word[1:-1])  # Here we are knowing about that kii in the last of word[1:-1] the count will start from 1 to -2 because last is not included
    
print(Pallindrom("malayalam"))

