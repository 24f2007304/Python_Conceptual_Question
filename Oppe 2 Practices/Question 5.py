'''Matrix Maker 
In the first line we get a integer 
and there are numbers in them'''

Matrix =[]
n = int(input())

for _ in range(n):
    inpu = input().split()
    list =[]
    for i in inpu:
        list.append(i)
    Matrix.append(list)
    
# Matrix.append(list)
print(Matrix)
