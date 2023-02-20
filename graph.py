from vertex import Vertex
from typing import Any, Text, List

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.time = 0


    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex


    def getVertex(self,n):
        return self.vertList[n] if n in self.vertList else None


    def __contains__(self,n):
        return n in self.vertList


    def addEdge(
        self,
        f: Any,
        t: Any,
        weight: int =0):
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
        vertQueue = self._extracted_from_dfs_2(start)
        while vertQueue:
            currentVert: Vertex = vertQueue.pop(0)
            for nbr in currentVert.getConnections():
                nbr: Vertex = nbr
                if (nbr.getColor() == 'white'):
                    self._extracted_from_dfs_10(nbr, currentVert, vertQueue)
            currentVert.setColor('black')

    def dfs(self, start: Vertex):
        vertStack = self._extracted_from_dfs_2(start)
        step = -1
        while vertStack:
            currentVert: Vertex = vertStack.pop(-1)
            step+=1
            for nbr in currentVert.getConnections():
                nbr: Vertex = nbr
                nbr.setDiscovery(step)
                if (nbr.getColor() == 'white'):
                    self._extracted_from_dfs_10(nbr, currentVert, vertStack)
            currentVert.setColor('black')
            step+=1
            currentVert.setFinish(self.time)

    # TODO Rename this here and in `bfs` and `dfs`
    def _extracted_from_dfs_2(self, start):
        start.setDistance(0)
        start.setPred(None)
        return [start]

    # TODO Rename this here and in `bfs` and `dfs`
    def _extracted_from_dfs_10(self, nbr, currentVert, arg2):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        arg2.append(nbr)


#Build word graph 
def buildGraph(wList):
    d = {}
    g = Graph()
    #phân hoạch các từ cùng độ dài chỉ khác nhau 1 ký tự
    for line in wList: #lấy từng từ trong từ điển
        word = line[:-1]
        for i in range(len(word)):
            bucket = f'{word[:i]}_{word[i + 1:]}'
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    #thêm các đỉnh và các cạnh cho các từng trong cùng bucket
    for bucket in d:
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g

def traverse(y:Vertex):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0,1)
    g.addEdge(0,4)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,6)
    g.addEdge(3,5)
    g.addEdge(6,7)
    g.addEdge(6,8)
    for v in g:
        for w in v.getConnections():
            print(f"( {v.getId()} , {w.getId()} )")

    g.dfs(g.getVertex(0))
    traverse(g.getVertex(6))

