from collections import deque

def solution(bridge_length, weight, truck_weights):
    seconds = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    bridge_weight = 0

    while truck_weights:
        bridge_weight -= bridge.popleft()
        
        if bridge_weight + truck_weights[0] <= weight:
            cur_truck_weight = truck_weights.popleft()
            bridge_weight += cur_truck_weight
            bridge.append(cur_truck_weight)
        else:
            bridge.append(0)
        
        seconds += 1
    
    return seconds + bridge_length