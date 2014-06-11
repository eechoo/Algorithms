#!/usr/bin/python
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def ismirror(self,left,right):
        if(left.val != right.val):
            return False
        mirror1=False
        mirror2=False
        if(left.right != None and right.left != None):
            mirror1=self.ismirror(left.right,right.left)
        elif(left.right == None and right.left == None):
            mirror1=True
        if(left.left!= None and right.right != None):
            mirror2=self.ismirror(left.left,right.right)
        elif(left.left == None and right.right  == None):
            mirror2=True
        if(mirror1 == True and mirror2 == True):
            return True
        return False

    def isSymmetric(self, root):
        if(root == None):
            return True
        if(root.left == None and root.right == None):
            return True
        elif(root.left != None and root.right != None):
            return self.ismirror(root.left,root.right)
        else:
            return False
            
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