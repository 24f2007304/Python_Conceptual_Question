# def get_scores(filename, index):
#     f = open(filename, 'r')
#     # Ignore the header
#     f.readline()	
#     # we are now at the beginning of the second line of the file
    
#     scores = [ ]
#     line = f.readline()
#     while line != '':
#         L = line.strip().split(',')
#         scores.append(int(L[index]))
#         line = f.readline()
    
#     f.close()
#     return scores

# print(get_scores("scores.csv",4))



# def do_something(L):
#     L.sort()
#     mid = len(L) // 2
#     if len(L) % 2 == 0:
#         return (L[mid] + L[mid - 1]) // 2
#     else:
#         return L[mid]
    
# print(do_something(get_scores('scores.csv', 4)))

# print((70+95)//2)

def do_something(infile, gender, outfile):
    f = open(infile, 'r')
    g = open(outfile, 'w')
    header = f.readline()
    # we are now at the beginning of the second line of the file
    # 'good,M,great'.replace(',M,', ',')
    # returns 'good,great'
    header = header.replace(',Gender,', ',')
    g.write(header)
    
    for line in f.readlines():
        fields = line.strip().split(',')
        gender_in_file = fields[2]
        if gender_in_file == gender:
            out_line = line.replace(f',{gender},', ',')
            g.write(out_line)
    
    f.close()
    g.close()
    
do_something('scores.csv', 'F', 'out.csv')