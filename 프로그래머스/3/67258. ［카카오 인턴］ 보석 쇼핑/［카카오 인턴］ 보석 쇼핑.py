from collections import defaultdict

def solution(gems):
    unique_gems = len(set(gems))
    gem_dict = defaultdict(int)
    shortest_range = [0, len(gems)]
    start, end = 0, 0

    if unique_gems == len(gems):
        return [1, unique_gems]
    
    while end < len(gems):
        gem_dict[gems[end]] += 1
        end += 1

        while len(gem_dict) == unique_gems:
            if end - start < shortest_range[1] - shortest_range[0]:
                shortest_range = [start, end]
            
            gem_dict[gems[start]] -= 1
            
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            
            start += 1
        
    return [shortest_range[0] + 1, shortest_range[1]] 