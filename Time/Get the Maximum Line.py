def get_Max_Line(filename):
    max_value = 0  # Here we are assign the Maximum value in the File
    max_value_lineNumber = 0 #Line Number of the Maximum Number
    
    with open(filename,"r") as f:
       for line_number , line in enumerate(f,start=1):
           try:
               line_count = int(line.strip())  # Here this is for Converting the linestrip into the Integer Value
               
           except ValueError:
               # It is for those who have not Integer Value
               continue
    if line_count>max_value:
                max_value = line_count
                max_value_lineNumber = line_number
            
    elif line_count == max_value:
                max_value_lineNumber =line_number
               
                
    return max_value_lineNumber
            
print(get_Max_Line("worde.text"))
               
       
            