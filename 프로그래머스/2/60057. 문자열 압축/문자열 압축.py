from collections import deque

def solution(s):
    spliter = len(s) // 2
    min_compressed_len = len(s)
    
    while spliter >= 1:                    
        cur_splited_str = deque([s[i:i+spliter] for i in range(0, len(s), spliter)])
        cur_compressed_str = deque([cur_splited_str.popleft()])
        compression_cnt = 1
                
        while cur_splited_str:
            cur_str = cur_splited_str.popleft()
            if cur_compressed_str[-1] == cur_str:
                compression_cnt += 1
            else:
                if compression_cnt != 1:
                    cur_compressed_str.append(str(compression_cnt) + cur_compressed_str.pop())
                    compression_cnt = 1
                cur_compressed_str.append(cur_str)
                
        if compression_cnt != 1:
            cur_compressed_str.append(str(compression_cnt) + cur_compressed_str.pop())

        min_compressed_len = min(min_compressed_len, len(''.join(cur_compressed_str)))
        spliter -= 1
        
    return min_compressed_len