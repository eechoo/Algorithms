#!/usr/bin/python
'''
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if(k==0 or head==None):
        	return head
        cur=head
        i=0
        while (i<k):
        	if(cur.next==None):
        		cur=head
        	else:
        		cur=cur.next
        	i+=1
        pre=head
        while(cur.next):
        	cur=cur.next
        	pre=pre.next
        cur.next=head
        head=pre.next
        pre.next=None
        return head
        
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if(k==0 or head==None):
        	return head
        cur=head
        i=1
        while (cur.next and i<=k):
        	cur=cur.next
        	i+=1
        if(cur.next==None and i<=k):
        	if(i==k):
        		return head
        	k%=i
        	i=1
        	cur=head
        	while (cur.next and i<=k):
        		cur=cur.next
        		i+=1
        pre=head
        while(cur.next):
        	cur=cur.next
        	pre=pre.next
        cur.next=head
        head=pre.next
        pre.next=None
        return head


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.maxProfit([1,2,3]),2)
    test(ins.maxProfit([3,2,1]),0)
    test(ins.maxProfit([1,4,2]),3)


if __name__ == '__main__':
    main()