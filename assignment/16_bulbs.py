A = [0, 1, 0, 1]
# A = [1,1,1,1]
count = 0 

for i in range(len(A)):
  state = A[i]
  if count % 2 == 0:
    state = A[i]
  else:
    state = 1 - A[i]
  
  if state == 0:
    count += 1
print(count)
