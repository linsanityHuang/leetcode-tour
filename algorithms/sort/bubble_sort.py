from typing import List


def bubble_sort(nums: List):

    n = len(nums)
    
    if n < 2:
        return
    
    for i in range(n):
        # 提前退出冒泡循环的标志位
        exchange = False
        for j in range(1, n - i):
            # 交换
            if nums[j-1] > nums[j]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
                # 表示有数据交换
                exchange = True
        # 没有数据交换，提前退出
        if not exchange:
            break


def test_bubble_sort_1():
    test_nums = [4, 5, 6, 3, 2, 1]
    
    bubble_sort(test_nums)
    
    assert test_nums == [1, 2, 3, 4, 5, 6]

    test_nums = [3, 5, 4, 1, 2, 6]
    
    bubble_sort(test_nums)

    assert test_nums == [1, 2, 3, 4, 5, 6]
