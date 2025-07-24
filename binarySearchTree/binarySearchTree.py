class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validates if a given binary tree is a valid Binary Search Tree (BST).

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is a valid BST, False otherwise.
        """
        return self._validate(root, float('-inf'), float('inf'))

    def _validate(self, node: TreeNode, lower_bound: float, upper_bound: float) -> bool:
        """
        Helper function to recursively validate the BST properties for a given node
        within specified lower and upper bounds.

        Args:
            node: The current node to validate.
            lower_bound: The minimum allowed value for nodes in the current subtree.
            upper_bound: The maximum allowed value for nodes in the current subtree.

        Returns:
            True if the subtree rooted at 'node' is a valid BST within the bounds,
            False otherwise.
        """
        if not node:
            # An empty tree or an empty subtree is a valid BST.
            return True

        # Check if the current node's value is within the allowed bounds.
        if not (lower_bound < node.val < upper_bound):
            return False

        # Recursively validate the left subtree:
        # The new upper bound for the left child is the current node's value,
        # as all nodes in the left subtree must be less than the current node.
        if not self._validate(node.left, lower_bound, node.val):
            return False

        # Recursively validate the right subtree:
        # The new lower bound for the right child is the current node's value,
        # as all nodes in the right subtree must be greater than the current node.
        if not self._validate(node.right, node.val, upper_bound):
            return False

        # If all checks pass, the current subtree is valid.
        return True
