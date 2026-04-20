# Problem 35: Search Insert Position(Binary Search)

# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Approach 1:   Linear Search
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)

# Time Complexity: O(N)
# Space Complexity: O(1)

# Approach 2: Binary Search
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
                
            elif nums[mid] < target:
                left = mid + 1
                
            else:
                right = mid - 1
                
        # If we exit the loop without finding the exact number thrn the pointers have crossed.
        return left

# Time Complexity: O(log N)
# Space Complexity: O(1)