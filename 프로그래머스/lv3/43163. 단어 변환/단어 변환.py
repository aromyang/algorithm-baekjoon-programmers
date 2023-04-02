from collections import deque


def solution(begin, target, words):
    visited = [False] * len(words)
    queue = deque()
    queue.append((begin, 0))

    while queue:
        cur_word, cur_step = queue.popleft()
        if cur_word == target:
            return cur_step

        for i in range(len(words)):
            cnt = 0
            if not visited[i]:
                for j in range(len(words[i])):
                    if words[i][j] != cur_word[j]:
                        cnt += 1
            if cnt == 1:
                visited[i] = True
                queue.append((words[i], cur_step + 1))
    return 0