# Problem 605: Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
# and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

# Approach 1: Brute Force (Naive Simulation with Extra Memory)
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        beds = list(flowerbed)
        planted = 0
        
        for i in range(len(beds)):
            if beds[i] == 0:
                left_emp = (i == 0) or (beds[i - 1] == 0)
                right_emp = (i == len(beds) - 1) or (beds[i + 1] == 0)
                
                if left_emp and right_emp:
                    beds[i] = 1
                    planted += 1
                    
        return planted >= n

# Time Complexity: O(N)
# Space Complexity: O(N)

# Approach 2: Greedy Programming
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        numf = len(flowerbed)
        
        for i in range(numf):
            if n == 0:
                return True
                
            if flowerbed[i] == 0:
                left_safe = (i == 0) or (flowerbed[i - 1] == 0)
                right_safe = (i == numf - 1) or (flowerbed[i + 1] == 0)
                
                if left_safe and right_safe:
                    flowerbed[i] = 1
                    n -= 1
                    
        return n <= 0

# Time Complexity: O(N)
# Space Complexity: O(1)