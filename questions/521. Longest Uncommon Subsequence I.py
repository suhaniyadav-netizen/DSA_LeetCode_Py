# Problem 521: Longest Uncommon Subsequence I

# Given two strings a and b, return the length of the longest uncommon subsequence between a and b.
# If the longest uncommon subsequence does not exist, return -1.
# An uncommon subsequence between two strings is a string that is a subsequence of one but not the other.

# Approach 1 (Not Brute Force)
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
            
        # If they are different then longest string is answer. shorter string can fit in longer but not vice versa
        if len(a) > len(b):
            return len(a)
        else:
            return len(b)

# Time Complexity: O(N)