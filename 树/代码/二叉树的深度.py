n=int(input())
x=0
s={i:1 for i in range(n)}
ans=1
leaves=[]
for i in range(n):
    l,r=map(int,input().split())
    if l==r==-1:
        x+=1
    leaves.append(l)
    leaves.append(r)
root={i for i in range(n)}-set(leaves)
for i in range(n):
    l=leaves[i*2]
    r=leaves[i*2+1]
    if l!=-1:
        s[l]=s[i]+1
        ans=max(ans,s[l])
    if r!=-1:
        s[r]=s[i]+1
        ans = max(ans, s[r])
if n==1:
    print('0 1')
elif n==2:
    print('1 1')
else:
    print(str(ans-1)+' '+str(x))

