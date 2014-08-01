#!/usr/bin/python
'''
DFS
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''

# Definition for a  binary tree node
class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

  def pathSum1(self,node,sum,path,result):
    path.append(node.val)
    if(node.left == None and node.right==None and sum == node.val):
      result.append(path[:])
    if(node.left != None):
      self.pathSum1(node.left,sum-node.val,path,result)
    if(node.right != None):
      self.pathSum1(node.right,sum-node.val,path,result)
    path.pop()

    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
  def pathSum(self, root, sum):
    path=[]
    result=[]
    if(root != None):
      self.pathSum1(root,sum,path,result)
    return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    root=TreeNode(5)
    left=TreeNode(4)
    right=TreeNode(8)
    root.left=left
    root.right=right
    test(root.pathSum(root,13),[])

if __name__ == '__main__':
    main()