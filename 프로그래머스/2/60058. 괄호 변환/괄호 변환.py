def solution(p):
    def seperate(p):
        balance_cnt = 0
        
        for i, pp in enumerate(p):
            if i != 0 and balance_cnt == 0:
                return p[:i], p[i:]
            if pp == '(':
                balance_cnt += 1
            else:
                balance_cnt -= 1
        
        return p, ''
    
    def is_correct(p):
        correct = []
        
        for pp in p:
            if pp == '(':
                correct.append(pp)
            else:
                if not correct:
                    return False
                correct.pop()
                
        return True
    
    def reverse(p):
        return ''.join(')' if c == '(' else '(' for c in p)
        
    def make_correct(p):
        if not p:
            return p
        
        u, v = seperate(p)
        
        if is_correct(u):
            return u + make_correct(v)
        else:
            return '(' + make_correct(v) + ')' + reverse(u[1:len(u)-1])
    
    answer = ''
    answer += make_correct(p)
    return answer