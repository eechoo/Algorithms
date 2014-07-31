#!/usr/bin/python
#Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def sortedListToBST1(self,B):
		print B
		if(len(B) == 1):
			return TreeNode(B[0])
		elif(len(B)==0):
			return None
		mid=len(B)/2
		ins=TreeNode(B[mid])
		ins.left=self.sortedListToBST1(B[:mid])
		ins.right=self.sortedListToBST1(B[mid+1:])
		return ins
    # @param head, a list node
    # @return a tree node
	def sortedListToBST(self, head):
		if(head == None):
			return None
		tmp=head
		#count the length of the list
		B=[]
		while(tmp):
			B.append(tmp.val)
			tmp=tmp.next
		X=self.sortedListToBST1(B)
		return X

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.sortedListToBST1([1,3]),0)
if __name__ == '__main__':
    main()