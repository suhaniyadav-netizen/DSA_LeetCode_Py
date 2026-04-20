# Problem 160: Intersection of Two Linked Lists

# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
# If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Approach 1: Brute Force - Nested while loop
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curr_a = headA
        while curr_a:
            curr_b = headB
            while curr_b:
                if curr_a == curr_b:
                    return curr_a
                curr_b = curr_b.next
            curr_a = curr_a.next
            
        return None

# Time Complexity: O(M * N) - m and n are lengths of two linked lists [Time Limit Exceeded]
# Space Complexity: O(1): No extra memory used.

# Approach 2: Two Pointers
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ele_a = headA
        ele_b = headB

        while ele_a != ele_b:
            if ele_a is None:
                ele_a = headB
            else:
                ele_a = ele_a.next

            if ele_b is None:
                ele_b = headA
            else:
                ele_b = ele_b.next
                
        return ele_a

# Time Complexity: O(m+n): We walk each trail a maximum of two times
# Space Complexity: O(1)