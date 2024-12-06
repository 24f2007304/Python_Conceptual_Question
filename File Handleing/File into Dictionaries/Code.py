'''Write a function named get_dict that accepts the filename as argument and returns a dictionary where the keys are the student names and the values are the corresponding ages of the students'''

def get_Dictionary(filename):
    D={}
    with open(filename,"r")as f: # Here we are opening the file 
        for linenumber,line in  enumerate(f,start=1): # Here we are start counting from 1.
            if linenumber>1: # If the LineNumber is greater than 2
                Name,Age =line.strip().split(",") # Here line split by comma
                D[Name]=Age # We define the Dictionary
        return D
    
print(get_Dictionary("C:\Phython Files\File Handleing\File into Dictionaries\Dictionary .text"))