# Here we are Solving Question from the Image
  
def findComponenets_undirectedGraph(vertices , edges):
    # Create an Adjency list using a normal dictionary
    graph = {}
    for v in vertices:
        graph[v] = [] #Intialize an empty list for each vertex
        
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = set()
    components = 0
    
    # DFS function
    def DFS(node):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(graph[current])
                
                
    #Count the number of connected components
    for vertex in vertices:
        if vertex not in visited:
            components += 1
            DFS(vertex)
    
    return components

# Example Usage

vertices =[1,2,3,4,5,6,7,8]

edges = [(1,3),(3,4),(3,7),(5,6),(5,8),(6,8)]

print(findComponenets_undirectedGraph(vertices,edges)) # 3
# 1-3-4-7
# 2
# 5-6-8

    
    
