A = [2, 4, 1, 3, 2]

def maxElement(A):
  max = A[0]
  for i in range(1,len(A)):
    if A[i] > max:
      max = A[i]
  return max

maxValue = maxElement(A)
count = 0
for i in range(len(A)):
  count = count + (maxValue - A[i])
print(count)
