# LINEAR SEARCH
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

#time complexity: O(n)
#space complexity: O(1)