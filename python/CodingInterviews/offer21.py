'''
Function:
    调整数组顺序使奇数位于偶数前面
Author:
    Charles
'''
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        p0, p1 = 0, len(nums) - 1
        while p0 < p1:
            if nums[p0] % 2 == 0 and nums[p1] % 2:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 -= 1
            elif nums[p0] % 2 == 0:
                p1 -= 1
            elif nums[p1] % 2:
                p0 += 1
            else:
                p0 += 1
                p1 -= 1
        return nums