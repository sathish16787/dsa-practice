A = [3, 7, 90, 20, 10, 50, 40]
B = 3
# A=[3, 7, 5, 20, -10, 0, 12]
# B=2


sum = 0 
for i in range(B):
  sum += A[i]
least_average = sum / B
for i in range(1,len(A)-B+1):
  sum = sum - A[i-1] + A[i+B-1]
  value = sum / B
  if value < least_average:
    least_average = value
    output = i 

print(output)










