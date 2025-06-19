n,m=map(int,input().split())
graph=[0]*n
adj_matrix=[[0]*n for _ in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    adj_matrix[a][b]=1
    adj_matrix[b][a]=1
    graph[a]+=1
    graph[b]+=1
for i in range(n):
    ans=[]
    for j in range(n):
        if i==j:
            ans.append(graph[i]-adj_matrix[i][j])
        else:
            ans.append(-adj_matrix[i][j])
    print(' '.join(map(str,ans)))
    ans.clear()
