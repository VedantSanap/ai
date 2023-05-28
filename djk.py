import sys
  
  
class Graph():
  
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
  
    def printSolution(self, dist, parent):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])
            
        print("edges included: ")
        for i in range(1,self.V):
            print(parent[i], "-", i, "\t") 
            
    def minDistance(self, dist, sptSet):
  
        
        min = sys.maxsize
  
        
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
  
        return min_index
  
 
    def dijkstra(self, src):
  
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        parent = [None] * self.V
  
        for cout in range(self.V):
  
          
            x = self.minDistance(dist, sptSet)
  
            sptSet[x] = True
  
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    parent[y] = x
  
        self.printSolution(dist,parent)
  

if __name__ == "__main__":
    g = Graph(6)
    g.graph=[ [0, 1, 4, 0, 0, 0],
              [1, 0, 4, 2, 7, 0],
              [4, 4, 0, 3, 5, 0],
              [0, 2, 3, 0, 4, 6],
              [0, 7, 5, 4, 0, 7],
              [0, 0, 0, 6, 7, 0] ];
    g.dijkstra(0)