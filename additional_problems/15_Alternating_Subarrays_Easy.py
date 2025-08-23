# A = [1, 0, 1, 0, 1]
# B = 1 
# A = [0, 0, 0, 1, 1, 0, 1]
# B = 0 
A=[0,0,0,1,0,0,0,1,0,1,1]
B=1

length = (2*B) + 1
print(length)
end = len(A) - length
print(end)

result = []
for i in range(end+1):
  prev_value = -1 
  flag = 1
  for j in range(i,(i+length)):
    if A[j] == prev_value:
      flag = 0
      break
    prev_value = A[j]
  if flag == 1:
    result.append(i+B)
print(result)
    
    







