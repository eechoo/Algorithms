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