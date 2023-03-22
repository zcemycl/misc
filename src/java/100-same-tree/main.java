class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if ( p == null && q == null )
            return true;
        else if ( p != null && q == null )
            return false;
        else if ( p == null && q != null )
            return false;
        if (! (p.val == q.val) )
            return false;
        return this.isSameTree(p.left, q.left) && 
            this.isSameTree(p.right, q.right);

    }
}