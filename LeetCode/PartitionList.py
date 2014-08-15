#!/usr/bin/python
'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
    	if(head==None):
    		return None
    	pre=small=None
    	cur=head
    	while (cur!=None):
    		if(cur.val < x):
    			if(small == None):
    				small=cur
    				if(cur!=head):
    					pre.next=cur.next
    					small.next=head
    					head=small
    					cur=pre
    			elif(small == pre):
    				small=cur
    			else:
    				pre.next=cur.next
    				tmp=small.next
    				small.next=cur
    				cur.next=tmp
    				small=small.next
    				cur=pre
    		pre=cur
    		cur=cur.next
    	return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    head=ListNode(1)
    head.next=ListNode(2)
    result=head.partition(head,3)
    while(result!= None):
    	print result.val
    	result=result.next

if __name__ == '__main__':
    main()