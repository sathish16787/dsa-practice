# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]

# A = [2, 2, 2]
# B = [[0, 0], [1, 2]]
A=[7,3,1,5,5,5,1,2,4,5]
B=[[6,9],[2,9],[2,4],[0,9]]

def prefixSum(A):
  PFA = A.copy()
  PFA[0] = A[0]
  arrayLength = len(A)
  for i in range(1,arrayLength):
    PFA[i] = PFA[i-1] + A[i]
  return PFA

prefixArray = prefixSum(A)

arrayLengthB = len(B)
arrayLengthA = len(A)
arrElements = arrayLengthA - 1
print(arrayLengthA)
print(arrElements)
result = []
for i in range(arrayLengthB):
  left = B[i][0]
  right = B[i][1]
  print(left,right)
  sum = 0
  if left == 0:    
    sum = prefixArray[right]
    print(f"{prefixArray[right]}")
  else:
    print(f"{prefixArray[right] -  prefixArray[left - 1]}")
    sum =  prefixArray[right] -  prefixArray[left - 1]
  result.append(sum)
  
print(A)
print(prefixArray)
print(result)