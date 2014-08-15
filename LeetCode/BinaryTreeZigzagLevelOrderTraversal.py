#!/usrbin/python
'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
		A=[]
		if(root == None):
			return A
		level=1
		tool=[root]
		while(tool != []):
			A.append([])
			for j in range(len(tool)):
				cur=tool.pop(0)
				A[-1].append(cur.val)
				if(level %2 == 1):
					if(cur.left != None):
						tool.append(cur.left)
					if(cur.right != None):
						tool.append(cur.right)
				else:
					if(cur.right != None):
						tool.append(cur.right)
					if(cur.left != None):
						tool.append(cur.left)
			level+=1
			tool.reverse()
		return A
        

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
    left1=TreeNode(4)
    right1=TreeNode(5)
    node1=TreeNode(7)
    root.left=left
    root.right=right
    left.left=left1
    right.right=right1
    right.left=node1
    test(root.zigzagLevelOrder(root),['()'])

if __name__ == '__main__':
    main()