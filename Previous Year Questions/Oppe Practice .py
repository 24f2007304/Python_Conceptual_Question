# Accept a sequence of Positive integer as input and print the maximum number in the sequence. The input will have n+1 lines , when n denotes the number of terms in the sequence . The ith line in the input will contains the term in the Sequence for 1<= n <=n . The last line of the input will always be the number 0 . Each test case will have at least one term in the Sequence
maxn = -float('inf')  # Initialize maxn to a very small number

while True:
    n = int(input())
    if n == 0:
        break
    if n > maxn:
        maxn = n

print(maxn)

