from collections import defaultdict

def solution(n, wires):
    def compute_splited_abs(linked_cnt):
        return abs((n - linked_cnt) - linked_cnt)
            
    def compute_linked_wires(cur_wire, seen, cnt):
        for linked_wire in wires_link[cur_wire]:
            if linked_wire not in seen:
                seen.add(linked_wire)
                cnt = compute_linked_wires(linked_wire, seen, cnt + 1)
        return cnt
    
    wires_link = defaultdict(list)
    
    for start, end in wires:
        wires_link[start].append(end)
        wires_link[end].append(start)
        
    answer = 100

    for cur_wire, linked_wires in wires_link.items():
        seen = set()
        seen.add(cur_wire)
         
        for cur_linked_wire in linked_wires:
            if cur_linked_wire not in seen:
                seen.add(cur_linked_wire)
                cur_linked_cnt = compute_linked_wires(cur_linked_wire, seen, 1)
                answer = min(answer, compute_splited_abs(cur_linked_cnt))

    return answer