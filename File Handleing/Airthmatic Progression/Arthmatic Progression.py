'''You do not have to accept input from the console or print the output. You have to write the function definition. Within the function, create the file named out.txt.'''

'''Write a function named write_AP that accepts the following arguments:

a_1: first term of the AP, integer.
d: common difference of the AP, integer.
n: number of terms in the AP, positive integer.
Within the function, create a file named out.txt and write the first 
n
n terms of the AP to it, one term on each line, starting from the first term.'''

# Here if the we have to given a first integer and commom difference  and Number of Integers. write in file line by line

def arthmatic_progression(a:int,d:int,n:int):
    with open("Airthmatic Progression.text","w") as AP:
        for i in range(n):
            Term = (a+(i*d))
            AP.write(f'{Term}\n')  # Here it is for to write the term in the Next Line.
    return "Airthmatic Progression.text"

print(arthmatic_progression(12,1,5))
                
            