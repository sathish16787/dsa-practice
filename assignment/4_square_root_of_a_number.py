A = int(input())

def squareRoot(A):
    sqrt = int(A ** 0.5)
    if sqrt * sqrt == A:
        return 1
    return -1 



# def findSquareRoot(A):
#         for i in range(1,A+1):
#             if i * i <= A:
#                 if i * i == A:
#                     return i
#             elif i * i > A:
#                  break
#         return -1
            

# print(findSquareRoot(A))
print(squareRoot(A))