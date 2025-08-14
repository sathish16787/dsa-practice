# A = [2, 1, 6, 4]
A = [1, 1, 1]

def prefixSum(A):
  PFE = A.copy()
  PFO = A.copy()
  PFE[0] = A[0]
  PFO[0] = 0
  arrayLength = len(A)
  for i in range(1,arrayLength):
    if i % 2 == 0:
        PFE[i] = PFE[i-1]+A[i]
        PFO[i] = PFO[i-1]
    else:
       PFE[i] = PFE[i-1]
       PFO[i] = PFO[i-1]+A[i]
  return PFE,PFO



preFixEven, preFixOdd = prefixSum(A)

count = 0
N = len(A) - 1
for i in range(len(A)):
   if i != 0:
    sumOfEven = preFixEven[i-1] + preFixOdd[N] - preFixOdd[i]
    sumOfOdd = preFixOdd[i-1] + preFixEven[N] - preFixEven[i]
   else:
    sumOfEven = preFixOdd[N] - preFixOdd[i]
    sumOfOdd =  preFixEven[N] - preFixEven[i]

   if sumOfEven == sumOfOdd:
     count += 1
print(count)

  
    
  

