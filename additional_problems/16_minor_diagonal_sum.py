A = [
  [1, -2, -3],
  [-4, 5, -6],
  [-7, -8, 9]
      ]

s = 0
e = len(A[0]) - 1

result = 0
for i in range(len(A)):
  result += A[e][s]
  s += 1
  e -= 1
print(result)
