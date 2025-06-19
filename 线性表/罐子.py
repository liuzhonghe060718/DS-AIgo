from collections import deque
a,b,c=map(int,input().split())
queue=deque([(0,0,[])])
visited=set()
while queue:
    watera,waterb,path=queue.popleft()
    if watera==c or waterb==c:
        print(len(path))
        for x in path:
            print(x)
        exit()
    for i in range(3):
        if i==1:
            if watera<a and (a,waterb) not in visited:
                visited.add((a,waterb))
                queue.append((a,waterb,path+['FILL(1)']))
            if waterb < b and (watera, b) not in visited:
                visited.add((watera, b))
                queue.append((watera, b, path + ['FILL(2)']))
        elif i==2:
            if (0,waterb) not in visited:
                visited.add((0,waterb))
                queue.append((0,waterb,path+['DROP(1)']))
            if (watera,0) not in visited:
                visited.add((watera,0))
                queue.append((watera,0,path+['DROP(2)']))
        else:
            if a-watera>=waterb and (watera+waterb,0) not in visited:
                visited.add((watera+waterb,0))
                queue.append((watera+waterb,0,path+['POUR(2,1)']))
            elif a-watera<waterb and (a,waterb-a+watera) not in visited:
                visited.add((a,waterb-a+watera))
                queue.append((a,waterb-a+watera,path+['POUR(2,1)']))
            if b-waterb>=watera and (0,watera+waterb) not in visited:
                visited.add((0,waterb+watera))
                queue.append((0,waterb+watera,path+['POUR(1,2)']))
            elif b-waterb<watera and (watera-b+waterb,b) not in visited:
                queue.append((watera-b+waterb,b,path+['POUR(1,2)']))



print('impossible')