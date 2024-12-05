'''Accept a S equence of words as input , append all these word in a list in the order in which they are enterred , anfd print this list as output  '''
''' The first line in the input is apostive integer n that denots the Number of words in the Sentence'''
''' The next n line have a word on each line'''

l =[]
n = int(input())
for  _ in range(n):
    inp = str(input())
    l.append(inp)

print(l)

