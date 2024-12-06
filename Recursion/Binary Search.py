'''Recursive function of Search'''

def search(L,k): 
    if len(L)==0: #If the list is empty then there will be not any element in list that is equals to k.
        return False #Then we return False
    if L[0]==k: # If the First element of the list is equals to the  k.
        return True  # Then we are going to return True
    return search(L[1:],k) # If that is not equals to this then we remove the first element and fruther go one these.

L=[12,23,3456,677,78]
print(search(L,123))