# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_arr = []
        right_arr = []

        def left_traversal(root, arr):
            if root:
                arr.append(root.val)
                left_traversal(root.left, arr)
                left_traversal(root.right, arr)
            else:
                arr.append(None)

        def right_traversal(root, arr):
            if root:
                arr.append(root.val)
                right_traversal(root.right, arr)
                right_traversal(root.left, arr)
            else:
                arr.append(None)

        left_traversal(root.left, left_arr)
        right_traversal(root.right, right_arr)
        print(left_arr, right_arr)
        return left_arr == right_arr


