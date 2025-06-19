
n=int(input())
speed=[]
ans=0
for i in range(n):
    speed.append(int(input()))
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge_count(left,right)
def merge_count(left,right):
    global ans
    arry=[]
    i=j=0
    ll=len(left)
    lr=len(right)
    while i<ll and j<lr:
        if left[i]>right[j]:
            ans+=(ll-i)
            arry.append(right[j])
            j+=1
        else:
            arry.append(left[i])
            i+=1
    arry.extend(left[i:])
    arry.extend(right[j:])
    return arry
merge_sort(speed[::-1])
print(ans)





def merge_and_count(arr, temp_arr, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)  # 计算逆序对数
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_sort_and_count(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += merge_sort_and_count(arr, temp_arr, left, mid)
        inv_count += merge_sort_and_count(arr, temp_arr, mid + 1, right)
        inv_count += merge_and_count(arr, temp_arr, left, mid, right)
    return inv_count


def count_inversions(arr):
    temp_arr = arr[:]
    return merge_sort_and_count(arr, temp_arr, 0, len(arr) - 1)


# 示例
arr = [1, 20, 6, 4, 5]
print("逆序对数量:", count_inversions(arr))  # 输出: 5


def bit_sum(BIT, i):
    s = 0
    while i > 0:
        s += BIT[i]
        i -= i & (-i) # 回溯⾄祖先节点
    return s

def bit_update(BIT, i, v):
    while i < len(BIT):
        BIT[i] += v
        i += i & (-i)
n = int(input())
values = [int(input()) for _ in range(n)]
# 离散化：建⽴值到索引的映射
sorted_vals = sorted(set(values))
value_to_index = {v: i + 1 for i, v in enumerate(sorted_vals)}
# 初始化树状数组
BIT = [0] * (len(sorted_vals) + 1)
count = 0
# 计算逆序对
for v in values:
    index = value_to_index[v]
    count += bit_sum(BIT, index - 1) # 查询⽐当前值⼩的元素个数
    bit_update(BIT, index, 1) # 在树状数组中记录当前值出现次数
print(count)


