n=int(input())
docu={}
for i in range(1,n+1):
    docu[i]=set((input().split()))
m=int(input())
for _ in range(m):
    ans=[]
    word=input()
    for i in range(1,n+1):
        if word in docu[i]:
            ans.append(str(i))
    print(' '.join(ans) if ans else 'NOT FOUND')
