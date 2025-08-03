N=int(input())


def isPrime(N):
    count = 2
    if N == 1:
        return "NO"
    else:
        for i in range(2,N):
            if N%i == 0:
                return "NO"
        return "YES"


print(isPrime(N))