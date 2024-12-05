# Accept a Square Matrix  as input and Store it in a variable named matrix. The first line of input will be, n , the number of rows in the matrix.Each of the next n lines will have a Sequence of n space seperated integers.

# Print(Matrix)
#2
#1 2
#1 3
# [[1,2],[1,3]]
''' Here I did It!!! '''

n =int(input())
Matrix = []
for _ in range(n):  
    a = input()
    List = a.split(" ")
    Matrix.append(List)
print(Matrix)    