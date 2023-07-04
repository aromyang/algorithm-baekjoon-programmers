def solution(cacheSize, cities):
    cache = []
    answer = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    while cities:
        cur = cities.pop(0).lower()
        if cur in cache:
            cache.remove(cur)
            cache.append(cur)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(cur)
            answer += 5
    
    return answer