# Factorial of a Number: Write a function factorial(n) that calculates the factorial of a number n using recursion.

n = int(input("Enter the Number which You Want To find the Factorial :"))
factorial = 1
for i in range(1,n+1):
    factorial*=i
print(f'The Factorial of {n} is {factorial}')