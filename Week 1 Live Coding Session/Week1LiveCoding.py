# Write a function shuffle(l1,l2) that takes two lists, l1 and l2 as input, and returns a list consisting of the first element in l1, then the first element in l2, then the second element in l1, then the second element in l2, and so on. If the two lists are not of equal length, the remaining elements of the longer list are appended at the end of the shuffled output.

def shuffle(l1,l2):
    List = l1 +l2
    List.sort()
    return List

print(shuffle([12,25,35,1,3,25],[15,51,12,15]))