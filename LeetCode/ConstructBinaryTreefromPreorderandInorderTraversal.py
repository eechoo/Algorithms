#!/usr/bin/python
'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if(inorder == [] or preorder == []):
        	return None
        root=TreeNode(preorder[0])
        if(len(preorder) > 1):
            for i in range(len(inorder)):
            	if(inorder[i] == root.val):
            		break
            leftInorder=inorder[:i]
            rightInorder=inorder[i+1:]
            if(leftInorder != []):
                leftPreorder=preorder[1:i+1]
                rightPreorder=preorder[i+1:]
            else:
                leftPreorder=[]
                rightPreorder=preorder[1:]
            root.left=self.buildTree(leftPreorder,leftInorder)
            root.right=self.buildTree(rightPreorder,rightInorder)
        return root


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.generateParenthesis(1),['()'])


if __name__ == '__main__':
    main()