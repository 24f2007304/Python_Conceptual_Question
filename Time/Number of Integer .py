"""
    Get the line that houses the maximum value

    Argument:
        filename: string, path to the file
    Return:
        result: integer
    """

def No_Integer_Line(filename,n):
    count=0
    with open(filename,"r") as f:
        for linenumber , line in enumerate(f,start=1):
            if linenumber == n:
                line_Content = line.strip()
                break
            else:
                return f'There will be less Number in the File.'
        for i in line_Content:
            if i in  ['1','2','3','4','5','6','7','8','9','0']:
                count +=1
        return count
    
print(No_Integer_Line("worde.text",1))
           
            
        
    

                

