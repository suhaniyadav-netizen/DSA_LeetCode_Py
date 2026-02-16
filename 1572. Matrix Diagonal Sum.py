# LEETCODE PROBLEM NO 1572 : MATRIX DIAGONAL SUM

# Given a square matrix mat, return the sum of the matrix diagonals.
# Only include the sum of all the elements on the primary diagonal and all the elements on 
# the secondary diagonal that are not part of the primary diagonal.

class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        for i in range(len(mat)):
            sum += mat[i][i]
            if i != len(mat) - 1 - i:
                sum += mat[i][len(mat) - 1 - i] 
        return sum
    
