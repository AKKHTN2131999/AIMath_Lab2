class Vertex:
    def __init__(
        self,
        key,
        ):
        self.id = key
        self.connectedTo = {}

    
    def getDistance(self):
        return self.distance

    def getPred(self):
        return self.pred

    def getColor(self):
        return self.color

    def setDistance(self, distance):
        self.distance = distance

    def setPred(self, pred ):
        self.pred = pred

    def setColor(self, color: str):
        self.color = color

    def setDiscovery(self, discovery):
        self.discovery = discovery

    def setFinish(self, finish):
        self.finish = finish

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight


    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])


    def getConnections(self):
        return self.connectedTo.keys()


    def getId(self):
        return self.id


    def getWeight(self,nbr):
        return self.connectedTo[nbr]


