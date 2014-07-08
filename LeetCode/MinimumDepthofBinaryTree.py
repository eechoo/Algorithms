#!/usr/bin/python
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
    	if(root == None):
    		return 0
    	A=[root]
    	level=1
    	num=0
    	while(len(A)!=0):
    		num=len(A)
    		for i in range(num):
    			cur=A.pop(0)
    			if(cur.left == None and cur.right == None):
    				return level
    			if(cur.left != None):
    				A.append(cur.left)
    			if(cur.right != None):
    				A.append(cur.right)
    		level+=1
    	return level
    		

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins1=TreeNode(1)
    ins2=TreeNode(2)
    ins3=TreeNode(3)
    ins4=TreeNode(4)
    ins5=TreeNode(5)
    ins1.left,ins1.right=ins2,ins3
    ins2.left=ins4
    ins3.right=ins5
    test(ins1.minDepth(ins1),3)


if __name__ == '__main__':
    main()