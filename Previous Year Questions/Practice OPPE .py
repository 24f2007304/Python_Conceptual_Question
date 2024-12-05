# Accept a sequence of Positive integer as input and print the maximum number in the sequence. The input will have n+1 lines , when n denotes the number of terms in the sequence . The ith line in the input will contains the term in the Sequence for 1<= n <=n . The last line of the input will always be the String abcdefghijklmnopqrst . Each test case will have at least one term in the Sequence
word = input()
minlen = len(word)
minword = word

end = "abcdefghijklmnopqrstuvwxyz"
while word!= end:
    if len(word)<=minlen:
        minlen = len(word)
        minword = word
    word = input()

print(minword)