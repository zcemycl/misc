class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    @classmethod
    def maxDepth(cls, root):
        if root == None:
            return 0
        left = cls.maxDepth(root.left)
        right = cls.maxDepth(root.right)
        return 1+max(left,right)


if __name__ == "__main__":
    n9 = TreeNode(val=9)
    n7 = TreeNode(val=7)
    n15 = TreeNode(val=15)
    n20 = TreeNode(val=20, left=n15, right=n7)
    n3 = TreeNode(val=3, left=n9, right=n20)

    n1 = TreeNode(val=1, right=TreeNode(val=2))

    print(Solution.maxDepth(n3))
    print(Solution.maxDepth(n1))
