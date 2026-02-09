#LEETCODE PROBLEM NUMBER 66 : PLUS ONE

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n-1,-1,-1):
            if digits[1]<9:
                digits+=1
                return digits
            digits[i]=0
        return [1]+digits 

# time complexity is O(n) and space complexity is O(1)