def unique(S):
  sorted = sorted(S)
  for i in range(1, len(sorted)):
    if S[i-1] === S[i]:
      return False
  return True
  
def disjoint2(A, B, C):
  ”””Return True if there is no element common to all three lists.””” for a in A:
  for b in B: 
    if a == b:
    for c in C: if a == c
      return False 
  return True
  
def prefix_sums(S):#calculate sum of a given slice of an array
  n = len(S)
  A = [0] * n + 1 #always has 0 as first element
  for x in range(1, n+1):
    A[x] = A[x-1] + S[x-1]
  return A
