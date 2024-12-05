'''Write a function named improvement which accepts the filename as argument. It should return the number of students whose scores have increased across the three courses. That is, the number of students whose scores are in this order: CT < Python < PDSA.'''

def improvement(filename):
    count=0
    with open(filename)as f:
        for linenumber,line in enumerate(f , start =1):
            try:   
                if linenumber>1:
                    SeqNo,Name,Gender,CT,Python,PDSA = line.strip().split(",")
                    if int(CT)<int(Python)<int(PDSA):
                         count+=1
            except ValueError:
                continue 
    return count

print(improvement("C:\Phython Files\oute.txt  "))
                    
