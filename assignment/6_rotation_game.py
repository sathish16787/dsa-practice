# A=[1,2,3,4]
# B=2
# k = B % len(A)
# print(k)

# print(arr_length)

def reverseArray(A,s,e):
    while (s < e):
        temp = A[s]
        A[s] = A[e]
        A[e] = temp

        s += 1
        e -= 1
    return A

elements = input()
A = list(map(int,elements.split()))
arr_length = A[0] - 1
A = A[1:]
B = int(input())
k = B % len(A)
print(reverseArray(A,0,arr_length))
print(reverseArray(A,0,k-1))
print(reverseArray(A,k,arr_length))

for i in range(len(A)):
    print(A[i], end=" ")