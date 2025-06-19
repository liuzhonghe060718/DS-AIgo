k=int(input())
for _ in range(k):
    m,n=map(int,input().split())
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    I,J=map(int,input().split())
    p=int(input())
    nodes=[]
    for i in range(p):
        nodes.append(tuple(map(int,input().split())))
