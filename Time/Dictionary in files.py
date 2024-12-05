
def get_Dictionary(filename):
    d ={}
    with open(filename,"r") as f:
        for line_Number,line in enumerate(f,start=1):
            try:
                line_content = line.strip()
                if  line_Number >1:
                   Name ,age = line_content.split(",")
                   d[Name] = int(age)  
         
                  
            except ValueError:
                continue
    return d    
        # if  line_Number >1:
        #     Name ,age = line_content.split(",")
        #     d[Name] = age  
        # return d
    
print(get_Dictionary("C:\Phython Files\Time\Dictionary.text"))
            
            
