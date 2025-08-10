# A = [2, 1, 2] 
# A = [2]
# A=[13,7,16,18,14,17,18,8,10]
# A=[13,7,16,18,14,17,18,8,10]
# A=[11,15,19]
# A=[13,7,16,18,14,17,18,8,10]
A=[4,4,4]

def secondMax(A):
  if len(A) < 2:
    return -1
  
  if A[0] > A[1]:
    max = A[0]
    second_max = A[1]
  elif A[1] > A[0]:
    max = A[1]
    second_max = A[0]
  elif A[0] == A[1]:
    max = A[0]
    second_max = -1
  for i in range(2,len(A)):
    if A[i] > max:
      second_max = max
      max = A[i]
    elif A[i]<max and A[i]>second_max:
      second_max = A[i]
    print(max,second_max)
  
  return second_max

print(secondMax(A))