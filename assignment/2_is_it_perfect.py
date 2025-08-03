def isPerfect(N):
    count = 1
    for i in range(2,N):
        if N % i == 0:
            count += i
    
    if count == N:
        return "YES"
    else:
        return "NO"

T = int(input())

for i in range(T):
    N = int(input())
    print(isPerfect(N))


