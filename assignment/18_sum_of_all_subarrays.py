A = [1, 2, 3]

sum = 0 
for i in range(len(A)):
  total = (i+1) * (len(A) - i)
  con = total * A[i]
  sum += con
 

print(sum)

