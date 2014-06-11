#!/usr/bin/python
#Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if (num == []):
            return None
        mid=len(num)/2
        root=TreeNode(num[mid])
        if(mid>0):
            root.left=self.sortedArrayToBST(num[0:mid])
        if((len(num)-1-mid)>0):
            root.right=self.sortedArrayToBST(num[mid+1:])
        return root

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()


if __name__ == '__main__':
    main()