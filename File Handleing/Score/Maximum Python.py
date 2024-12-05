'''Write a function named extract_lines that accepts filename as argument. Within the function, read the file and look for all male students who have scored at least 70 marks in Python. Copy these lines into a new file named python.csv. The entries in this file should be in the increasing order of sequence numbers. Also, the first line of python.csv should be the header, which is same as the one in filename.'''

def extract_lines(filename):
    with open(filename ,"r") as f, open("python.csv","w") as p:
        for linenumber,line in enumerate(f ,start=1):
            if linenumber >1:
                SeqNo,Name,Gender,CT,Python,PDSA = line.strip().split(",")
                if linenumber>1:
                    if Gender=="Male":
                        if int(Python)>70:
                            p.write(f'{line}/n')
    return "python.csv"
                          
print(extract_lines("C:\Phython Files\File Handleing\Score\Score Data Set.text"))  
            

        