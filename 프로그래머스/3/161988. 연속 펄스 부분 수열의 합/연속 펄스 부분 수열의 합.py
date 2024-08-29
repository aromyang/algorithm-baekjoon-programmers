def solution(sequence):
    def compute_max_pulse_sequence_sum(pulse_sequence):
        cur_max = total_max = pulse_sequence[0]
        
        for cur_elem in pulse_sequence[1:]:
            cur_max = max(cur_elem, cur_max + cur_elem)
            total_max = max(cur_max, total_max)
            
        return total_max

    pulse_sequence = [sequence[i] if i & 1 else -sequence[i] for i in range(len(sequence))]
    reverse_pulse_sequence = [-sequence[i] if i & 1 else sequence[i] for i in range(len(sequence))]
        
    return max(compute_max_pulse_sequence_sum(pulse_sequence), compute_max_pulse_sequence_sum(reverse_pulse_sequence))