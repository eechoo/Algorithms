#!/usr/bin/python
'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1  m  n  length of list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
    	if(head == None):
    		return None
    	if(m==n):
    		return head
    	node=ListNode(-1)
    	node.next=head
    	cur=head
    	tail=head=node
    	tailm=nodem=None
    	i=1
    	while (cur!=None):
    		if(i == n):
    			tmp=cur.next
    			cur.next=nodem
    			tailm.next=tmp
    			break
    		if(i == m):
    			tailm=cur
    		if(tailm!=None):
    			tail.next=cur.next
    			cur.next=nodem
    			nodem=cur
    			cur=tail.next
    			i+=1
    			continue
    		cur=cur.next
    		tail=tail.next
    		i+=1
    	return head.next

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    node1=ListNode(-2)
    node2=ListNode(2)
    node3=ListNode(-3)
    node1.next=node2
    node2.next=node3
    result=node1.reverseBetween(node1,1,2)
    while (result!=None):
    	print result.val
    	result=result.next


if __name__ == '__main__':
    main()