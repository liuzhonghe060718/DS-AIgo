class Dir:
    def __init__(self,name):
        self.name=name
        self.children=[]
k=1
def show_dir(curdir,l):
    print('|     '*l+curdir.name)
    content=[]
    for y in curdir.children:
        if isinstance(y,str):
            content.append(y)
        else:
            show_dir(y,l+1)
    for filem in sorted(content):
        print('|     ' * l + filem)
while True:
    stack=[]
    files,dirs=[],[]
    first_file=input()
    if first_file=='#':
        break
    if k!=1:
        print()
    if first_file[0]=='d':
        stack.append(Dir(first_file))
    else:
        files.append(first_file)
    while True:
        file=input()
        if file=='*':
            break
        if stack:
            if file[0]=='f':
                stack[-1].children.append(file)
            elif file[0]=='d':
                now_dir=Dir(file)
                stack[-1].children.append(now_dir)
                stack.append(now_dir)
            else:
                finish_dir=stack.pop()
                if not stack:
                    dirs.append(finish_dir)
        else:
            if file[0]=='f':
                files.append(file)
            else:
                now_dir=Dir(file)
                stack.append(now_dir)
    print(f'DATA SET {k}:')
    print('ROOT')
    for my_dir in dirs:
        show_dir(my_dir,1)
    for i in sorted(files):
        print(i)
    k+=1