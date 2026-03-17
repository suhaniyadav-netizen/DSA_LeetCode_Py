
# REVERSE LINKED LIST 

def reverse(self,head):
    curr = head
    temp = None
    prev = None
    while curr is not None :
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev



