#!/usr/bin/python
'''
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#insert a node into root.if not return False
    def creatTree(self,start,end):
		if(start > end):
			return [None]
		else:
			root=[]
			for i in range(start,end+1):
				left=self.creatTree(start,i-1)
				right=self.creatTree(i+1,end)
				for l in range(len(left)):
					for r in range(len(right)):
						root.append(TreeNode(i))
						root[-1].left=left[l]
						root[-1].right=right[r]
			return root

    # @return a list of tree node
    def generateTrees(self, n):
    	if(n==0):
    		return [None]
    	else:
    		return self.creatTree(1,n)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=TreeNode(1)
    result=ins.generateTrees(2),
    for i in range(len(result[0])):
    	print result[0][i]


if __name__ == '__main__':
    main()