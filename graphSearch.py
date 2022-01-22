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
# @short	DFS, BFS & shortest Path for undirected graphs
# Implementation of DFS, BFS & Shortest Path Algorithms for undirected graphs
#
# <p>
# See GIT for detailed history.
# <p>
# Copyright (c) 2022 Kiran S. All rights reserved.
#
##################################################################

from collections import deque
import queue
from tracemalloc import start

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

        while queue:
            vertex = queue.popleft()
            for adjVertex in vertex.adjacentVertices:
                if adjVertex.value not in visitedVertices:
                    visitedVertices[adjVertex.value] = True
                    queue.append(adjVertex)
                    vertices.append(adjVertex.value)

        return vertices

def shortestPath(startingVertex, endingVertex):
    queue = deque()
    visitedVertices = {}
    shortestPreviousVertex = {}

    visitedVertices[startingVertex] = True
    queue.append(startingVertex)

    while queue:
        currentVertex: Vertex = queue.popleft()
        for adjVertex in currentVertex.adjacentVertices:
            if adjVertex not in visitedVertices:
                visitedVertices[adjVertex] = True
                queue.append(adjVertex)
                shortestPreviousVertex[adjVertex] = currentVertex

    currentVertex = endingVertex
    shortestPath = []

    while currentVertex != startingVertex:
        shortestPath.append(currentVertex.value)
        currentVertex = shortestPreviousVertex[currentVertex]
    
    shortestPath.append(currentVertex.value)
    shortestPath.reverse()

    string = "Shortest Path between " + startingVertex.value + " and " + endingVertex.value + " is " + ", ".join(shortestPath)

    return string

#Test
v1 = Vertex("Kiran")
v2 = Vertex("Amar")
v3 = Vertex("Madhu")
v4 = Vertex("Ajay")

v1.addAdjacentVertex(v2)
v1.addAdjacentVertex(v4)
v2.addAdjacentVertex(v3)
v3.addAdjacentVertex(v4)

print(v1.dfsTraversal())
print(v1.bfsTraversal())
print(shortestPath(v1,v3))