#!/usr/bin/python
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if(root==None):
            return False
        if(root.left==None and root.right==None):
            if(root.val==sum):
                return True
            else:
                return False
        if(root.left != None):
            isLeft=self.hasPathSum(root.left,sum-root.val)
            if(isLeft == True):
                return True
        if(root.right != None):
            isRight=self.hasPathSum(root.right,sum-root.val)
            if(isRight==True):
                return True
            else:
                return False
        return False

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    root=TreeNode(5)
    node1=TreeNode(4)
    node2=TreeNode(8)
    root.left=node1
    root.right=node2
    test(root.hasPathSum(root,9),True)


if __name__ == '__main__':
    main()