n,k=map(int,input().split())
l1=[]
for i in range(1,n+1):
    a,b=map(int,input().split())
    l1.append((a,b,i))
l1.sort(reverse=True)
l2=l1[:k].copy()
l2.sort(key=lambda x:x[1],reverse=True)
print(l2[0][2])
