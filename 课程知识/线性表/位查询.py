n,m=map(int,input().split())
nums=list(map(int,input().split()))
def check(i):
    k=0
    i=int(i)
    for num in nums:
        s=bin(num)
        if len(s)>i+2 and  s[-i-1]=='1':
            k+=1
    return k
def ad(d):
    d=int(d)
    for j in range(n):
        nums[j]=(nums[j]+d)%65536
for _ in range(m):
    kind,number=input().split()
    if kind=='C':
        ad(number)
    else:
        print(check(number))