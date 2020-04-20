"""
@Author: Yi Bin
@Date: 2020/1/26
@Source: https://leetcode-cn.com/problems/kth-largest-element-in-an-array/
@Description:

    Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
    not the kth distinct element.

    Example 1:
        Input: [3,2,1,5,6,4] and k = 2
        Output: 5

    Example 2:
        Input: [3,2,3,1,2,4,5,5,6] and k = 4
        Output: 4
"""


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    return quick_select(nums, 0, len(nums) - 1, k)


def quick_select(nums, start, end, k):
    if start == end:
        return nums[start]

    index = partition(nums, start, end)
    if index > k - 1:
        return quick_select(nums, start, index - 1, k)
    elif index < k - 1:
        return quick_select(nums, index + 1, end, k)
    else:
        return nums[index]


def partition(nums, start, end):
    pivot = nums[start]
    left, right = start + 1, end
    while left <= right:
        while left <= right and nums[left] > pivot:
            left += 1
        while left <= right and nums[right] <= pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    nums[start], nums[right] = nums[right], nums[start]
    return right


if __name__ == '__main__':
    inputs = [
        [[3, 2, 1, 5, 6, 4], 2],
        [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4]
    ]
    for _input in inputs:
        print(findKthLargest(*_input))
