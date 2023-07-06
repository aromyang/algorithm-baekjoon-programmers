from collections import deque

def solution(people, limit):
    cnt = 0
    people = deque(sorted(people))
    
    while people:
        weight = people.pop()
        while people and people[0] + weight <= limit:
            weight += people.popleft()
        cnt += 1
    
    return cnt