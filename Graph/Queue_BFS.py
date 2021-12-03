class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeue = queue.pop(0)
            print(dequeue)
            for adjacentVertex  in self.gdict[dequeue]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            dequeue = stack.pop()
            print(dequeue)
            for adjacentVertex in self.gdict[dequeue]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

customdict= {"a": ["b", "c"],
             "b": ["d", "e"],
             "c": ["e"],
             "d": ["e", "f"],
             "e": ["f"],
             "f": ["d", "e"]
             }

graph = Graph(customdict)
graph.dfs("a")
#print(graph.gdict)