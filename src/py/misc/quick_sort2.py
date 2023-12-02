tests = [
    [4,5,1,2,10,0],
    [7,8,1,3,10,100,50]
]

def partition(arr, l, r, p):
    i = l-1
    for j in range(l,r):
        if arr[j] <= p:
            i+=1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

def quick_sort(arr, l, r):
    if l>=r:
        return
    pivot = arr[r]
    pid = partition(arr, l, r, pivot)
    quick_sort(arr, l, pid-1)
    quick_sort(arr, pid+1, r)


for arr in tests:
    L = len(arr)
    quick_sort(arr, 0, L-1)
    print(arr)