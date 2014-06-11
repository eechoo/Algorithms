#!/usr/bin/python
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isMirror(self,)

    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if(root == None):
            return False
        if(root.left == None and root.right == None):
            return True
        if(root.left != None and root.right != None):
            return self.isMirror(root.left,root.right)
            
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Inorder()


if __name__ == '__main__':
    main()