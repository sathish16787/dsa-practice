# A = [ 2, 3, -1, 4, 2, 1 ]
# B = 4
# A=[-533,-666,-500,169,724,478,358,-38,-536,705,-855,281,-173,961,-509,-5,942,-173,436,-609,-396,902,-847,-708,-618,421,-284,718,895,447,726,-229,538,869,912,667,-701,35,894,-297,811,322,-667,673,-336,141,711,-747,-132,547,644,-338,-243,-963,-141,-277,741,529,-222,-684,35]
# B=48

A=[-584,-714,-895,-512,-718,-545,734,-886,701,316,-329,786,-737,-687,-645,185,-947,-88,-192,832,-55,-687,756,-679,558,646,982,-519,-856,196,-778,129,-839,535,-550,173,-534,-956,659,-708,-561,253,-976,-846,510,-255,-351,186,-687,-526,-978,-832,-982,-213,905,958,391,-798,625,-523,-586,314,824,334,874,-628,-841,833,-930,487,-703,518,-823,773,-730,763,-332,192,985,102,-520,213,627,-198,-901,-473,-375,543,924,23,972,61,-819,3,432,505,593,-275,31,-508,-858,222,286,64,900,187,-640,-587,-26,-730,170,-765,-167,711,760,-104,-333]
B=32
# A = [5, -2, 3 , 1, 2]
# B = 3


def prefixSum(A):
  pfArr = A.copy()
  pfArr[0] = A[0]
  for i in range(1,len(A)):
    pfArr[i] = pfArr[i-1] + A[i]
  return pfArr

def sufixSum(A):
  suarr = A.copy()
  n = len(A) - 1
  suarr[n] = A[n]
  for i in range(n-1,-1,-1):
    suarr[i] = suarr[i+1] + A[i]
  return suarr


prefixArray = prefixSum(A)
suffixArray = sufixSum(A)


def maxSum(prefixArray,suffixArray,B):
  max = -10000000000001
  edgeLeft = prefixArray[B-1]
  edgeRight = suffixArray[len(A) - B]
  if edgeLeft > max:
    max = edgeLeft
  if edgeRight > max:
    max = edgeRight
  N = len(prefixArray)
  for i in range(1,B):
    sum = prefixArray[i-1] + suffixArray[N-B+i]
    if max < sum:
      max = sum 
  return max


print(maxSum(prefixArray,suffixArray,B))