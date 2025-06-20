from collections import deque
while True:
    n,p,m=map(int,input().split())
    if m==n==p==0:
        break
    queue=deque([i for i in range(p,n+1)]+[i for i in range(1,p)])
    ans=[]
    while queue:
        idx=1
        while idx<m:
            queue.append(queue.popleft())
            idx+=1
        ans.append(queue.popleft())
    print(','.join(map(str,ans)))