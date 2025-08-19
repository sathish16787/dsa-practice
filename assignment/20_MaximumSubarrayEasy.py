# A = 5
# B = 12
# C = [2, 1, 3, 4, 5]

A=2
B=4
C=[8,7]

# def prefixSum(A):
#   PFA = A.copy()
#   PFA[0] = A[0]
#   for i in range(1,len(A)):
#     PFA[i] = PFA[i-1] + A[i]
#   return PFA
max = float('-inf')
for i in range(len(C)):
  sum = 0 
  for j in range(i,len(C)):
    sum += C[j]
    if sum > max and sum <= B:
      max = sum

if max == float('-inf'):
  print(0)
else:
  print(max)






# prefixArray = prefixSum(C)
# print(C)
# print(prefixArray)