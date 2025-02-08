'''Selection Sort'''
''' Time Complexity is the Upper Bound O(n2)'''

# In Selection Sort, we keep updating the same list rather than creating a new one



def Selection_Sort(l):
    n = len(l)
    # If the List Have Only One or Empty list does not need to be Sort
    if n < 1:
        return(l)
    for i in range(n):
        # Assuem l[:i] is Sorted
        mposeA = i 
        
        #mpose : position of minimum in l[i:]
        
        for j in range(i+1,n):
        # Here we are Selcting the Value of i = 0 then  the range is from 1 to last Index of the List,
        # By the Help fo these loop we can find the min Value after the ith index 
            if l[j]< l[mpose]:
            # Here we are 
                mpose = j 
            
        # l[mpose] : smallest Value in l[i:]
        #Exchange l[mpose] and l[i]            
        l[i],l[mpose]= l[mpose],l[i]
        
    return(l)
            

l = [12,64,13,84,96]

print(Selection_Sort(l))