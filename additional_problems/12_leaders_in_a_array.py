# A = [16, 17, 4, 3, 5, 2]
A = [5, 4]

result = []
max = A[len(A)-1]
result.append(max)
print(max)
for i in range(len(A)-1-1,-1,-1):
  if A[i] > max:
    result.append(A[i])
    max = A[i]
print(result)

