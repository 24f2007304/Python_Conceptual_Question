import time
''' Here we have Binary Search that is the Fastest Way to Search on Shorted List'''

def Binary_Search(l,k):
    # Here we are Defining the Begining of Shorted List.
    begin = 0
    # Here we Define the End of the Shorted List..
    end = len(l)-1
    
    while(end-begin >10):
        mid = (begin+end)//2
        ''' Here we are Define the mid of the List '''
        if(l[mid]==k):  # If the k is in the Middle of the List.
            return True
        if(l[mid]>k): # If the k is in the left side of the list.
            end = mid-1
        if(l[mid]<k): # If the k is in the Right side of the List.
            begin=mid+1
            
            ''' Here we are going to the if the while condition is false .Just like if the List is [2,2] that means the end - begin is equalt to 0 and it became -1 if list is not shorted..'''
    if (begin ==k) or (end ==k):
        return True
    else:
        return False
    

l = range(1000*1000*1000)

a =time.time()
print(Binary_Search(l,-10))  # It takes 0.0 sec
b=time.time()
print(b-a)