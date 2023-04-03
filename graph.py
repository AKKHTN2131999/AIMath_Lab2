from vertex import Vertex
from typing import Any, Text, List

from queue import Queue


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex

        return newVertex


    def getVertex(self, n):
        return self.vertList[n] if n in self.vertList else None


    def __contains__(self,n):
        return n in self.vertList


    def addEdge(self, f: Any, t: Any, weight: int =0):
        if f not in self.vertList:
            nv = self.addVertex(f)

        if t not in self.vertList:
            nv = self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], weight)


    def getVertices(self):
        return self.vertList.keys()


    def __iter__(self):
        return iter(self.vertList.values())


    def bfs(self, start: Vertex):
        start.setDistance(0)
        start.setPred(None)

        vertQueue = Queue()
        vertQueue.put(start)

        while vertQueue.qsize() > 0:
            currentVert = vertQueue.get()

            for nbr in currentVert.getConnections():
                if nbr.getColor() == 'white':
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)

                    vertQueue.put(nbr)

            currentVert.setColor('black')


    def dfs(self):
        time = 0

        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(None)

        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex, time)
    

    def dfsvisit(self, startVertex, time):
        startVertex.setColor('gray')
        time += 1
        startVertex.setDiscovery(time)

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                time = self.dfsvisit(nextVertex, time)

        startVertex.setColor('black')
        time += 1
        startVertex.setFinish(time)
        
        return time


    def traverse_dfs(self):
        for vertex in self:
            key = vertex.getId()
            pred = 'None' if vertex.getPred() is None else vertex.getPred().getId()
            discovery = vertex.getDiscovery()
            finish = vertex.getFinish()

            print("key: {}, pred: {}, discovery: {}, finish: {}".format(key, pred, discovery, finish))


    def traverse_bfs(self):
        for vertex in self:
            key = vertex.getId()
            pred = 'None' if vertex.getPred() is None else vertex.getPred().getId()
            distance = vertex.getDistance()

            print("key: {}, pred: {}, distance: {}".format(key, pred, distance))


def traverse(y: Vertex):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


if __name__ == '__main__':
    g = Graph()
    for i in range(9):
        g.addVertex(i)
    
    g.addEdge(0, 1)
    g.addEdge(1, 0)

    g.addEdge(0, 4)
    g.addEdge(4, 0)

    g.addEdge(1, 2)
    g.addEdge(2, 1)

    g.addEdge(1, 3)
    g.addEdge(3, 1)

    g.addEdge(2, 5)
    g.addEdge(5, 2)

    g.addEdge(3, 6)
    g.addEdge(6, 3)

    g.addEdge(6, 7)
    g.addEdge(7, 6)

    g.addEdge(6, 8)
    g.addEdge(8, 6)


    for v in g:
        for w in v.getConnections():
            print(f"( {v.getId()} , {w.getId()} )")

    g.dfs()
    g.traverse_dfs()

