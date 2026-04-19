# Merge sort is a sorting algorithm that:
# divides the array into smaller parts
# sorts those smaller parts
# merges them back in sorted order

# It follows divide and conquer.

# Example : [8, 3, 5, 4]

# Step 1: Divide
# [8, 3] n [5, 4]
# Step 2: Divide again
# [8] [3] [5] [4] 
# Step 3: Merge
# [8] + [3] -> [3, 8]
# [5] + [4] -> [4, 5]
# Step 4: Merge bigger parts
# [3, 8] + [4, 5] -> [3, 4, 5, 8]


        
def merge_sort(arr):                            # Sort Code Only
    if len(arr) <= 1:                           # Base case: if array has 0/1 element, it's sorted
        return arr

    mid = len(arr) // 2                         # find middle index
    left = merge_sort(arr[:mid])                # Recursively sort left half
    right = merge_sort(arr[mid:])               # Recursively sort right half

    return merge(left, right)


def merge(left, right):                         # Merge Code Only 
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

# Time Complexity : O(n log n) in all cases
# Space Complexity : O(n) 



# LEETCODE Format CODE

class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            return merge(left, right)

        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        return merge_sort(nums)