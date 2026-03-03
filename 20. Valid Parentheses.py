# LEETCODE PROBLEM NUMBER 20 : Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the 
# input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false



class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if i==")" and top != '(':
                    return False
                if i=="}" and top != '{':
                    return False
                if i=="]" and top != '[':
                    return False
        return len(stack) == 0    
        