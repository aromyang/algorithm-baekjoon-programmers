import sys

input = sys.stdin.readline

an = 0

while True:
    s = input().strip()
    if s == '고무오리 디버깅 끝':
        break
    elif s == '고무오리':
        if an == 0:
            an += 2
        else:
            an -= 1
    elif s == '문제':
        an += 1

if an <= 0:
    print('고무오리야 사랑해')
else:
    print('힝구')
