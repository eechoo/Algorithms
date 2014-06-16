#!/usr/bin/python
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
    	A=[]
    	if(root == None):
    		return A
    	if(root.left != None):
    		A=self.postorderTraversal(root.left)
    	if(root.right != None):
    		A+=self.postorderTraversal(root.right)
    	A.append(root.val)
    	return A


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    root=TreeNode(7)
    Tleft=TreeNode(3)
    Tright=TreeNode(4)
    root.left=Tleft
    root.right=Tright
    test(root.postorderTraversal(root),[3,4,7])


if __name__ == '__main__':
    main()