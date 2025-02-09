# Here we are going to Deal with Deapth First Search and 
# These Search not be in the Level wise andbut the Node 

#  Here we use the Stack that means and there will be the First in Last Out

'''Stack Implementation'''

class Stack:
    def __init__(self):
        self.stack = []
        
    def Push(self,a):
        self.stack.append(a)
        
    def is_empty(self):
        return(self.stack == [])
    
    def pop(self):
        v = None #Intialise the v is None
        if not self.is_empty( ): # In these Code that means that for excation for these block is_empty must be False or not(False) is True
            v = self.stack.pop()
        return(v)
    
    def __str__(self):
        return(str(self.stack))
    
    
#  Here we are going to be Define the Function of the Adjency List

def DFSList(AList,start_vertex):
    #  Intialization
    
    visited = {}
    
    for each_vertex in AList.keys():
        visited[each_vertex] = False
        
    # Create stack Object st
    
    st = Stack()
    
    # Push start_vertex in the stack as First vertex
    st.Push(start_vertex)
    
    # Reapte the Stack Until the Stack is empty
    
    while(not st.is_empty()):
        # Pop the vertex from Stack
        
        current_vertex = st.pop()
        #  If popped vertex is not visited marked visited
        if visited[current_vertex]==False:
            visited[current_vertex] =True
            # Push all unvisited adjecent of popped vertex into the Stack
            
            for adj_vertex in AList[current_vertex]:
                if(not visited[adj_vertex]):
                    st.Push(adj_vertex)
                
    return visited

AList = {0:[1,2],1:[1,4],2:[4,3],3:[4],4:[]}
print(DFSList(AList,0))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    