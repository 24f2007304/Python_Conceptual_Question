import numpy as np


s1 = [12,45,6]
s2 = [15,45,18]
s3 = [19,45,84]

r1 = [8,54,63]
r2 = [75,86,56]
r3 = [85,78,32]

A = [] 
B= []
A.append(s1)
A.append(s2)
A.append(s3)


B.append(r1)
B.append(r2)
B.append(r3)



C = [[0,0,0],[0,0,0],[0,0,0]]

# Matrix Multiplication is from Row Cross Columns 
dim = 3

for i in range(dim):
    for j in range(dim):
        for p in range(dim):
            C[i][j] = C[i][j] + A[i][p]*B[p][j] # Here we are updating C[i][j] where A[i](Here row is fixed) and B[][j] (Here colum is fixed)
print(C)

# Second way of Doing these 
x = np.asmatrix(A)
y=np.asmatrix(B)
print(x*y)


