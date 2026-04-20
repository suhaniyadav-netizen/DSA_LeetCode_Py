# Problem 234: Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        li = []
        curr = head
        while curr:
            li.append(curr.val)
            curr = curr.next
            
        left = 0
        right = len(li) - 1
        
        while left < right:
            if li[left] != li[right]:
                return False
            left += 1
            right -= 1
            
        return True

# Time Complexity: O(N)
# Space Complexity: O(N)

# Approach 2: Based on Floyd's Cycle ALGO
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
            
        left = head
        right = prev
        while right :
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True

# Time Complexity: O(N)
# Space Complexity: O(1)