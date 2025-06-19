class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
class Graph:
    def __init__(self,n):
        self.vertexlist={i:Vertex(i) for i in range(n)}
    def addEdge(self,f,t,weight=0):
        self.vertexlist[f].addNeighbor(self.vertexlist[t],weight)
n0,m0 =map(int,input().split())
graph=Graph(n0)
for i in range(m0):
    a,b=map(int,input().split())
    graph.addEdge(a,b)
    graph.addEdge(b,a)
for i in range(n0):
    ans=[]
    for j in range(n0):
        num=0
        if graph.vertexlist[j] in graph.vertexlist[i].connectedTo:
            num-=1
        if i==j:
            num +=len(graph.vertexlist[i].connectedTo)
        ans.append(num)
    print(' '.join(map(str,ans)))




