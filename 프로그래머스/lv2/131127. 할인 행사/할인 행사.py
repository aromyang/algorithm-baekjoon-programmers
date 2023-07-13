from collections import Counter

def solution(want, number, discount):
    wants = dict(zip(want, number))
    cnt = 0
    
    for i in range(len(discount) - 9):
        cnts = Counter(discount[i:i+10])
        for k, v in wants.items():
            if k not in cnts or v > cnts[k]:
                cnt -= 1
                break
        cnt += 1
    
    return cnt