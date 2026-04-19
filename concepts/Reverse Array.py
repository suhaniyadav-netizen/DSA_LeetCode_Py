
# # to print reversed array without builtin functions

a = [3,4,7,6]
s = a.reverse()
print(s)  # This will print 'None' because reverse() modifies the list in place and returns None
print(a)  # This will print the reversed list: [6, 7, 4, 3]


# # without builtin functions
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list
b = [1, 2, 3, 4, 5]
print(reverse_list(b))
 

# # another method
arr = [3,4,7,6]
def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
        return arr
print(reverse_array(arr))
