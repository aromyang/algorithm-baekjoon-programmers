from collections import defaultdict
import math

def solution(fees, records):
    infos = defaultdict(int)
    total = defaultdict(int)
    max_out = 23 * 60 + 59
    
    for record in records:
        time, car, command = record.split()
        hour, minutes = time.split(':')
        time = int(hour) * 60 + int(minutes)
        
        if command == 'IN':
            infos[car] = (time)
        else:
            in_time = infos[car]
            infos.pop(car)
            total[car] += (time - in_time)
            
    for car, time in infos.items():
        total[car] += max_out - time
    
    total = sorted(total.items())
    ans = []
    for car, time in total:
        if time <= fees[0]:
            ans.append(fees[1])
        else:
            ans.append(fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3])
            
    return ans