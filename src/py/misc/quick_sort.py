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