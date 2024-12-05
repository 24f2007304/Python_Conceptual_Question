# Here we are going to make a file that can make a file by the help of given amount in the file which is Seperated by comma.

# def Matrix_maker(filename):
#     l=[]
#     with open(filename,"r") as f:
#         for linenumber , line in enumerate(f,start=1):
#             try:
#                 Number  = list(line.strip().split(","))
#                 for linenumber in f:
#                     l.append([])
#                     for j in Number:
#                         l[int(linenumber)].append(j)
#             except ValueError:
#                 continue
#     return l
               




# def Matrix_maker(filename):
#     matrix = []
#     with open(filename, "r") as f:
#         for line in f:
#             try:
#                 # Strip newline characters and split by commas to get the numbers
#                 numbers = line.strip().split(",")
#                 intNumber =[int(x)for x in numbers]
                
#                 # Append the list of numbers to the matrix
#                 matrix.append(intNumber)
#             except ValueError:
#                 continue
#     return matrix


def get_matrix(filename):
    """
    Convert the contents of the file into a matrix

    Argument:
        filename: string
    Return:
        matrix: list of lists
    """
    matrix = []
    with open(filename,"r")as f:
        for line in f:
            try:
                number = line.strip().split(",")
                alok = [int(x) for x in number]
                matrix.append(alok)
        
            except ValueError:
                continue
    return matrix

print(get_matrix("C:\Phython Files\Matrix.text"))     