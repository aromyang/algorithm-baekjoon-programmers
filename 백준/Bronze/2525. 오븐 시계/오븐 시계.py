hour, min = map(int, input().split())
time = int(input())

hour += time // 60
min += time % 60

if min >= 60:
    hour += 1
    min -= 60
if hour >= 24:
    hour -= 24

print(hour, min)
