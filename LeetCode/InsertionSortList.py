#!/usr/bin/python
#Sort a linked list using insertion sort.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
    	if(head == None or head.next==None):
    		return head
    	pre=head
    	cur=head.next
    	while (cur!=None):
    		pos=head
    		while(cur.val >= pos.val and pos != cur):
    			psopre=pos
    			pos=pos.next
    		if(pos == cur):
    			pre=cur
    			cur=cur.next
    		elif(pos == head):
    			pre.next=cur.next
    			cur.next=head
    			head = cur
    			cur=pre.next
    		else:
    			pre.next=cur.next
    			psopre.next=cur
    			cur.next=pos
    	return head

    def insertionSortList1(self, head):
    	if(head == None or head.next==None):
    		return head
    	cur=head.next
    	head.next=None
    	pos=head
    	pospre=None
    	while (cur!=None):
    		if(pospre !=None and pospre.val > cur.val):
    			pos=head
    			pospre=None
#    		elif(pos == None and pospre.val > cur.val):
#    			pos=head
#    			pospre=None
    		while(pos != None and cur.val>pos.val ):
    			pospre=pos
    			pos=pos.next
    		tmp=cur.next
    		if(pospre != None):
    			pospre.next=cur
    		else:
    			head=cur
    		cur.next=pos
    		cur=tmp
    	return head

    def insertionSortList2(self, head):
    	if(head == None or head.next== None):
    		return head
    	node=ListNode(0)
    	node.next=head
    	pos=sortedEnd=node.next
    	while (sortedEnd.next!=None):
    		cur=sortedEnd.next
    		if(pos.val > cur.val):
    			pos=node
    		while(pos != sortedEnd and cur.val>pos.next.val ):
    			pos=pos.next
    		if(pos == sortedEnd):
    			sortedEnd=sortedEnd.next
    			continue
    		sortedEnd.next=cur.next
    		cur.next=pos.next
    		pos.next=cur
    	return node.next

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    node2=ListNode(2)
    node1=ListNode(1)
    node3=ListNode(3)
    node4=ListNode(4)
    node3.next=node4
    node4.next=node1
    result=node2.insertionSortList2(node3)
    while(result != None):
    	print result.val
    	result=result.next

if __name__ == '__main__':
    main()