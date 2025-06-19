#15:11-15:30
a,b,k=map(int,input().split())
matrix=[[True for _ in range(b)]for _ in range(a)]
now_mx=matrix
now_range=[0,a-1,0,b-1]
for _ in range(k):
    r,s,p,t=map(int,input().split())
    r-=1
    s-=1
    l=(p-1)//2
    boom=(max(r-l,0),min(a-1,r+l),max(0,s-l),min(b-1,s+l))
    if t==0:
        for x in range(max(now_range[0],boom[0]),min(now_range[1],boom[1])+1):
            for y in range(max(now_range[2],boom[2]),min(now_range[3],boom[3])+1):
                matrix[x][y]=False
    else:
        now_range[0]=max(now_range[0],boom[0])
        now_range[1]=min(now_range[1],boom[1])
        now_range[2] = max(now_range[2], boom[2])
        now_range[3] = min(now_range[3], boom[3])
ans=0
for i in range(now_range[0],now_range[1]+1):
    for j in range(now_range[2],now_range[3]+1):
        if matrix[i][j]:
            ans+=1
print(ans)
