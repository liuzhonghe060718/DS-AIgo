m,n,p,q=map(int,input().split())
matrix=[]
core=[]
for i in range(m):
    matrix.append(list(map(int,input().split())))
for i in range(p):
    core.append(list(map(int,input().split())))
ans=[[0 for _ in range(n+1-q)]for _ in range(m+1-p)]
for x in range(m+1-p):
    for y in range(n+1-q):
        for i in range(p):
            for j in range(q):
                ans[x][y]+=core[i][j]*matrix[x+i][y+j]
for i in range(m+1-p):
    print(' '.join(map(str,ans[i])))