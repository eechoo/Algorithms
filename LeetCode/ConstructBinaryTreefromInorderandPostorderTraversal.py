#!/usr/bin/python
'''
Given inorder and postorder traversal of a tree, construct the binary tree.

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
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if(inorder == [] or postorder == []):
        	return None
        root=TreeNode(postorder[-1])
        if(len(postorder) > 1):
            for i in range(len(inorder)):
            	if(inorder[i] == root.val):
            		break
            leftInorder=inorder[:i]
            rightInorder=inorder[i+1:]
            if(leftInorder != []):
                leftPostorder=postorder[:i]
                rightPostorder=postorder[i:-1]
            else:
                leftPostorder=[]
                rightPostorder=postorder[:-1]
            root.left=self.buildTree(leftInorder,leftPostorder)
            root.right=self.buildTree(rightInorder,rightPostorder)
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