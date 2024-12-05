'''Compute the Sum of the first n positive integer'''

def triangular(n):
    if n ==0:  # Here we are going to find if n =0  then we should have to return 0.
        return 0
    return n+ triangular(n-1) # And adding the Value to it until 0 is not comes.


print(triangular(5))

        