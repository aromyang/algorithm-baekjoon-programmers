def solution(skill, skill_trees):
    skill_dict = {}
    for i, s in enumerate(skill):
        skill_dict[s] = i

    answer = 0
    for tree in skill_trees:
        visited = [False] * len(skill)
        for t in tree:
            if t in skill_dict and not visited[skill_dict[t]]:
                idx = skill_dict[t]
                visited[idx] = True
                if idx > 0 and not visited[skill_dict[skill[idx - 1]]]:
                    answer -= 1
                    break
        answer += 1
    
    return answer