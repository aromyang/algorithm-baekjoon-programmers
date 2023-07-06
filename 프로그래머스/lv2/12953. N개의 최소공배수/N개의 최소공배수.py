import math

def solution(arr):
    lcm = arr[0]
    arr.sort()
    
    for i in range(1, len(arr)):
        lcm = abs(lcm * arr[i] // math.gcd(lcm, arr[i]))
    
    return lcm