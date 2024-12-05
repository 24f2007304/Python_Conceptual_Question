import time

def Obvoues_search(l,n):
    '''Here we are Checking the k element is Present in L.
    This function is authored by Alok Tiwari'''
    for i in l:
        if i == n:
            return True
    return False

l = range(1000*1000*1000)

a =time.time()
print(Obvoues_search(l,-10 ))  # It takes approximately 1.856sec
b=time.time()
print(b-a)


'''Then we have how to structured a function that can be more faster'''
# Thats Search is called as Binary Search 

    