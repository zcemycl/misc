tests = [
    [4,5,1,2,10,0],
    [7,8,1,3,10,100,50]
]

def partition(arr, l, r, p):
    i = l-1
    for j in range(l, r):
        if arr[j] <= p:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_select(arr, l, r, k):
    if l>=r:
        return
    pivot = arr[r]
    pid = partition(arr, l, r, pivot)
    if pid == k:
        return arr[k]
    elif pid > k:
        return quick_select(arr, l, pid-1, k)
    elif pid < k:
        return quick_select(arr, pid+1, r, k)

for arr in tests:
    L = len(arr)
    print(quick_select(arr, 0, L-1, 3))
    print(arr)
