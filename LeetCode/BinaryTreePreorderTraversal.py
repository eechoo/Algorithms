#!/usr/bin/python
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Preorder(object): 
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        if(root == None):
            return []
        array=[]
        array.append(root.val)
        if(root.left != None):
            array+=self.preorderTraversal(root.left)
        if(root.right != None):
            array+=self.preorderTraversal(root.right)
        return array

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