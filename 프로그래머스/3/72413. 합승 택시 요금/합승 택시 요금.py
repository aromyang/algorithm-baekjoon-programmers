import heapq
from collections import defaultdict

def dijkstra(graph, n, start):
    min_fare = [float("inf")] * (n + 1)
    min_fare[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_fare, cur_loc = heapq.heappop(pq)
        
        if min_fare[cur_loc] < cur_fare:
            continue
        for next_loc, next_fare in graph[cur_loc]:
            to_go_fare = min_fare[cur_loc] + next_fare
            if to_go_fare < min_fare[next_loc]:
                min_fare[next_loc] = to_go_fare
                heapq.heappush(pq, (to_go_fare, next_loc))
                
    return min_fare

def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    
    for start, end, fare in fares:
        graph[start].append((end, fare))
        graph[end].append((start, fare))
    
    min_fare_from_s = dijkstra(graph, n, s)
    min_fare_from_a = dijkstra(graph, n, a)
    min_fare_from_b = dijkstra(graph, n, b)
    
    min_total_fare = float("inf")
    for meet_point in range(1, n + 1):
        cur_meet_fare = min_fare_from_s[meet_point] + min_fare_from_a[meet_point] + min_fare_from_b[meet_point]
        min_total_fare = min(min_total_fare, cur_meet_fare)
    
    return min_total_fare