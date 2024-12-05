# Problem 1 Write a Phython Code that gives Output Number of Upper ,Lower CaseWords and no of Character  also no. of Words
def upper(s):
    count =0
    for i in s:
        if i.isupper(): # isupper is know as to find is UpperCase or Not
            count +=1
    return count

def Lower(p):
    count =0 
    for i in p:
        if(i.islower()):
            count +=1
    return count

def No_Chart(k):
    count = 0 
    for i in k:
        count +=1
    return count
def No_Words(l):
    count =0
    b =l.split()
    return len(b)
# To count no of Words we have another word by knowing the Space

def Words(w):
    count = 0
    for i in w:
        if(i==" "):
            count +=1
    return count

    
Str = str(input('Enter the Sentence:'))
# For no.. of UpperCase letter we use Upper(Str)
Ucase  = upper(Str)
Lcase = Lower(Str)
Charr = No_Chart(Str)
Wordsp = No_Words(Str)
Words = Words(Str)
print(f'Number of upper case letter is {Ucase}')
print(f'The NUmber of lower case letter is {Lcase}')
print(f'Number of Charracter is {Charr}')
print(f'Number of Words is {Words}')
print(f'Second Method of Number of Words is {Wordsp}')
     
     
       
