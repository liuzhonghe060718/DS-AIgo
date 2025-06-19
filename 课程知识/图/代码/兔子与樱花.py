p=int(input())
graph={}
for _ in range(p):
    graph[input()]={}
q=int(input())
for _ in range(q):
    a,b,distance=input().split()
    graph[a][b]=int(distance)
    graph[b][a]=int(distance)
r=int(input())
def find_lowest_node(costs,processed):
    lowest_cost=float('inf')
    lowest_cost_node=None
    for node in costs:
        cost=costs[node]
        if cost<lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node
    return lowest_cost_node
for i in range(r):
    start,end=input().split()
    process=[]
    mcosts={}
    parents={}
    for node in graph.keys():
        mcosts[node]=float('inf')
    for key,value in graph[start].items():
        mcosts[key]=value
        parents[key]=start

    node=find_lowest_node(mcosts,process)
    while node is not None:
        cost=mcosts[node]
        for n in graph[node].keys():
            new_cost=cost+graph[node][n]
            if mcosts[n]>new_cost:
                mcosts[n]=new_cost
                parents[n]=node
        process.append(node)
        node=find_lowest_node(mcosts,process)
    ans=[]
    now=end
    while now!=start:
        ans.append(now)
        now=parents[now]
    ans.append(start)
    ans.reverse()
    result=ans[0]
    for j in range(1,len(ans)):
        result+='->('+str(graph[ans[j-1]][ans[j]])+')->'+ans[j]
    print(result)