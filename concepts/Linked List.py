#LINKED LISTS : A linked list is a linear data structure where each element is a separate object.
# Each element (we will call it a node) of a list is comprising of two items - the data and 
# a reference to the next node. The last node has a reference to null. The entry point into a 
# linked list is called the head of the list. It should be noted that head is not a separate node,
# but the reference to the first node. If the list is empty then the head is a null reference.


from xml.dom import Node


# class sll:
#     def __init__(self, start=None):
#         self.start = start
#     def is_empty(self):
#         return self.start == None
#     def insert_at_beginning(self, data):
#         if not self.is_empty():
#             n=Node (self.start.data, self.start.next)
#             self.start.next = n
#         else:
#             n=Node(data)    
#             self.start = n


# BASIC STRUCTURE OF LL :
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# INSERT AT BEGINNING :                    # time complexity is O(1) and space complexity is O(1) 
def insert_begin(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node       


# INSERT AT END :                          # time complexity is O(n) and space complexity is O(1)
def insert_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head


# DELETE A NODE :                          # time complexity is O(n) and space complexity is O(1)
def delete_node(head, key):
    temp = head
    if temp and temp.data == key:
        return temp.next
    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next
    if temp:
        prev.next = temp.next
    return head

# TRAVERSE A LINKED LIST :                    # time complexity is O(n) and space complexity is O(1)
def display(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next