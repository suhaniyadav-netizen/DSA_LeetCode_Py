# Problem 141: Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Return true if there is a cycle, and false otherwise.

# Approach 1: Brute Force
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next

        return False

# Time Complexity: O(n)
# Space Complexity: O(n)

# Floyd’s Cycle-Finding Algorithm
# The idea is to use two pointers, one slow and one fast. The slow pointer moves one step at a time, 
# while the fast pointer moves two steps at a time. 
# If there is a cycle in the linked list, the fast pointer will eventually meet the slow pointer. 
# If there is no cycle, the fast pointer will reach the end of the list.

# Approach 2: Floyd’s Cycle-Finding Algorithm (Fast and slow Pointer)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next        # slow runner moves 1 step at a time
            fast = fast.next.next   # fast runner moves 2 steps at a time
            if slow == fast:
                return True
                
        return False

# Time Complexity: O(N)
# Space Complexity: O(1)