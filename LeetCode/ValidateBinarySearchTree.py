#!/usr/bin/python
'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class sol:
	def isValidBST2(self,root,max,min):
		if(root.val >= max or root.val <= min):
			return False
		if(root.left != None):
			left=self.isValidBST2(root.left,root.val,min)
			if(left ==  False):
				return False
		if(root.right!=None):
			right=self.isValidBST2(root.right,max,root.val)
			if(right == False):
				return False
		return True

    # @param root, a tree node
    # @return a boolean
	def isValidBST(self, root):
		if(root == None):
			return True
		return self.isValidBST2(root,99999999,-9999999)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	ins=sol()
	root=TreeNode(1)
	root.left=TreeNode(1)
	test(ins.isValidBST(root),['()'])


if __name__ == '__main__':
    main()