#/usr/bin/python
'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def recoverTree1(self,root,pre,result):
    	if(root.left!=None):
    		self.recoverTree1(root.left,pre,result)
    	if(pre==None):

    	if(root.right!=None):
    		pre=root
    	return (node1,node2)

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
    	if(root==None ):
    		return root
    	result=[]
    	self.recoverTree1(root,None,result)
    	if(result != []):
    		tmp=node1.val
    		node1.val=node2.val
    		node2.val=tmp
    	return root

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.maxProfit([1,2,3]),2)
    test(ins.maxProfit([3,2,1]),0)
    test(ins.maxProfit([1,4,2]),3)


if __name__ == '__main__':
    main()