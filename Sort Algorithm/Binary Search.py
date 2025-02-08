'''Here we are Disscus about the Binary Search'''


'''But, For the Binary Search List Must Be Sorted in Asending Order'''

'''Time Commplixity is the Upper Bound O(logn)'''


def Binary_Search(L,v):
    if L ==[]:  # Here it will return the False When the No Element will be there . Thats Because the we are removing
        return(False)
    m = len(L)//2
      # For Mid Point
    if v == L [m]:
        return(True)
      # For every middle Element we see that this is v are not
    
    if v < L [m]:
        return(Binary_Search(L[:m],v))
      # Here we are searching  in the First Half
    
    else :
        return(Binary_Search(L[m+1:],v))
       
       # Here we are searchng for the Second Half
       
       
