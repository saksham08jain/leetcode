# Last updated: 5/6/2025, 11:07:34 pm
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self,root: TreeNode, targetSum: int) -> int:
        def dfs(node: TreeNode, current_sum: int) -> int:
            if not node:
                return 0
            
            # Update current sum
            current_sum += node.val
            
            # Check if we have a valid path ending at current node
            count = prefix_sums[current_sum - targetSum]
            
            # Update prefix sum count
            prefix_sums[current_sum] += 1
            
            # Recurse on left and right children
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            
            # Backtrack: remove current sum from prefix_sums
            prefix_sums[current_sum] -= 1
            
            return count

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # To handle paths starting from root
        return dfs(root, 0)