# Accept a postive Integer n as input and print the first n positive integers, one number on as each line .
n = int(input())
for i in range(n):
    print(n)
    
    
#  Accept a positive integer n as input the first n positive integers , one number in each line.
n =int(input())
for i in range(n+1):
    print(i)
    
#  Accept a positive integer n as input and print all the factors, one number in each line.

n = int(input("Enter the Number :"))
for i in range(1 , n+1):
    if n%i == 0:
        print(i)