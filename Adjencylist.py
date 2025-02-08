edges= [(0,1),(0,4),(2,0),(3,4),(3,6),(4,0),(4,3),(4,7),(5,3),(5,7),(6,5),(7,4),(7,8),(8,5),(8,9),(9,8),(1,2)]
# If I want ot make an Adjency Matrix we have to use the numpy

import numpy as np
A  = np.zeros(shape=(10,10))

for (i,j) in edges:
    A[i,j] = 1 # That if there will any edge between the vertex then the matrix represent it through 1 otherwise to 0
    
print(A)

#  In the Dictionary Alist, for example, Alist[i]==[j,k] represent two edges from i to j and i to k


#  In these the Adjency Dictionary 
#  To find the Neighbours of the vertix 
Alist = {}
for i in range(10):
    Alist[i] = []
for (i,j) in edges:
    Alist[i].append(j)
print(Alist)


'''Here we are Find the Neighbour of thr Vertix of the '''

def Neighbour(Amat,v):  # Note here Undirected Graph just Like the Arline Route Question
    nbrs = []
    (row,column) = Amat.shape
    for i in range(column):
        if Amat[v,i] == 1:
            nbrs.append(i)
    return nbrs
       
print(Neighbour(A,0))

"""Here there will be a problem is that these is Applicable for Only Undirect Graph there the Rows and the Columns are the Same"""