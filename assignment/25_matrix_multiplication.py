# A = [[1, 2],
#      [3, 4]]
# B = [[5, 6],
#      [7, 8]]

A = [[1, 1]]
B = [[2],
     [3]]

for i in range(len(A)):
  for j in range(len(A[0])):
    print(A[i][j],B[j][i])