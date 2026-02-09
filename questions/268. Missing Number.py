
# LEETCODE PROBLEM NUMBER 268 : MISSING NUMBER
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = n * (n + 1) // 2
        asum = sum(nums)
        ans = total - asum
        return ans