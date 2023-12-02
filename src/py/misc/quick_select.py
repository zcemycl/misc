tests = [
    [4,5,1,2,10,0],
    [7,8,1,3,10,100,50]
]


def partition(arr, l, r, p):
    i = l
    j = r-1
    while True:
        while i<=r-1 and arr[i] < p:
            i+=1
        while j>=l and arr[j] > p:
            j-=1
        if i>=j:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[r] = arr[r], arr[i]
    return i


def quick_select(arr, l, r, k):
    if l>=r:
        return
    pivot = arr[r]
    pid = partition(arr, l, r, pivot)
    if pid==k:
        return arr[k]
    elif pid<k:
        return quick_select(arr, pid+1, r, k)
    elif pid>k:
        return quick_select(arr, l, pid-1, k)

for arr in tests:
    L = len(arr)
    print(quick_select(arr, 0, L-1, 3))
    
