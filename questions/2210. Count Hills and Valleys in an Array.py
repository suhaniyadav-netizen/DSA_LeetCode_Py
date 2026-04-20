# Problem 2210: Count Hills and Valleys in an Array

# You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. 
# Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i].
# Adjacent indices i and j with the same value are considered part of the same hill or valley.
# Return the number of hills and valleys.

# Approach 1: Brute Force
class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot_count = 0
        n = len(nums)
        
        for i in range(1, n - 1):
            if nums[i] == nums[i - 1]:
                continue
                
            left_ele = nums[i]
            right_ele = nums[i]
            
            for j in range(i - 1, -1, -1):
                if nums[j] != nums[i]:
                    left_ele = nums[j]
                    break
                    
            for j in range(i + 1, n):
                if nums[j] != nums[i]:
                    right_ele = nums[j]
                    break
                    
            # Check if hill
            if left_ele < nums[i] and right_ele < nums[i]:
                tot_count += 1
            # Check if valley
            elif left_ele > nums[i] and right_ele > nums[i]:
                tot_count += 1
                
        return tot_count

# Time Complexity: O(n^2)