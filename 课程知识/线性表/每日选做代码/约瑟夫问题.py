while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    s=[i for i in range(1,n+1)]
    used=set()
    k=0
    idx=0
    while len(used)<len(s)-1:
        if s[idx%n] not in used:
            k+=1

        if k==m:
            used.add(s[idx%n])
            k=0
        idx += 1
    for x in set(s)-used:
        print(x)

