def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potential_match = targetSum - num
        if potential_match in nums:
            return [potential_match, num]
        else:
            nums[num]=True
    return []