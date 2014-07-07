#!/usr/bin/python
'''Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        cur=head
    	delete=head
    	if(head.next == None and n==1):
    	    return None
    	for i in range(n):
    		cur=cur.next
    	if(cur==None):
    		head=head.next
    	else:
    	    while(cur.next):
    		    cur=cur.next
    		    delete=delete.next
    	    delete.next=delete.next.next
    	return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():



if __name__ == '__main__':
    main()