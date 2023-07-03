from collections import Counter

def solution(s):
    cnt = 0
    zeros = 0
    
    while s != '1':
        cnt_dict = Counter(s)
        zeros += cnt_dict.get('0', 0)
        s = str(bin(cnt_dict.get('1'))[2:])
        cnt += 1

    return [cnt, zeros]