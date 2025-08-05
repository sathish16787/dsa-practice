

def searchElement(arr,A):
    arr_len= len(arr)
    for i in range(arr_len):
        if arr[i] == A:
            return 1
    return 0


T = int(input())
for i in range(T):
    arr_length = int(input())
    elements = input()
    arr = list(map(int,elements.split()))
    A = int(input())
    print(arr,A)
    print(searchElement(arr,A))
