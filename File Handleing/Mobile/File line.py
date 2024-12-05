''' Herev we are print the output line from a file and if the number of line is exceded from it print None'''


def File_line(filename , n):
    with open(filename,"r")as f:
        for lineNumber,line in enumerate(f,start =1):
            if lineNumber == n:
                value = int(line.strip())
                return f'{line.strip()} and {value}'
        return None
    
print(File_line("C:\Phython Files\File Handleing\myalok.text",1))