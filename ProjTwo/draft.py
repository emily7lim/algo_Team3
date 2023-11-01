# input graph G = (V, E) is stored in an array of adjacency lists and we  use  aminimizing heap for  the  priority  queue.  Implement the  Dijkstra’s algorithm

import numpy as np
import heapq

def addEdge(index, vertice, weight):
    adj[index].append((vertice,weight))
    # adj[vertice].append((index,weight))

def dijkstra(src):
    d = [np.inf for i in range(size)]
    print(adj)
    pq = []
    d[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        #choose according to weights thus weights in front
        vertex = heapq.heappop(pq)[1]
        # print(weights, vertex, adj[vertex],d)
        for i,j in adj[vertex]:
            # print(i,j,vertex,'AA')
            if d[i] > d[vertex] + j:
                d[i] = d[vertex]+j
                heapq.heappush(pq,(d[i],i))
    for i in range(size):
            print(f"{i} \t\t {d[i]}")
    # return d


size = 5
adj = [[] for _ in range(size)]

# addEdge(0, 1, 4)
# addEdge(0, 7, 8)
# addEdge(1, 2, 8)
# addEdge(1, 7, 11)
# addEdge(2, 3, 7)
# addEdge(2, 8, 2)
# addEdge(2, 5, 4)
# addEdge(3, 4, 9)
# addEdge(3, 5, 14)
# addEdge(4, 5, 10)
# addEdge(5, 6, 2)
# addEdge(6, 7, 1)
# addEdge(6, 8, 6)
# addEdge(7, 8, 7)
addEdge(0,2,10)
addEdge(0,1,5)
addEdge(1,2,3)
addEdge(1,3,9)
addEdge(1,4,2)
addEdge(2,3,1)
addEdge(2,1,2)
addEdge(3,4,4)
addEdge(4,0,7)
addEdge(4,3,6)
dijkstra(0)
# print(dijkstra(0))