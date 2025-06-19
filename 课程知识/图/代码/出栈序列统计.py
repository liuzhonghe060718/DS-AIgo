n=int(input())
ans=0
stack=[]
def dfs(k,idx):
    global ans
    if k==2*n:
        ans+=1
        return
    if stack:
        a=stack.pop()
        dfs(k+1,idx)
        stack.append(a)
    if idx<n+1:
        stack.append(idx)
        dfs(k+1,idx+1)
        stack.pop()
dfs(0,1)
print(ans)
