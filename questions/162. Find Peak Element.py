# Problem 162. Find Peak Element

# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index. 
# If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly 
# greater than a neighbor that is outside the array.

# Write soln in O(nlogn)

# Approach 1: Brute Force
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return i
                
        return n - 1

# # Time Complexity: O(N) 

# Approach 2: Binary Search - Time limit exceeded 
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
                
        return left