A = [0, 1, 0, 1]
# A = [1,1,1,1]

# Brute force approch 
# A = [1,1,0,1,0,0,1]
# count = 0
# for i in range(len(A)):
#   if A[i] == 0:
#     A[i] = 1
#     count += 1
#     for j in range(i+1,len(A)):
#       if A[j] == 1:
#         A[j] = 0
#       elif A[j] == 0:
#         A[j] = 1
     
# print(A)
# print(count)


    

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
