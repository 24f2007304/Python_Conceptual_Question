'Insertion Sort'

def Insertion_Sort(L):
    n = len(L)
    
    if n <1:
        return(L)
    
    for i in range(n):
        j =i 
        
        while(j>0 and L[j]<L[j-1]):
            (L[i],L[j-1]) = (L[j-1],L[i])
            j =j-1
            
    return(L)


Lis = [12,11,52,14,65]

print(Insertion_Sort(Lis))