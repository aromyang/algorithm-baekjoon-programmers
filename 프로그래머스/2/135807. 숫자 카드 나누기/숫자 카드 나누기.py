from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    gcdA = reduce(gcd, arrayA)
    gcdB = reduce(gcd, arrayB)
    
    def is_valid(gcdN, arr):
        for a in arr:
            if a % gcdN == 0:
                return False
        return True
    
    ans = 0
    
    if is_valid(gcdA, arrayB):
        ans = gcdA
    if is_valid(gcdB, arrayA):
        ans = max(ans, gcdB)
    
    return ans