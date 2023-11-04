cases = [
    [1,28,2,3,0,11],
    [1,2,0]
]

def condition(n1:int, n2:int, asc:bool):
    if asc:
        return n1>n2
    else:
        return n1<n2

def bubble_sort(arr: list, asc: bool = True) -> list:
    L = len(arr)
    for i in range(L):
        for j in range(L-i-1):
            if condition(arr[j], arr[j+1], asc):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

for case in cases:
    print('Orig: ', case)
    print('Asc: ', bubble_sort(case))
    print('Dsc: ', bubble_sort(case, False))