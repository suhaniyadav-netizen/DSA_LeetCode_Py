
# # palindrome check --- python approach 
def palindrome(l):
    n=len(l)
    for i in range(n//2):
        if l[i] != l[n-i-1]:
            return False
    return True
print(palindrome([1,2,3,2,1]))  # True
print(palindrome([1,2,3,4,5]))  # False


# another method for palindrome ---- General approach
def is_palindrome(a):
    left = 0
    right = len(a) - 1
    while left < right:
        if a[left] != a[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome([1,2,3,2,1]))  # True