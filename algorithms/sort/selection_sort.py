

def selection_sort(nums: list):
    
    n = len(nums)
    
    if n < 2:
        return
    
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if nums[j] < nums[min_index]:
                min_index = j
        
        if nums[min_index] < nums[i]:
            nums[min_index], nums[i] = nums[i], nums[min_index]


def test_selection_sort_1():
    test_nums = [4, 5, 6, 3, 2, 1]
    
    selection_sort(test_nums)
    
    assert test_nums == [1, 2, 3, 4, 5, 6]
    
    test_nums = [3, 5, 4, 1, 2, 6]
    
    selection_sort(test_nums)
    assert test_nums == [1, 2, 3, 4, 5, 6]
