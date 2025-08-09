# A = [2, 4, 3, 1, 5]
# B = 3 

def littlePony(A,B):
  count = 0
  result = 0
  for i in range(len(A)):
    if A[i] > B:
      count += 1
    if A[i] == B:
      result += 1

  if result > 0:
    return count
  else:
    return -1


A=[24,33,13,11,30,28,19,8,30,25,42,6,30,49,3,49,24,13,3,50]
B = 13 

print(littlePony(A,B))