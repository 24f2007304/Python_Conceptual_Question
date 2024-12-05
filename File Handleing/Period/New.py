def add_period(filename):
    """
    Add a period at the end of each line

    Argument:
        filename: string; path of the file
    Return:
        None
    """
    with open(filename,"r")as f , open("oute.txt","w")as w:
        for line in f:
            w.write(f'{line.strip()}.\n')
            
print(add_period('scores.csv'))