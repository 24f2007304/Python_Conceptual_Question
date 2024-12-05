# Take a (a,b)input from user
# Print the sum of all integer in the range [1000,2000],endpoint inclusive,that are
# Divissible by both a and b . If you find as number satisfying this condition

num1 = int(input("Enter The NUmber :"))
num2 = int(input("Enter The Number :"))
sum = 0
for i in range(1000,2001):
    if i % num1 ==0 and i % num2 == 0:
        sum +=i
print(sum)
 
# num1 = int(input("Enter The NUmber :"))
# num2 = int(input("Enter The Number :"))
# sum = 0
# for i in range(1000,2001):
#   if i % num1 == 0 and i % num2 ==0:
#      sum+=i
# print(sum)