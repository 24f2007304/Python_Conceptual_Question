# Fibonacci Sequence: Write a function fibonacci(n) that returns the first n numbers in the Fibonacci sequence
# F(n) = F(n-2) + F(n-1)
#0,1,1,2,3,5,8,13,21,34 ...


def fibonacci(n):
    sequence = [] # Here we define a list that is store the value of Sequence
    a, b = 0, 1  #
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage
num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:")
print(fib_sequence)

''' This is Code is Written by Me'''
n = int(input())
Seq = [0,1]
a = 0
b = 1
while len(Seq)<n:
    Seq.append(b)
    a,b = b,a+b # Here we are going to be increment from lasat one
print(Seq)

    
    
    
        
        
    