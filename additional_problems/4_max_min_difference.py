A = [5, 17, 100, 1]

def max(A):
  max = -1_000_000_001
  min = 1_000_000_001
  for i in range(len(A)):
    if A[i] % 2 == 0:
      if A[i] > max:
        max = A[i]
    if A[i] % 2 != 0:
      if A[i] < min:
        min = A[i]
  return max,min


def maxMinDifference(A):
  a,b= max(A)
  return a - b


print(maxMinDifference(A))

