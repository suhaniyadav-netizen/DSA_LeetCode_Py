# Problem 503: Next Greater Element II

# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.
# The next greater number of a number x is the first greater number to its traversing-order next in the array, 
# which means you could search circularly to find its next greater number. If it doesn't exist, return -1.

# Approach 1: Brute Force
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1] * n
        for i in range(n):
            for j in range(1, n):
                check = (i + j) % n
                
                if nums[check] > nums[i]:
                    result[i] = nums[check]
                    break
        return result

# Time Complexity: O(n^2)

# Approach 2: Monolitic Stack
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1] * n
        l = []
        
        for i in range(2 * n):
            cur_posn = i % n
            cur_hgt = nums[cur_posn]
            
            while l and cur_hgt > nums[l[-1]]:
                vrbl = l.pop()
                result[vrbl] = cur_hgt

            if i < n:
                l.append(cur_posn)
                
        return result

# Time Complexity: O(N)