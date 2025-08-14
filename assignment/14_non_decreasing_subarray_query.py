# A = [1, 7, 3, 4, 9]
# B = [ 
#       [0, 1], 
#       [1, 4]
#     ]

# A = [1, 1, 7, 2, 3]
# B = [ 
#       [0, 2], 
#       [2, 4]
#     ]
A = [7,7,1,6,9]
B=[[0,2],[3,4],[0,1],[2,3],[0,4]]
def prefixSum(A):
  PFA = A.copy()
  PFA[0] = 1
  arrayLength = len(A)
  for i in range(1,arrayLength):
    if A[i] >= A[i-1]:
      PFA[i] = PFA[i-1] + 1
    else:
      PFA[i] = 0
  return PFA

result = []
prefixArray = prefixSum(A)
print(A)
print(prefixArray)
for i in range(len(B)):
  
  left = B[i][0]
  right = B[i][1]
  print(f"{left}-{right}")
  total = right - left 
  print(total,prefixArray[B[i][1]])

  if total == prefixArray[B[i][1]] - prefixArray[B[i][0]]:
    result.append(1)
  else: 
    result.append(0)

print(result)
   


  
  
  
  


      
    

