'''
Function:
    把数组排成最小的数
Author:
    Charles
'''
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        def QuickSort(nums, left, right):
            if left >= right: return
            partition, i, j = nums[left], left, right
            while i < j:
                while i < j and nums[j] + partition >= partition + nums[j]: j -= 1
                nums[i] = nums[j]
                while i < j and nums[i] + partition <= partition + nums[i]: i += 1
                nums[j] = nums[i]
            nums[i] = partition
            QuickSort(nums, left, i-1)
            QuickSort(nums, i+1, right)
        QuickSort(nums, 0, len(nums)-1)
        return ''.join(nums)