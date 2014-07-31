#!/usr/bin/python

'''Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def sumNumbers2(self,leaf,curnum,sum):
        if(leaf.left == None and leaf.right == None):
            sum+=curnum*10+leaf.val
        if(leaf.left != None):
            sum=self.sumNumbers2(leaf.left,curnum*10+leaf.val,sum)
        if(leaf.right != None):
            sum=self.sumNumbers2(leaf.right,curnum*10+leaf.val,sum)
        return sum

    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if(root == None):
            return 0
        return self.sumNumbers2(root,0,0)
    	


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    root=TreeNode(1)
    left=TreeNode(2)
    right=TreeNode(3)
    root.left=left
    root.right=right
    test(root.sumNumbers(root),25)


if __name__ == '__main__':
    main()