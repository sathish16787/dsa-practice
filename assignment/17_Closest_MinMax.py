
# A = [2, 6, 1, 6, 9]
# A = [1, 3, 2]
A=[814,761,697,483,981]
def minValue(A):
  max = A[0]
  min = A[0]
  for i in range(1,len(A)):
    if A[i] > max:
      max = A[i]
    if A[i] < min:
      min = A[i]

  return min,max

print(minValue(A))
minValue,maxValue = minValue(A)

def closestMinMax(A,min,max):
  minIndex = -1
  maxIndex = -1
  ans = len(A)

  for i in range(len(A)-1,-1,-1):
    if A[i] == min:
      minIndex = i
      if maxIndex != -1:
        length = maxIndex - minIndex + 1
        if length < ans:
          ans = length
    if A[i] == max:
      maxIndex = i
      if minIndex != -1:
        length = minIndex - maxIndex + 1
        if length < ans:
          ans = length
  return ans
    

print(closestMinMax(A,minValue,maxValue))

 