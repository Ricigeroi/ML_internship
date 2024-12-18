class Solution:
    def has_path_sum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        def traversal(root, current_sum):
            if not root:
                return False

            current_sum += root.val

            if not root.left and not root.right:
                return current_sum == target_sum

            return traversal(root.left, current_sum) or traversal(root.right, current_sum)

        return traversal(root, 0)
