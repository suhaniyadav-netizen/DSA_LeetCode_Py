#LEETCODE PROBLEM NO 349 : INTERSECTION OF TWO ARRAYS

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        result = set()
        for i in nums2:
            if i in set1:
                result.add(i)
        return list(result)
    
# time complexity is O(n) and space complexity is O(n) 

# another method 
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return(list(set(nums1) & set(nums2)))
    
# time complexity is O(n) and space complexity is O(n)