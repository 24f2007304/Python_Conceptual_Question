''' Recursion By Useig the Recursion'''

def sum_rec(l):
    if len(l)==0:  # At we going to last element then it will give a 0 that we are adding to the l[0] and return it..
        return 0
    return l[0] + sum_rec(l[1:])
        
    # l =[1,2,3,4]
    #1+sum[2,3,4]
print(sum_rec([12,23]))
