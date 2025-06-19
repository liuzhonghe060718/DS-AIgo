from collections import defaultdict, deque

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    if m<n-1:
        for i in range(m):
            input()
        print('Sorted sequence cannot be determined.')
        continue
    graph=defaultdict(list)
    nodes=set()
    result=False
    indegree = defaultdict(int)
    for i in range(1,m+1):
        s=input()
        graph[s[0]].append(s[2])
        nodes.add(s[0])
        nodes.add(s[2])
        indegree[s[2]]+=1
        stack=[]
        queue=deque()
        for u in nodes:
            if indegree[u]==0:
                queue.append(u)
        active=True
        indegrees=indegree.copy()
        while queue:
            if len(queue) != 1:
                active = False
            u=queue.popleft()
            stack.append(u)
            for v in graph[u]:
                indegrees[v]-=1
                if indegrees[v]==0:
                    queue.append(v)
        if len(stack)!=len(graph):
            for j in range(m-i):
                input()
            result=True
            print(f'Inconsistency found after {i} relations.')
            break
        if active and len(stack)==n:
            for j in range(m-i):
                input()
            ans=''.join(stack)
            result=True
            print(f'Sorted sequence determined after {i} relations: {ans}.')
            break
    if not result:
        print('Sorted sequence cannot be determined.')