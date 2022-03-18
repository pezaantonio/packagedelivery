#
# Antonio Peza
# C950 Data Structures & Algorithms 2
# Graph class to store adjacency list
#
import csv

distanceFile = "wgups/distancedata.csv"

class Node:
    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.prevVertex = None
    
class Graph:
    def __init__(self):
        self.adjacencyList = {}
        self.edgeWeights = {}
    
    def addVertex(self, newVertex):
        self.adjacencyList[newVertex] = []
    
    def addDirectedEdge(self, fromVertex, toVertex, weight = 0):
        self.edgeWeights[(fromVertex, toVertex)] = weight
        self.adjacencyList[fromVertex].append(toVertex)

    def addUndirectedEdge(self, fromVertex, toVertex, weight = 0):
        self.addDirectedEdge(fromVertex, toVertex, weight)
        self.addDirectedEdge(toVertex, fromVertex, weight)


graph = Graph()