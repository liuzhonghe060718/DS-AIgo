from collections import defaultdict
from functools import cmp_to_key
models=defaultdict(list)
n=int(input())
def compare(a,b):
    if a[-1]=='B' and b[-1]=='M':
        return 1
    elif a[-1]=='M' and b[-1]=='B':
        return -1
    else:
        a,b=float(a[:len(a)-1]),float(b[:len(b)-1])
        if a>b:
            return 1
        elif a==b:
            return 0
        else:
            return -1
for _ in range(n):
    model,scale=input().split('-')
    models[model].append(scale)


for name in sorted(models.keys()):
    print(name+': '+', '.join(sorted(models[name],key=cmp_to_key(compare))))


