def get_times(h, m, s):
    sec_angle = (s * 6) % 360
    min_angle = (m * 6 + s * 0.1) % 360
    hour_angle = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360
    count = (h * 60 + m) * 2 - h

    if sec_angle >= min_angle:
        count += 1
    if sec_angle >= hour_angle:
        count += 1
    if h >= 12:
        count -= 2

    return count

def solution(h1, m1, s1, h2, m2, s2):
    answer = get_times(h2, m2, s2) - get_times(h1, m1, s1)

    if h1 in [0, 12] and m1 == 0 and s1 == 0:
        answer += 1

    return answer
