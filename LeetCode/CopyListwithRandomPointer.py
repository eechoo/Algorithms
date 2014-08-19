#!/usr/bin/python
'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):
		if(head == None):
			return None
		cur=head
		while(cur!=None):
			newnode=RandomListNode(cur.label)
			newnode.next=cur.next
			cur.next=newnode
			cur=cur.next.next
		cur=head
		while(cur!=None):
			if(cur.random!=None):
				cur.next.random=cur.random.next
			cur=cur.next.next
		result=new=head.next
		old=head
		while(new.next!=None):
			old.next=new.next
			old=old.next
			new.next=old.next
			new=new.next
		old.next=None
		return result

def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	node1=RandomListNode(-1)
	result=node1.copyRandomList(node1)
	print node1.label
	print node1.next


if __name__ == '__main__':
    main()