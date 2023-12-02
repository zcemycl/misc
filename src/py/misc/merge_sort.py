tests = [
    [4,5,1,2,10,0],
    [7,8,1,3,10,100,50]
]

def merge(larr, rarr):
    arr = []
    L,R = len(larr), len(rarr)
    l,r = 0,0
    while l<L and r<R:
        if larr[l] < rarr[r]:
            arr.append(larr[l])
            l+=1
        else:
            arr.append(rarr[r])
            r+=1
    
    arr += larr[l:]
    arr += rarr[r:]
    return arr


def merge_sort(arr):
    L = len(arr)
    if L <= 1:
        return arr
    larr = merge_sort(arr[:L//2])
    rarr = merge_sort(arr[L//2:])
    return merge(larr, rarr)


for arr in tests:
    print(merge_sort(arr))