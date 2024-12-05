'''Here we should have to find the Factorial of some thing'''

def factorial_Num(n):
    if n ==0:
         return 1
    return n*factorial_Num(n-1)  # Here we can intialize the value to n==0 this is 1 and alog these multiplying these to other.

print(factorial_Num(4))
    
        


        