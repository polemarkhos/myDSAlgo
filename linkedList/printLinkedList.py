# Printing a Linked List

# The function prints the contents of the head node, then moves on to the next
# node by setting var head to head.next, which is the pointer to the next node
# in the list. It continues to do this until there is no next node.

def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next
