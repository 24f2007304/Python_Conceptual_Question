''' A Square matrix M is said to be:
* Diagonal Matrix : If the enteries out Side the main Diagonal are all Zero
* Scalar : If it is a Diagonal matrix ,all the digonal element are Equal
*Identity : If it is a Scalar matrix,all of whose digonal element are 1'''
 
# Write a function named matrix_type accept a matrix M as an Argument and return type of matrix
import numpy as np
M=np.matrix

def Matrix_Type(M):
B = M[0][0]
dim = len(M)
Identity = 0
Scalar = 0

for i in range(dim):
    for j in range(dim):
        # Checking for Diagonal Matrix
        if i != j :
            if M[i][j] != 0:
                print("Not a Diagonal Matrix")
        else:
            # For identity matrix
            if M[i][j] == 1:
                 Identity += 1
            
            else :
                if M[i][j] == B:
                  Scalar +=1
if(Identity == dim):
    return ("Identity Matrix")
elif(Scalar == dim):
    return("Scalar Matrix")
else:
    return("Diagonal Matrix")                


                        