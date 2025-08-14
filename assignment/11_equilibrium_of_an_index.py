# A = [-7, 1, 5, 2, -4, 3, 0]
# A = [1, 2, 3]
A=[1,2,3,7,1,2,3]

def prefixSum(A):
  PFA = A.copy()
  PFA[0] = A[0]
  for i in range(1,len(A)):
    PFA[i] = PFA[i-1] + A[i]
  return PFA

prefixArray = prefixSum(A)


def equilibriumIndex(PFA):
  arrayLength = len(PFA)
  arrayElements = arrayLength - 1
  for i in range(len(PFA)):
    if i ==0:
      left = 0 
      right = PFA[arrayElements] - PFA[i]
      print(i,left,right)
    else:
      left = PFA[i-1]
      right = PFA[arrayElements] - PFA[i]
      print(i,left,right)
      
    if left == right:
      return i
  return -1

print(equilibriumIndex(prefixArray))
    