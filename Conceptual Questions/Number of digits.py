# Here we are count the no of digit
# n = int(input("Enter the Number:"))
# adsNum = abs(n)
# digit = 0
# while(adsNum>0):
#     adsNum = adsNum//10
#     digit = digit+1
# print(digit)

#  Here we try to find min number in the list
def max_list(l):
    min = l[0]
    for i in range(len(l)):
        if(l[i]>min):
          min = l[i]
    return min
#  Similarly we find max number in the list
# def max_list(l):
#    maxi = l[0]
#    for i in range(len(l)):
#       if(l[i]>maxi):
#          maxi = l[i]
#     return maxi
def min_list(l):
    min = l[0]
    for i in range(len(l)):
        if(l[i]<min):
          min = l[i]
    return min

# Here add all Element 
def add_list(l):
   add  = 0
   for i in range(len(l)):
     add = add + l[i]
   return add

# Here Substraction all Element
def Sub_list(l):
   add  = 0
   for i in range(len(l)):
     add = add - l[i]
   return add

# Here in the Multiple all Element
def Mul_list(l):
   Mul = 1
   for  i in range(len(l)):
      Mul = Mul*l[i]
      return Mul

l = [12,24,35,568,45,25,98]


print(min_list(l))

print(max_list(l))           

print(add_list(l)) 

print(Sub_list(l))


print(Mul_list(l))


