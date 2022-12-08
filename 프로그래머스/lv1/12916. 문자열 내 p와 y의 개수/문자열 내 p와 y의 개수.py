import re


def solution(s):
    s = str(s).lower()
    s = sorted(re.sub('[^py]', '', s))
    if len(s) & 1:
        return False

    return not s or s[len(s) // 2] != s[len(s) // 2 - 1]