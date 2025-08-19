A = "ABCGAG"

print(A)
count = 0
ans = 0
arrayLength = len(A)
for i in range(len(A)):
  if A[i] == 'A':
    count += 1
  if A[i] == 'G':
    ans += count
print(ans % (10**9 + 7))
