from collections import Counter
from itertools import combinations

def solution(weights):
    weights_cnt = Counter(weights)
    possible_distances = list(combinations([2, 3, 4], 2))
    matched = 0
    
    for cur_weight, cur_cnt in weights_cnt.items():
        matched += cur_cnt * (cur_cnt - 1) // 2
        for distance1, distance2 in possible_distances:
            matched += cur_cnt * weights_cnt[cur_weight * distance1 / distance2]
    
    return matched