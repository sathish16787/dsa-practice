# A = [2, 5, 6]
# B = 10
A = [1, 11, 2, 3, 15]
B = 10
count = 0
for i in range(len(A)):
  sum = 0 
  for j in range(i,len(A)):
    sum += A[j]

    if sum < B:
      count += 1

print(count)