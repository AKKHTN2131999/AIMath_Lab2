from vertex import Vertex

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0


    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex


    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None


    def __contains__(self,n):
        return n in self.vertList


    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)


    def getVertices(self):
        return self.vertList.keys()


    def __iter__(self):
        return iter(self.vertList.values())


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def bfs(self, start: Vertex):
        start.setDistance(0)
        start.setPred(None)
        vertQueue = []
        vertQueue.append(start)
        while (len(vertQueue) > 0):
            currentVert: Vertex = vertQueue.pop(0)
            for nbr in currentVert.getConnections():
                nbr: Vertex = nbr
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.append(nbr)
            currentVert.setColor('black')


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0


    def dfs(self):
        for aVertex in self:
            aVertex : Vertex = aVertex
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)


    def dfsvisit(
        self,
        startVertex: Vertex
        ):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            nextVertex:Vertex = nextVertex
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)
        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
        g.addEdge(0,1,5)
        g.addEdge(0,5,2)
        g.addEdge(1,2,4)
        g.addEdge(2,3,9)
        g.addEdge(3,4,7)
        g.addEdge(3,5,3)
        g.addEdge(4,0,1)
        g.addEdge(5,4,8)
        g.addEdge(5,2,1)
        for v in g:
            for w in v.getConnections():
                print("( %s , %s )" % (v.getId(), w.getId()))
