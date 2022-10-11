hour, min, sec = map(int, input().split())
time = int(input())

sec += time % 60
min += time // 60

if sec >= 60:
    min += sec // 60
    sec %= 60
if min >= 60:
    hour += min // 60
    min %= 60
if hour >= 24:
    hour %= 24

print(hour, min, sec)
