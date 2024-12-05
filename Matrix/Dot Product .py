# Matrix Multiplication
A = [1,2,3]
B = [1,2,3]
ans =0
for i in range(len(A)):
    for j in range(len(B)):
        ans += A[i]*B[j]
print(ans)