def Matrix_maker(filename):
    matrix = []
    with open(filename, "r") as f:
        for line in f:
            try:
                # Strip newline characters and split by commas to get the numbers
                numbers = line.strip().split(",")
                intNumber =[int(x)for x in numbers]
                
                # Append the list of numbers to the matrix
                matrix.append(intNumber)
            except ValueError:
                continue
    return matrix
