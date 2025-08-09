# A = [1,2,3,2,1]
A = [1,1,10]
def reverseArray(A):
  i = 0
  j = len(A) - 1
  for i in range(i,len(A)):
    if i < j:
      temp = A[i]
      A[i] = A[j]
      A[j] = temp
      i += 1
      j -= 1
  return A

print(reverseArray(A))