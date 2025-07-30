### Reversing Linked List

# The first function here simply takes a linked list and prints it in reverse
# order.
# We solve this using recursion. We recurse until we hit the end of the list,
# then as the stack executes, we print at each stage. this has the effect of
# printing the stage backward.

def reversePrint(head):
    if head is None:
        return
    reversePrint(head.next)
    print(head.data)

# Reversing a linked list.
# We can do it this way, using a sort of swap. We take our next node, set out
# current node's pointer to point at the previous node (None, at the head of the
# list), then set our previous node to the current node, and hop on to the next.
# This is more clear if we call llist something like "head" or "current"

def reverse(llist):
    if not llist:
        return None

    prev = None
    while llist:
        next_node = llist.next
        llist.next = prev
        prev = llist
        llist = next_node
