from collections import deque


class Vertex:
    def __init__(self,key):
        self.id=key
        self.connectedTo={}
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr]=weight
    def __repr__(self):
        return self.id
class Graph:
    def __init__(self):
        self.vertexlist={}
        self.number=0
    def addVertex(self,key):
        self.number+=1
        self.vertexlist[key]=Vertex(key)
        return self.vertexlist[key]
    def addEdge(self,f,t,weight=0):
        if f not in self.vertexlist:
            self.addVertex(f)
        if t not in self.vertexlist:
            self.addVertex(t)
        self.vertexlist[f].addNeighbor(self.vertexlist[t],weight)

def build_graph(all_words):
    buckets={}
    the_graph=Graph()
    for word in all_words:
        for i,_ in enumerate(list(word)):
            bucket=f'{word[:i]}_{word[i+1:]}'
            buckets.setdefault(bucket,set()).add(word)
    for similar_words in buckets.values():
        for word1 in similar_words:
            for word2 in similar_words-{word1}:
                the_graph.addEdge(word2,word1)
    return the_graph
def bfs(start,target):
    visited={start}
    queue=deque([[start,[start.id]]])
    while queue:
        vertex,path=queue.popleft()
        for nxt_x in vertex.connectedTo.keys():
            if nxt_x.id == target:
                return path+[target]
            if nxt_x not in visited:
                visited.add(nxt_x)
                queue.append([nxt_x,path+[nxt_x.id]])
    return ['NO']
n=int(input())
words=[]
for _ in range(n):
    words.append(input())
start0,target0=input().split()
graph=build_graph(words)
start0=graph.vertexlist[start0]
print(' '.join(bfs(start0,target0)))




