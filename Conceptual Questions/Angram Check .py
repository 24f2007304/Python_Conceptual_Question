# Anagram Check: Write a function are_anagrams(str1, str2) that checks if two strings are anagrams. Two strings are anagrams if they contain the same characters in the same frequency.
# str1 = "listen"
# str2 = "silent"
# print(are_anagrams(str1, str2))  # Output: True

def are_anageument(String1,String2):
    Word1 =set()
    Word2 = set()
    for i in String1:
        Word1.add(i)
    for j in String2:
        Word2.add(j)
    if Word1 == Word2:
        return True
    else:
        return False
        


print(are_anageument("Alok","lokAm"))