# A="ABEC"
A='pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn'
A=list(A)
count=0
for i in range(len(A)):
  if A[i].upper() == 'A' or A[i].upper() == 'E' or A[i].upper() == 'I' or A[i].upper() == 'O' or A[i].upper() == 'U':
    for j in range(i,len(A)):
      count += 1

print(count%10003)


