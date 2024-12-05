''' Here we are going to have a recursive method to find log 
of Base 2 Example:8 then it div by 2 at 4 times then it log(8)=4'''

def Log(x):
    if x ==1:  # It is termination Point of Recursion Method.
        return 0 # If x==1 then we stops the function and returns 0.
    return 1 + Log(x//2) # We adding the number untill I get a x =1.