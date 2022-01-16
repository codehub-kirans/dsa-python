##################################################################
##
##                       DOCUMENTATION
##
##################################################################
#
#
# @file	graphSearch.py
# @version	1
# @author	Kiran S
# @short	DFS & BFS for graphs
# Implementation of DFS and BFS Algorithms for undirected graphs
#
# <p>
# See GIT for detailed history.
# <p>
# Copyright (c) 2022 Kiran S. All rights reserved.
#
##################################################################

from collections import deque

class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.adjacentVertices = []
    
    def addAdjacentVertex(self, vertex):
        self.adjacentVertices.append(vertex)
        if self in vertex.adjacentVertices:
            return
        vertex.adjacentVertices.append(self)

    def dfsTraversal(self, vertex = None, visitedVertices = {}, vertices = []):
        currentVertex = vertex or self
        visitedVertices[currentVertex.value] = True
        vertices.append(currentVertex.value)

        for adjVertex in currentVertex.adjacentVertices:
            if visitedVertices.get(adjVertex.value) is None:
                self.dfsTraversal(adjVertex, visitedVertices, vertices)
        
        return vertices

    def bfsTraversal(self):
        queue = deque([]) # a deque with empty list
        visitedVertices = {}
        vertices = []

        visitedVertices[self.value] = True
        queue.append(self)
        vertices.append(self.value)

        try:
            while True:
                vertex = queue.popleft()
                for adjVertex in vertex.adjacentVertices:
                    if visitedVertices.get(adjVertex.value) is None:
                        visitedVertices[adjVertex.value] = True
                        queue.append(adjVertex)
                        vertices.append(adjVertex.value)
              
        except:
            return vertices

               

#Test
v1 = Vertex("Alice")
v2 = Vertex("Bob")
v3 = Vertex("Elaine")
v4 = Vertex("Ruth")

v1.addAdjacentVertex(v2)
v1.addAdjacentVertex(v4)
v2.addAdjacentVertex(v3)
v3.addAdjacentVertex(v4)

print(v1.dfsTraversal())
print(v1.bfsTraversal())



        

