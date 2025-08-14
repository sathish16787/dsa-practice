
def prefixSum(arr):
  prearr = arr.copy()
  prearr[0] = arr[0]
  for i in range(1,len(arr)):
    prearr[i] = prearr[i-1] * arr[i]
  return prearr

def suffixSum(arr):
  sufarr = arr.copy()
  n = len(arr) - 1
  sufarr[n] = arr[n] 
  for i in range(n-1,-1,-1):
    sufarr[i] = sufarr[i+1] * arr[i]
  return sufarr

arr = [1, 2, 3, 4, 5]


prefixArray = prefixSum(arr)
suffixArray = suffixSum(arr)

print(f"{arr} \n{prefixArray} \n{suffixArray}")

result = []
for i in range(len(arr)):
  print(i,arr[i])
  if i == 0:
    result.append(suffixArray[i+1])
  elif i == len(arr) - 1:
    result.append(prefixArray[i-1])
  else:
    result.append(prefixArray[i-1]*suffixArray[i+1])
print(result)

