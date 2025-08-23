A = [1, 2, 2, 3, 1]

result = 0
for i in range(len(A)):
  result = result ^ A[i]
print(result)


