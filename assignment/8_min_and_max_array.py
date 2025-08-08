def arrayMax(A):
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    return max

def arrayMin(A):
    min = A[0]
    for i in range(len(A)):
        if A[i] < min:
            min = A[i]
    return min 


elements = input()
N =  list(map(int,elements.split()))
A = N[1:]

print(arrayMax(A), arrayMin(A)) 

