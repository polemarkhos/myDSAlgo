### Inserting Nodes

# Insert at tail
# This code iterates through the linked list until it reaches the end, then
# creates a new node SinglyLinkedListNode() implemented elsewhere.
# head is the pointer to the head node of the LL, data is the data to insert


def insertNodeAtTail(head, data):
    if not head:
        return SinglyLinkedListNode(data)

    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = SinglyLinkedListNode(data)
    return head


# Insert at head
# Interestingly, this is even easier.
# We create a new node, and simply append the rest of the list


def insertNodeAtHead(llist, data):
    newNode = SinglyLinkedListNode(data)
    newNode.next = llist

    return newNode


# Insert at a given position
# Given a linked list, a position and data to insert, we simply iterate along
# the list until we reach the position, then "save" the next node, add our new
# node as the next node, then set the pointer in our new node to our saved node.


def insertNodeAtPosition(llist, data, position):
    newNode = SinglyLinkedListNode(data)
    curr = llist
    for i in range(position - 1):
        curr = curr.next

    afterNode = curr.next
    curr.next = newNode
    newNode.next = afterNode

    return llist


# Delete a node at the given position
# This works very similarly to inserting a node, only we follow the pointers to
# the node after we want to delete, then set our next node pointer to that. If
# you're using a non garbage collected language you would probably need to
# manually dealloc that node


def deleteNode(llist, position):
    curr = llist
    if position == 0:
        llist = llist.next
        return llist

    for i in range(position - 1):
        curr = curr.next

    if curr.next.next:
        twoAfterNode = curr.next.next
        curr.next = twoAfterNode
    else:
        curr.next = None

    return llist
