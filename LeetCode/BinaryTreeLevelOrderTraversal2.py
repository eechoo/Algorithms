#!/usr/bin/python
#Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def levelOrderBottom(self, root):
    	if(root == None):
    		return []
    	queue=[root]
    	A=[]
    	i=0
    	while (queue!=[]):
    		A.append([])
    		for j in range(len(queue)):
    			tree=queue.pop(0)
    			if(tree.left != None):
    				queue.append(tree.left)
    			if(tree.right!= None):
    				queue.append(tree.right)
    			A[i].append(tree.val)
    		i+=1
    	A.reverse()
    	return A


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	node1=TreeNode(5)
	node2=TreeNode(3)
	node3=TreeNode(7)
	node4=TreeNode(9)
	node1.left=node2
	node1.right=node3
	node3.right=node4
	node11=TreeNode(1)
	test(node1.levelOrderBottom(node1),[[9], [3, 7], [5]])
	test(node11.levelOrderBottom(node11),[[1]])

if __name__ == '__main__':
    main()