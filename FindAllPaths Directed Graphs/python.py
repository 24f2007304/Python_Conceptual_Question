# Solve the Given Question

def findAllPaths(vertices,glist,source,destination):
    stack =[(source,[source])]
    allpath = []
    
    while stack :
        node,path = stack.pop()
        
        if node == destination:
            allpath.append(path)
            continue
        
        if node in glist:
            for neigbour in glist[node]:
                if neigbour not in path:
                    stack.append((neigbour,path+[neigbour]))
                    
    return allpath

vertices = [1, 2, 3, 4, 5, 6, 7, 8]
gList = {
    1: [3, 4],
    2: [3],
    3: [6],
    4: [6, 7],
    5: [4, 6],
    6: [2],
    7: [5]
}
source = 1
destination = 2
print(findAllPaths(vertices, gList, source, destination)) # [[1, 3, 6, 2], [1, 4, 6, 2]]
        
    
