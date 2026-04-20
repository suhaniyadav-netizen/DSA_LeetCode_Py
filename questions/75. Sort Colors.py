# Problem 75: Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place 
# so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Approach 1: Brute Force (Bubble Sort)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    temp_val = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = temp_val

# Time Complexity: O(n^2)

# Approach 2: Counting Sort (Two Passes)
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red_C = 0
        white_C = 0
        blue_c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                red_C += 1
            elif nums[i] == 1:
                white_C += 1
            else:
                blue_c += 1
                
        for i in range(len(nums)):
            if i < red_C:
                nums[i] = 0
            elif i < red_C + white_C:
                nums[i] = 1
            else:
                nums[i] = 2

# Time Complexity: O(n)