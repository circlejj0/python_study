def solution(nums):
    answer = []
    for i in range(len(nums)):
        if nums[i] in answer:
            continue
        else:
            answer.append(nums[i])
    
    if len(answer) > (len(nums)/2):
        result = (len(nums) / 2)
    else:
        result = len(answer)
    return result
