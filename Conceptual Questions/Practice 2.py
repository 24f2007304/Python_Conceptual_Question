# In a first line of input, accept a Sequence of Space-Seperated Words . In the second line of input, accept a single word. If this word is not present in the Sequence Print NO and if Present print YES otherwise stay let to be .

'''Yes , I did It!!!'''

Secq = input()
Word = input()
Para = Secq.split(" ")
count = 0
Ncoun =0
for i in Para:
    if i == Word:
        count +=1
        print("YES")
        print(count)
    else:
        Ncoun +=1
if Ncoun == len(Para):
    print("NO")