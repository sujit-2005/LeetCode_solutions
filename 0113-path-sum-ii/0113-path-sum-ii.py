# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        if not root:
            return []

        result = []
        stack = [(root, targetSum, [root.val])]

        while stack:
            node, current_sum, path = stack.pop()

            if not node.left and not node.right and current_sum == node.val:
                result.append(path)
                continue

            if node.right:
                stack.append((node.right, current_sum - node.val, path + [node.right.val]))

            if node.left:
                stack.append((node.left, current_sum - node.val, path + [node.left.val]))

        return result