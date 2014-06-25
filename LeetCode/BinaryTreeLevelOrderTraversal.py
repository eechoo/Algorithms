#!/usr/bin/python

#Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def levelOrder(self, root):
    	A=[]
    	if(root ==None):
    		return A
    	i=0
    	tool=[root]
    	while(tool != []):
    		A.append([])
    		for j in range(len(tool)):
    			cur=tool.pop(0)
    			if(cur.left != None):
    				tool.append(cur.left)
    			if(cur.right != None):
    				tool.append(cur.right)
    			A[i].append(cur.val)
    		i+=1
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
	test(node1.levelOrder(node1),[[5], [3, 7], [9]])
	test(node11.levelOrder(node11),[[1]])

if __name__ == '__main__':
    main()
