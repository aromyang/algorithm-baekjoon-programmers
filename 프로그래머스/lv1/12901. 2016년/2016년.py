def solution(a, b):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d_name = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    
    day = b if a == 1 else sum(days[: a - 1]) + b
    return d_name[day % 7]
