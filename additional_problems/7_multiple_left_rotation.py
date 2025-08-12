A = [1, 2, 3, 4, 5]
B = [2, 3]
# A = [5,17,100,11]
# B = [1]

def arrayRotation(A,s,e):
  e = e - 1
  while s < e:
      temp = A[s]
      A[s] = A[e]
      A[e] = temp
      s += 1
      e -= 1
  return A


result = []
for i in range(len(B)):
   copyA = A.copy()
   k = B[i] % len(copyA)
   arr_length = len(copyA) 
   arrayRotation(copyA,0,arr_length)
   arrayRotation(copyA,0,arr_length-k)
   arrayRotation(copyA,arr_length-k,arr_length)
   result_string_nums = " ".join(str(item) for item in copyA)
   result.append(f"[{result_string_nums}]")

print(" ".join(result))
   

  
# print(reverseArray(A,0,arr_length))
# print(reverseArray(A,0,k-1))
# print(reverseArray(A,k,arr_length))