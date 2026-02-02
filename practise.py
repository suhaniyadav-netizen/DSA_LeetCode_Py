
# # to print reversed array without builtin functions

# a = [3,4,7,6]
# s = a.reverse()
# print(s)  # This will print 'None' because reverse() modifies the list in place and returns None
# print(a)  # This will print the reversed list: [6, 7, 4, 3]


# # without builtin functions
# def reverse_list(lst):
#     reversed_list = []
#     for i in range(len(lst) - 1, -1, -1):
#         reversed_list.append(lst[i])
#     return reversed_list
# b = [1, 2, 3, 4, 5]
# print(reverse_list(b))
 

# # another method
# arr = [3,4,7,6]
# def reverse_array(arr):
#     start = 0
#     end = len(arr) - 1
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
#         return arr
# print(reverse_array(arr))


# # palindrome check --- python approach 
# def palindrome(l):
#     n=len(l)
#     for i in range(n//2):
#         if l[i] != l[n-i-1]:
#             return False
#     return True
# print(palindrome([1,2,3,2,1]))  # True
# print(palindrome([1,2,3,4,5]))  # False


# # another method for palindrome ---- General approach
# def is_palindrome(a):
#     left = 0
#     right = len(a) - 1
#     while left < right:
#         if a[left] != a[right]:
#             return False
#         left += 1
#         right -= 1
#     return True
# print(is_palindrome([1,2,3,2,1]))  # True


# # input a number, check if it's even or odd then check if it's prime or not using single function general approach

# def check_number(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
#     if num <= 1:
#         print("input valid number greater than 1")
#     else:
#         for i in range(2,num//2):
#             if num % i == 0:
#                 print("not prime")
#                 break
#         else:
#             print("prime")

# check_number(11)


# # given array = [0,2,0,4,3,0,7,8,0]
# # after moving zeros to end => [2,3,4,7,8,0,0,0,0]

# arr = [0,2,0,4,3,0,7,8,0]
# new_arr=[]

# for i in arr:                                  # O(n) time complexity since loop 
#     if i != 0:
#         new_arr.append(i)
# new_arr.sort()                                 # used sorting therefore time complexity is O(log n)

# c = arr.count(0)

# for j in range(c):
#     new_arr.append(0)
# print(new_arr)                                 # final time complexity is O(n log n) and space complexity is O(n)


# # new method O(n) time complexity and O(1) space complexity without sorting method :

# arr = [0,2,0,4,3,0,7,8,0]
# i = 0
# j = 1
# while i<j and j<len(arr):
#     if arr[i] == 0 and arr[j] == 0:
#         j+=1
#     elif arr[i] == 0 and arr[j] != 0:
#         arr[i], arr[j] = arr[j], arr[i]
#         i+=1
#         j+=1
#     else:
#         i+=1
#         j+=1
# print(arr) 


# Print elements in the given list :            

# l = [ [2,5,6], [3,1,7], [5,2,1] ]              # it's a 2D list we need nested loops therefore O(n^2) time complexity
# for i in range(len(l)):
#     for j in range(len(l[i])):
#         print(l[i][j] , end=" ")
#     print()


# make a list add elements and find the max element from the list without using builtin functions
# maxi = -math.inf means minus infinity 

import math


arr = [3,4,5,6,7,12,0,15,8]
n = arr[0]
for i in range(1, len(arr)):
    if arr[i] > n:
        n = arr[i]
print(n)

# time complexity is O(n) and space complexity is O(1)

#to find the second highest value from the list without using builtin functions

arr = [3,4,5,6,7,12,0,15,8]
m = arr[0]
n = arr[1]
for i in range(len(arr)):
    if arr[i] > m:
        n = m
        m = arr[i]
    elif arr[i] > n and arr[i] != m:
        n = arr[i]
print(n)

# time complexity is O(n) and space complexity is O(1)

# another method ( sir vala )
import math
arr = [3,4,5,6,7,12,0,15,8]
maxi = -math.inf
mini = -math.inf
for i in arr:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i
print(maxi, mini)

# time complexity is O(n) and space complexity is O(1)

# LEETCODE PROBLEM NUMBER 412 : FIZZ BUZZ

def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                res.append("FizzBuzz")
            elif i%3==0:
                res.append("Fizz")
            elif i%5==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
# time complexity is O(n) and space complexity is O(n)




