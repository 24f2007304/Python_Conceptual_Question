'''Write a recursive function named unique that accepts a non-empty list l as argument and returns a new list after removing all duplicates from it . You function musrt retain the last occurance of each distinct in the list.'''

def unique(l):
    if len(l) <= 1: # If there will be only one element then it will be a unique list .
        return l  # Then it will return only  list
    if l[0] in l[1:]: # If the first element present in the list
        return unique(l[1:]) # If the first element is not unique then it will be remove from itt.
    return[l[0] + unique(l[1:])] # If it is Unique then it will be add to another list and Return it...