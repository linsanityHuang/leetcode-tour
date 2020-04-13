

def insertion_sort(nums: list):
    
    n = len(nums)
    
    if n < 2:
        return
    
    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            else:
                break


def test_insertion_sort_1():
    test_nums = [4, 5, 6, 3, 2, 1]
    
    insertion_sort(test_nums)
    
    assert test_nums == [1, 2, 3, 4, 5, 6]
    
    test_nums = [3, 5, 4, 1, 2, 6]
    
    insertion_sort(test_nums)
    assert test_nums == [1, 2, 3, 4, 5, 6]
