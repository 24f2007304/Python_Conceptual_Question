# Find Missing Number: Given a list of integers from 1 to n with one number missing, write a function find_missing_number(lst) that finds the missing number.


'''To find the Difference in The List we have to use set difference method = set(List1)-set(List2) that means remove all element in List1 those who are in List 2'''

def Missing_Number(List):
    Range = []
    n = max(List)
    for j in range(1,n):
             Range.append(j)
    Missing_Number =list( set(Range) - set(List))  
    Missing = ' , '.join(map(str , Missing_Number))
    # The ", ".join() method in Python is used to concatenate the elements of an iterable (such as a list or tuple) into a single string, with each element separated by a specified delimiter. In this case, the delimiter is a comma followed by a space (,).
    return f'List of Element that is not Present in given btw List = {Missing}'

'''For Geeting Not in List  We use for loop'''

print(Missing_Number([12,34,56]))
    
    