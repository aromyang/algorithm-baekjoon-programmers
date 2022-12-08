def solution(phone_number):
    return str(phone_number).replace(phone_number[:-4], '*' * (len(phone_number) - 4), 1)
