#  Here First we have to Define tthe Queue Data Sturcutre
#  Here It Work on the Property Called that First in First Out
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, a):
        self.queue.append(a)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            return None  # or raise an exception

    def is_empty(self):
        return len(self.queue) == 0
    
    

# BFS Implemenation for Adjacency List

def BFSList(Alist,start_vertex):
    # Initialization
    
    visited = {}
    
    for i in Alist.keys():
        visited[i] = False
        
#  Create Queue Object

    q = Queue()

#  Mark the start_vertex visited and insert it into the Queue
    visited[start_vertex]= True
    q.enqueue(start_vertex)  # Here we are Appending the  start vertex in the  Queue List
    
    # Repeat the following until the queue is empty
    while( not q.is_empty()):
        # Remove the one vertex in the Queue
        curr_vertex = q.dequeue()
        #  visits each adjencent of the remove vertex(if not visted) , mark that visited , and insert it into the Queue
        for adj_vertex in Alist[curr_vertex]:
            if(not visited[adj_vertex]):
                visited[adj_vertex] = True
                q.enqueue(adj_vertex)
    return(visited)
    
    
Alist = {0: [1, 4], 1: [2], 2: [0], 3: [4, 6], 4: [0, 3, 7], 5: [3, 7], 6: [5], 7: [4, 8], 8: [5, 9], 9: [8]}
print(BFSList(Alist,0))

"""Write an Algorithum in the  Adjency Matrix Form """

        