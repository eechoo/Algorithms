#!/usr/bin/python
#Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

#For example,
#Given 1->2->3->3->4->4->5, return 1->2->5.
#Given 1->1->1->2->3, return 2->3.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
    	if(head == None or head.next==None):
    		return head
    	pre=head
    	tail=head.next
    	curval=pre.val
    	delete=None
    	while(tail!=None):
    		if(tail.val == curval ):
    			delete=curval
    		else:
    			if(pre.val == delete):
    				pre=tail
    				if(head.val == delete ):
    					head=tail
    			elif(pre.next != tail and pre.next.val!= delete):
    			    pre=pre.next
    			elif(pre.next!=tail and pre.next.val== delete):
    				pre.next=tail
    			curval=tail.val
    		if(tail.next == None and tail.val == delete):
    			if(pre.val == delete):
    				pre=tail.next
    				if(head.val == delete):
    					head=tail.next
    			else:
    			    pre.next=None
    		tail=tail.next
    	tmp=head
    	while(head):
    		print head.val
    		head=head.next
    	return head

    def deleteDuplicates(self, head):
    	if(head == None or head.next==None):
    		return head
    	virHead=ListNode(-9999)
    	virHead.next=head
    	head=virHead
    	pre=head
    	cur=head.next
    	tail=cur.next
    	dup=False
    	while(tail != None):
    		if(tail.val == cur.val):
    			dup=True
    		else:
    			if( dup ):
    				pre.next=tail
    			else:
    				pre=cur
    			dup=False
    		tail=tail.next
    		cur=cur.next
    	if(dup):
    	    pre.next=None
    	return head.next

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=ListNode(1)
    ins2=ListNode(2)
    ins3=ListNode(2)
    ins4=ListNode(3)
    ins.next=ins2
    ins2.next=ins3
    ins3.next=ins4
    ins4.next=None
    test(ins.deleteDuplicates(ins),None)


if __name__ == '__main__':
    main()