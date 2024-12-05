# Accept a positive integer n as input and print a triangle of zeros for n lines. The ith line should have i zeros . There Should not be any spaces between conscutive zeros. Do not print a space at end of a line.

 # Input
# 3
# 0
# 00
# 000
# I see you're working on a little Python program! Your code prints a pattern of zeros. Here's what it does:

# It asks the user to input a number.

# For each number from 0 up to the entered number (inclusive), it prints that many zeros.

# Let me tweak your code a bit to make it more readable and avoid any potential confusion with the sep parameter, which isn't needed here:

num = int(input("ENTER THE NUMBER :"))
for i in range(num+1):
    for j in range(i): # By these we are printing for single line 
        print("0" ,sep='',end="")   
    print() #Great question! The print() at the end of the inner loop is used to move to the next line after printing all the zeros for the current row. Without it, all the zeros would be printed on a single line, rather than forming the desired triangle pattern.
    