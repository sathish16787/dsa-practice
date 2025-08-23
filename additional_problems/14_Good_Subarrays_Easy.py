# A = [1, 2, 3, 4, 5]
# B = 4

A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
B = 65
good_array = 0
for i in range(len(A)):
  sum = 0 
  length = 0
  for j in range(i,len(A)):
    length += 1
    sum += A[j]
    if length % 2 == 0 and sum < B:
      good_array += 1
    elif length % 2 != 0 and sum > B:
      good_array += 1
print(good_array)
    
