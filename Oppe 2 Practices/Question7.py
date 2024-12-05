'''You are given a listr marks that has the marks scored by a class in Mathmatics test.
Find the median marks and store it in a float variable named median.'''

# It is for finding the Median of a list

Marks =[12,106,52,123]
lenght = len(Marks)
Marks.sort()


if lenght//2 ==0:
    print(Marks[(lenght//2)+1])  # If the length of list is even then median is the next number after the middle of list.
    
else:
    print(Marks[(lenght)//2]) # To find the middle of the list..
    