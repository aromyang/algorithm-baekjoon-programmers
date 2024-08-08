from collections import defaultdict

def solution(user_id, banned_id):
    def is_match(u_id, b_id):
        return all(u == b or b == '*' for u, b in zip(u_id, b_id))
        
    possible_banned = defaultdict(set)
    user_id_len_dict = defaultdict(list)
    [user_id_len_dict[len(u_id)].append(u_id) for u_id in user_id]
    
    for idx, b_id in enumerate(banned_id):
        for u_id in user_id_len_dict[len(b_id)]:
            if is_match(u_id, b_id):
                possible_banned[idx].add(u_id)
        
    answer = set()
    
    def backtrack(index, cur_set):
        if index == len(banned_id):
            answer.add(tuple(sorted(cur_set)))
            return
        
        for user in possible_banned[index]:
            if user not in cur_set:
                backtrack(index + 1, cur_set + [user])
    
    backtrack(0, [])
    
    return len(answer)