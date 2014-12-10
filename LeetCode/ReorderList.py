#!/usr/bin/python
'''
Given a singly linked list L0-L1-...-Ln-1-Ln,
reorder it to: L0-Ln-L1-Ln-1-L2-Ln-2-...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

	def reverse(self,head):
		if(head == None or head.next==None):
			return head
		newhead=None
		while(head!=None):
			tmp=newhead
			newhead=head
			head=head.next
			newhead.next=tmp
		return newhead
	# @param head, a ListNode
	# @return nothing
	def reorderList(self, head):
		if(head == None or head.next==None):
			return head
		slow=fast=head
		while(fast.next!=None and fast.next.next!=None ):
			slow=slow.next
			fast=fast.next.next
		list2=slow.next
		slow.next=None
		list1=head
		list2=self.reverse(list2)
		while(list2!=None):
			tmp=list1.next
			list1.next=list2
			list2=list2.next
			list1.next.next=tmp
			list1=tmp
		return head

def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	node1=ListNode(1)
	node2=ListNode(2)
	node3=ListNode(3)
#	node4=ListNode(4)
	node1.next=node2
	node2.next=node3
#	node3.next=node4
	result=node1.reorderList(node1)
	while(result!=None):
		print result.val
		result=result.next

if __name__ == '__main__':
    main()
