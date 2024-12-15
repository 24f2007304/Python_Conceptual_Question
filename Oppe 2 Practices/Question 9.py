'''Write a function named write_AP that accepts the following arguments:

a_1: first term of the AP, integer.
d: common difference of the AP, integer.
n: number of terms in the AP, positive integer.
Within the function, create a file named out.txt and write the first 
n
n terms of the AP to it, one term on each line, starting from the first term'''

def write_AP(a_1,d,n):
    with open('out.txt',"w")as f:
        for i in range(1,n+1):
            Term = (a_1 + (i*d))
            f.write(f'{Term}\n') # We Should Know to Write Output to next Line we use the /n and f we use forward Slasse''
            
    return f

print(write_AP(1,2,3))

