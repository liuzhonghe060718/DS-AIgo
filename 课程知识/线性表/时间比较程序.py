import timeit

a, b = 10, 20

# 测试手写 if
def max_if(a, b):
    if a > b:
        return a
    else:
        return b
def max_builtin(a, b):
    return max(a, b)

print(timeit.timeit(lambda: max_if(a, b), number=1000000))

# 测试 max
print(timeit.timeit(lambda: max_builtin(a, b), number=1000000))
