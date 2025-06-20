import math
while True:
    m,n=map(int,input().split())
    if m==n==0:
        break
    ans=0
    x=int(math.log(n,2))
    y=int(math.log(m,2))
    h=x-y
    ans+=2**(h+1)-1
    left=m*(2**h)
    right=left+2**h-1
    if n>right:
        print(ans)
    elif n<left:
        print(2**h-1)
    else:
        print(ans-(right-n))




