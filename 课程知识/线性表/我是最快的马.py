#13:13-13:49
from collections import deque
start_x,start_y=map(int,input().split())
fin_x,fin_y=map(int,input().split())
m=int(input())
places=set()
for _ in range(m):
    places.add(tuple(map(int,input().split())))
queue=deque([[start_x,start_y,'('+str(start_x)+','+str(start_y)+')',0,{(start_x,start_y)}]])


ans=[[],0,0]
dire=[(1,2),(1,-2),(-1,2),(-1,-2),(2,-1),(2,1),(-2,-1),(-2,1)]
while queue:
    x0,y0,path,step,visited=queue.popleft()
    if ans[0]:
        if step>ans[1]:
            break


    for dx,dy in dire:
        nx,ny=x0+dx,y0+dy
        if 0<=nx<11 and 0<=ny<11 and (nx,ny) not in visited and (x0+dx//2,y0+dy//2) not in places:
            if nx == fin_x and ny == fin_y:
                if not ans[0]:
                    ans = [path + '-(' + str(nx) + ',' + str(ny) + ')', step+1, 1]
                else:
                    ans[2] += 1
            else:
                visited0=visited.copy()
                visited0.add((nx, ny))
                queue.append([nx, ny, path + '-(' + str(nx) + ',' + str(ny) + ')', step + 1,visited0])

if ans[2]==1:
    print(ans[0])
else:
    print(ans[2])



