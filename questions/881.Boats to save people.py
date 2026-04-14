#LEETCODE PROBLEM NO 881 : BOATS TO SAVE PEOPLE

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i = 0
        j = len(people) - 1
        boats = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            boats += 1
        return boats
    
# time complexity is O(n log n) due to sorting and space complexity is O(1)