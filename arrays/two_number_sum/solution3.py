def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == targetSum:
            return[array[left],array[right]]
        elif current_sum < targetSum:
            left += 1
        elif current_sum > targetSum:
            right -= 1
    return []