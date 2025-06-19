import math
from collections import defaultdict
import heapq
hx,hy,sx,sy=map(int,input().split())
graph=defaultdict(list)
distance={(hx,hy):0,(sx,sy):math.sqrt((hx-sx)**2+(hy-sy)**2)/10}
def di(x1,y1,x2,y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)/1000
while True:
    try:
        nums=list(map(int,input().split()))
        for i in range(0,len(nums)-4,2):
            l=di(nums[i],nums[i+1],nums[i+2],nums[i+3])/40
            graph[(nums[i],nums[i+1])].append((nums[i+2],nums[i+3],l))
            graph[(nums[i+2]),nums[i+3]].append((nums[i],nums[i+1],l))
            distance[(nums[i],nums[i+1])]=float('inf')
        distance[(nums[-4],nums[-3])]=float('inf')
    except EOFError:
        break
for a in list(graph.keys()):
    graph[(hx,hy)].append((a[0],a[1],di(hx,hy,a[0],a[1])/10))
    graph[a].append((sx,sy,di(sx,sy,a[0],a[1])/10))
    for b in graph.keys():
        if b!=a:
            graph[a].append((b[0],b[1],di(a[0],a[1],b[0],b[1])/10))
heap=[(0,hx,hy)]
while heap:
    d,x0,y0=heapq.heappop(heap)
    if x0==sx and y0==sy:
        print(round(distance[(sx,sy)]*60))
        exit()
    if d>distance[(x0,y0)]:
        continue
    for vx,vy,w in graph[(x0,y0)]:
        if distance[(vx,vy)]>d+w:
            distance[(vx,vy)]=d+w
            heapq.heappush(heap,(distance[(vx,vy)],vx,vy))


