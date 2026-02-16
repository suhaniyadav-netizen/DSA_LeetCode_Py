#LINKED LISTS : A linked list is a linear data structure where each element is a separate object.
# Each element (we will call it a node) of a list is comprising of two items - the data and 
# a reference to the next node. The last node has a reference to null. The entry point into a 
# linked list is called the head of the list. It should be noted that head is not a separate node,
# but the reference to the first node. If the list is empty then the head is a null reference.


from xml.dom import Node


class sll:
    def __init__(self, start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_beginning(self, data):
        if not self.is_empty():
            n=Node (self.start.data, self.start.next)
            self.start.next = n
        else:
            n=Node(data)    
            self.start = n

