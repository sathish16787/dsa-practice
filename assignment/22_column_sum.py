A=[
  [1,2,3,4],
   [5,6,7,8],
   [9,2,3,4]
   ]
result = []
for i in range(len(A[0])):
  sum = 0
  for j in range(len(A)):
    sum += A[j][i]
  result.append(sum)
for i in result:
  print(i)

print(result)
  


