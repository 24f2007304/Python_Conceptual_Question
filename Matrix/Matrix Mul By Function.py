# Here we going to intialise the matri or making of matrix

def Matrix_Maker(dim):
    c = []
    for i in range(dim):
        c.append([])
    for i in range(dim): # Here we going to find inside matrix just like [[],[],[]] and we call them by c[i] after that
        for j in range(dim): # Here we are calling the inside the c[i] to append 0.
            c[i].append(0)
    return c
print(Matrix_Maker(3))



# Function for dot product

def Dot_prodc(a,b):
    dim = len(a)
    ans = 0
    for i in range(dim): # Here we going to make a dot product that can be a[i]*b[i] and i = 0,1,2 that means a[0]*b[0]+a[1]*b[1]+ a[2]*b[2]
        ans = ans + a[i]*b[i]
    return ans

x = [12,54,84]
y = [8,69,3]
print(Dot_prodc(x,y))
        
def ith_row(m,i):
    dim = len(m)
    l = []
    for p in range(dim):
        l.append(m[i][p])     # Here we are fixing the row that is i-th row and columns are varing p = range of dim
    return l 

def ith_column(m,i):
    dim = len(m)
    l = []
    for p in range(dim):
        l.append(m[p][i])     # Here we are fixing the coloumn that is i-th row and row are varing p = range of dim
    return l 
    
def matrix_Mul(A,B):
    dim = len(A)
    C = Matrix_Maker(dim)
    for i in range(dim):
        for j in range(dim):
            C[i][j] = Dot_prodc(ith_row(A,i), ith_column(B,j))
    return C

B= [[12,5,45],[8,45,71],[9,21,32]]
A= [[1,5,45],[1,45,71],[1,0,32]]


print(matrix_Mul(A,B))

 