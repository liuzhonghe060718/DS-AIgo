n,k=map(int,input().split())
l=[]
for _ in range(n):
    l.append(int(float(input())*100))
left=1
right=max(l)
def check(num):
    ans=0
    for i in l:
        ans+=i//num
    return ans>=k
while left<=right:
    mid=(left+right)//2
    if check(mid):
        left=mid+1
    else:
        right=mid-1
print(f"{right/100:.2f}" if right>=100 else '0.00')
