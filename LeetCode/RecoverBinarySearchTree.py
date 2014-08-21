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

    def recoverTree1(self,cur,pre,result):
    	if(cur==None):
    		return None
    	if(cur.left!=None):
    		pre=self.recoverTree1(cur.left,pre,result)
    	if(pre!=None):
    		if(pre.val > cur.val):
    			if(result==[]):
    				result.append(pre)
    				result.append(cur)
    			else:
    				result.pop()
    				result.append(cur)
    	pre=cur
    	if(cur.right!=None):
    		pre=self.recoverTree1(cur.right,pre,result)
    	return pre

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
    	if(root==None ):
    		return root
    	result=[]
    	self.recoverTree1(root,None,result)
    	if(result != []):
    		tmp=result[0].val
    		result[0].val=result[1].val
    		result[1].val=tmp
    	return root

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node2.left=node3
    node2.right=node1
    root=node2.recoverTree(node2)
    print root.left.val
    print root.right.val


if __name__ == '__main__':
    main()