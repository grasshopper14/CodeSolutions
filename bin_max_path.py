class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """   
        if root is None:
            return 0
        
        self.s = root.val
        self.maxPathSumCalc(root)
        return self.s
    def maxPathSumCalc(self,root):        
        if root is None:
            return 0
        lsum = self.maxPathSumCalc(root.left)
        rsum = self.maxPathSumCalc(root.right)        
        if lsum<0:
            lsum = 0
        if rsum<0:
            rsum = 0
        self.s = max(self.s,lsum+rsum+root.val)        
        return max(lsum,rsum)+root.val
