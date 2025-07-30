### Tree Traversal

# Pre Order Traversal. We process the root node, then left tree, then right tree.
# The best way to do this, is recursion. This, as well as In Order and Post
# Order, are Depth First Searches.

def preOrder(root):
    if root is not None:
        print(root.data, end=' ')
        preOrder(root.left)
        preOrder(root.right)


# In Order Traversal
# In this case we process the left tree, then the root node, then the right
# tree.

def inOrder(root):
    if root is None:
        return
    inOrder(root.left)
    print(root.info, end=' ')
    inOrder(root.right)

# PostOrder Traversal
# In this case we process the left tree, then the right tree, then the root
# node. As you can see, with this recursion based solution, the difference
# really just depends on where we place our logic.

def postOrder(root):
    if root is None:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.info, end=' ')

# Finding the height of a tree
# We just combine out depth first search with a counter, to check how many edges
# we pass to get to the bottom of the tree. When the node is None we return -1 to
# decrement the counter to show we pass no edges. We add with each return to
# show that we passed an edge.

def height(root):
    if root is None:
        return -1
    else: 
        return 1 + max(
            height(root.left),
            height(root.right)
            )

# Level order traversal
# This is also known as a breadth first search. In this case we use a queue
# rather than a stack, since we take nodes in a FIFO order. We can't use
# recursion for this reason.

from collection import deque

def levelOrder(root):
    que = deque([root])
    while que:
        current_length = len(que)
        for _ in range(current_length):
            node = que.popleft()
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
            print(node.info, end=' ')
