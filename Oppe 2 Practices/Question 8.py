
'''n lines. A sample file is given for your reference:

1,2,3
4,5,6
7,8,9
Your task is to return the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]]'''

def Matrix_File(filename):
    Matrix =[]
    
    with open(filename ,"r")as f:
       for line in f:
           alok = [int(x) for x in line.strip().split(",")]  # Here important Step is these
           Matrix.append(alok)
    return Matrix

print(Matrix_File("C:\Phython Files\Oppe 2 Practices\Matrix.text"))