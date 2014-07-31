#!/usr/bin/python
'''
DFS
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def pathSum1(self,root,sum,result):


    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
    	result=[]
    	if(root==None):
            return result
        return self.pathSum1(root,sum,result)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.generateParenthesis(1),['()'])
    test(ins.generateParenthesis(2),['(())','()()'])
    test(ins.generateParenthesis(3),['((()))','(()())','(())()','()(())','()()()'])


if __name__ == '__main__':
    main()