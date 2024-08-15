from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer = []
    order_cnt_dict = defaultdict(int)
    
    for order in orders:
        order = sorted(order)
        for i in range(2, min(len(order) + 1, 11)):
            order_combinations = list(combinations(order, i))
            for order_combination in order_combinations:
                order_cnt_dict[''.join(order_combination)] += 1
    
    for cur_course in course:
        max_order_cnt = max((order_cnt for order, order_cnt in order_cnt_dict.items() if len(order) == cur_course and order_cnt > 1), default=0)
        
        if max_order_cnt:
            answer.extend(order for order, order_cnt in order_cnt_dict.items() if len(order) == cur_course and order_cnt == max_order_cnt)
    
    return sorted(answer)