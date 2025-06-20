n=int(input())
find={}
files=set()
for i in range(n):
    s=list(input().split())
    pq=set(s[1:])
    find[i]=pq
    files|=pq
m=int(input())
for _ in range(m):
    require=list(input().split())
    not_in=set()
    i=0
    ans=files
    for j in range(n):
        if require[j]=='1':
            ans=ans&find[j]
        elif require[j]=='-1':
            not_in=not_in|find[j]
    ans=ans-not_in
    print(' '.join(sorted(list(ans))) if ans else 'NOT FOUND')
