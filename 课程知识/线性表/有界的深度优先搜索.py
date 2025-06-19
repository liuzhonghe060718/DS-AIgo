n,m,L=map(int,input().split())
graph={i:[] for i in range(n)}
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
start=int(input())
ans=[str(start)]
visited=set()
visited.add(start)
def dls(node,depth):
    if depth>=L:
        return
    for x in sorted(graph[node]):
        if x not in visited:
            visited.add(x)
            ans.append(str(x))
            dls(x,depth+1)
dls(start,0)
print(' '.join(ans))
