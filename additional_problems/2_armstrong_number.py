
def armstrongNumber(N):
    number = N
    sum = 0 
    while number > 0:
        remainder = int(number%10)
        sum = remainder * remainder * remainder + sum
        number =int(number / 10)
    if sum == N:
        print(N)

N = int(input())
for i in range(1,N+1):
    armstrongNumber(i)