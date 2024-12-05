# Matrix Transposition: Write a function transpose(matrix) that returns the transpose of a given 2D matrix.
'''Matrix Transpose Means intercnaging if row and columns.'''


def Intialise_Matrix(dim):
    Matrix = []
    for i in range(dim):
        Matrix.append([])   # At these time we [[],[],[]] if given dim =3 , We have nested list that can append as a list. 
    for i in range(dim): # 0,1,2 are the range(dim) .It helps to  select the small list [].
        for j in range(dim): # 0,1,2 in the range(dim) . It helps to append "zeros" in the List for 3 Times.in the same list Let Say that is #0 is the index Number .
            Matrix[i].append("0")
    return Matrix 




def Matrix_Transpose(Matrix):
    
    dim = len(Matrix)
    Transpose_Matrix = Intialise_Matrix(dim)
    for i in range(dim):
        for j in range(dim):
            Transpose_Matrix[j][i] = Matrix[i][j]
    return Matrix


print(Matrix_Transpose([[12,3,4],[4,5,6],[6,7,8]]))
print(Intialise_Matrix(4))


       

