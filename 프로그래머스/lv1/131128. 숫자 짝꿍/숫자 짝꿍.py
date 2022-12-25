def solution(X, Y):
    inter = ''
    nums = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
    for i in range(10):
        if nums[i] in X and nums[i] in Y:
            if nums[i] == '0' and not inter:
                inter = '0'
                break
            cnt = min(X.count(nums[i]), Y.count(nums[i]))
            inter += nums[i] * cnt
            
    
    return inter if inter else '-1'
