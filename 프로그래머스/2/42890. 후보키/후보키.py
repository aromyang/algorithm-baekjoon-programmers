from itertools import combinations

def is_unique(relation, comb):
    seen = set()

    for row in relation:
        key = tuple(row[col] for col in comb)
        seen.add(key)
        
    return len(seen) == len(relation)

def is_min(candidate_keys, comb):
    for key in candidate_keys:
        if set(key).issubset(set(comb)):
            return False
    return True

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    
    candidate_keys = []
    
    for i in range(1, col_len + 1):
        for comb in combinations(range(col_len), i):
            if is_unique(relation, comb) and is_min(candidate_keys, comb):
                candidate_keys.append(comb)
    
    return len(candidate_keys)