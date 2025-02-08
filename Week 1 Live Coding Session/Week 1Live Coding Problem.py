# Write a function del_char(s,c) that takes string s and c as input where c has length 1(i.e..,a single character), and returnas the string obtained by deleting all occurance of c in s. If c has length other than 1 , the function should return s.

def del_char(s,c):
    d=""
    for i in s:
        if i != c:
            d+=i
    return d


print(del_char("Banana","B"))