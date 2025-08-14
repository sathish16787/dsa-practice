A=[1,2,3,4,5]
sarr = A.copy()
n = len(A) - 1
for i in range(n,-1,-1):
  print(i,A[i])

sarr[n] = A[n]
print(sarr[n])
for i in range(n-1,-1,-1):
  print(i,sarr[i])
  sarr[i] = A[i] * sarr[i+1]

print(sarr)

