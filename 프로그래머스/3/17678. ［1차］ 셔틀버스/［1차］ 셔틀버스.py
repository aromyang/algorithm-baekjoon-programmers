import heapq

def time_to_min(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def min_to_time(minutes):
    hour = minutes // 60
    minute = minutes % 60
    return f"{hour:02}:{minute:02}"

def solution(n, t, m, timetable):
    timetable = sorted([time_to_min(time) for time in timetable])    
    bus_time = time_to_min("09:00")
    answer = 0
    
    for bus_num in range(n):
        crews = []
        while timetable and timetable[0] <= bus_time and len(crews) < m:
            crews.append(heapq.heappop(timetable))
            
        if bus_num == n - 1:
            if len(crews) < m:
                answer = bus_time
            else:
                answer = crews[-1] - 1
        
        bus_time += t
    
    return min_to_time(answer)