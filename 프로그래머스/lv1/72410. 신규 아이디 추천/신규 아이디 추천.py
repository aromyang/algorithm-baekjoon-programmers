import re

def solution(new_id):
    answer = str(new_id).lower()
    answer = re.sub('[^a-z0-9\\-_.]', '', answer)
    answer = re.sub('\\.+', '.', answer)
    answer = re.sub('^[.]|[.]$', '', answer)
    answer = 'a' if not answer else answer[:15]
    answer = re.sub('^[.]|[.]$', '', answer)
    answer = answer if len(answer) >= 3 else answer + ''.join([answer[-1] for i in range(3 - len(answer))])

    return answer