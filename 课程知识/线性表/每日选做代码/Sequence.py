import heapq
T=int(input())
for _ in range(T):
    m,n=map(int,input().split())
    lst1=sorted(map(int, input().split()))
    for _ in range(m-1):
        lst2=sorted(map(int, input().split()))
        heap=[lst1[i]+lst2[j] for i in range(n//2+1) for j in range(n//2+1)]
        heap.sort()
        lst1=heap[:n]
    print(' '.join(map(str,lst1)))








