'''
Function:
    数组中出现次数超过一半的数字
Author:
    Charles
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        mid = int(len(nums) / 2)
        return nums[mid]