 # LEETCODE PROBLEM NUMBER 217 : CONTAINS DUPLICATE
# 
class Solution(object):
  def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """  
        if len(nums) != len(set(nums)):
            return True
        return False
# time complexity is O(n) and space complexity is O(n)