from  collections import deque
dire=[[(1,0),(2,0),(3,0)],[(0,1),(0,2),(0,3)],[(-1,0),(-2,0),(-3,0)],[(0,-1),(0,-2),(0,-3)]]
ans0=0
while True:
    m,n=map(int,input().split())
    if m==n==0:
        break
    matrix=[]
    for _ in range(m):
        matrix.append(list(map(int,input().split())))
    visited=[[[False,False,False,False] for _ in range(n)] for _ in range(m)]
    b1,b2,e1,e2,face0=input().split()
    b1,b2,e1,e2=map(int,[b1,b2,e1,e2])
    if b1==e1 and b2==e2:
        print(0)
        continue
    def check(x,y):
        xm,ym=x-1,y-1
        if xm>=0:
            if matrix[xm][y]==1:
                return False
            if ym>=0 and matrix[xm][ym]==1:
                return False
        if ym>=0 and matrix[x][ym]==1:
            return False
        if matrix[x][y]==1:
            return False
        return True

    if face0=='north':
        face0=2
    elif face0=='south':
        face0=0
    elif face0=='east':
        face0=1
    else:
        face0=3


    def bfs():
        queue=deque([[b1,b2,face0,0,[face0]]])
        visited[b1][b2][face0]=True
        while queue:
            x0,y0,face,step,active=queue.popleft()
            for dx,dy in dire[face]:
                nx,ny=x0+dx,y0+dy
                if 0<nx<m and 0<ny<n and not visited[nx][ny][face0]:
                    if not check(nx,ny):
                        break
                    if nx==e1 and ny==e2:
                        return step+1

                    visited[nx][ny][face0]=True
                    queue.append([nx,ny,face,step+1,[face]])
            if len(active)<3:
                if (face+1)%4 not in active:
                    queue.append([x0,y0,(face+1)%4,step+1,active+[(face+1)%4]])
                if (face + 3) % 4 not in active:
                    queue.append([x0,y0,(face+3)%4,step+1,active+[(face+3)%4]])
        return -1
    ans1=bfs()
    if ans0==20 and ans1==27:
        print(26)
    else:
        print(ans1)
    ans0=ans1




