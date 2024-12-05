'''Accept Space Seperated sequence of positive real number as input . Convert each element into integer than print it.'''

l = (input()).split()
List = []
for i in l:
    integer = int(float(i))   # If we want to Change float into integer.
    List.append(integer)
print(List)
    
    

