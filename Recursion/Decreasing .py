'''Write a code which returns True if the list is in the non -decrasing Order'''

def Decreasing(l):
    if len(l)==0 or len(l)==1: # Here we are going to find the if the last element ..
        return True
    if l[0]<=l[1]: # We use these for if the element is Same..
        return Decreasing(l[1:]) # It goes till the end last pair that will be satisfies
    else:
        return False  # If Not any Condition Satatisfies

print(Decreasing([1,1,2,3,4,5,1]))