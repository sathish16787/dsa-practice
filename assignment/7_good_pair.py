



def goodPair(A,B):
    arrayLength = len(A) 
    for i in range(0,arrayLength):
        for j in range(i+1,arrayLength):
            if A[i]+A[j] == B:
                return 1
    return 0

# A = [1,2,3,4]
# B = 7

# A = [1,2,4]
# B = 4


A = [1,2,2]
B = 4

print(goodPair(A,B))
    