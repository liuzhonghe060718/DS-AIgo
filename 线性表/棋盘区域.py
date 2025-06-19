while True:
    n,k=map(int,input().split())
    if n==k==-1:
        break
    matrix=[''for _ in range(n)]
    for i in range(n):
        matrix[i]=input()
    ans=0
    visited=[[False for _ in range(n)]for _ in range(n)]
    def bfs(idx,pl):
        global ans
        if pl==k:
            ans+=1
            return
        if idx==n:
            return
        for j in range(n):
            if matrix[idx][j]=='#' and not visited[idx][j]:

                for q in range(idx+1,n):
                    visited[q][j]=True
                bfs(idx+1,pl+1)
                for q in range(idx + 1, n):
                    visited[q][j] = False
        bfs(idx+1,pl)
    bfs(0,0)
    print(ans)