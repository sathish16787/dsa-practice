def oddEven(A):
  even = []
  odd = []
  for i in range(len(A)):
    if A[i] % 2 == 0:
      even.append(A[i])
    if A[i] % 2 != 0:
      odd.append(A[i])
  return even, odd




T = int(input())
for i in range(T):
  N = int(input())
  elements = input()
  A = list(map(int,elements.split()))
  e,o = oddEven(A)
  for i in range(len(e)):
    print(e[i], end=" ")
  print()
  for i in range(len(o)):
    print(o[i], end=" ")
  

