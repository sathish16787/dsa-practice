N = int(input("Enter the number: "))

def sqrt(N):
    count = 0
    for i in range(1,N+1):
        if N % i == 0:
            count += 1

    return count



print(sqrt(N))

