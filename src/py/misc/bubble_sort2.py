tests = [
    [4,5,1,2,10,0]
]

def bubble_sort(arr):
    L = len(arr)
    for i in range(L):
        for j in range(i+1,L):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

for arr in tests:
    print(bubble_sort(arr))