# A Positive Integer m is a prime prodect if it can be written as p*q , where p and q are both primes,
#  Write a Python Function prime_product(m) that take an intger m as input and returns True .If m is a prime product and False otherwise (If m is not positive , function should return False)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_product(n):
    for i in range(n):
        for j in range(n):
            if is_prime(i) and is_prime(j) and i*j ==n:
                return True
    return False


    
print(Multiplication_Prime(6))