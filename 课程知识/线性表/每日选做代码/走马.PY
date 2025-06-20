
n=int(input())
dire=[(-1,-2),(1,-2),(-2,-1),(2,-1),(-2,1),(2,1),(-1,2),(1,2)]


def bfs(p,q,x0, y0, idx, path,visited):
    if idx == p * q:
        return path
    for dx, dy in dire:
        nx, ny = x0 + dx, y0 + dy
        if 0 <= nx < p and 0 <= ny < q and not visited[nx][ny]:
            visited[nx][ny] = True
            s = bfs(p,q,nx, ny, idx + 1, path + places[ny] + str(nx + 1),visited)
            visited[nx][ny] = False
            if s:
                return s

    return False


for i in range(1,n+1):
    p0,q0=map(int,input().split())
    places='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    visited=[[False for _ in range(q0)]for _ in range(p0)]
    visited[0][0]=True
    ans=bfs(p0,q0,0,0,1,'A1',visited)
    print(f'Scenario #{i}:')
    print(ans if ans else 'impossible')
    if i!=n:
        print()