#!/usr/bin/python
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode

    def reverseKGroup(self, head, k):
    	if(head == None or head.next==None or k==1):
    		return head
    	node=ListNode(0)
    	node.next=head
    	pre=node
    	while(pre.next !=None):
    		num=k-1
    		end=pre.next
    		while(end != None and num >0 ):
    			num-=1
    			end=end.next
    		if(end ==None):
    			break
    		bak=re=pre.next
    		unre=re.next
    		tmp=end.next
    		while(unre !=end ):
				cur=unre
				unre=unre.next
				cur.next=re
				re=cur
    		end.next=re
    		pre.next=end
    		bak.next=tmp
    		pre=bak
    	return node.next


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
	node4=ListNode(4)
	node5=ListNode(5)
	node1.next=node2
#	node2.next=node3
#	node3.next=node4
#	node4.next=node5
	result=node1.reverseKGroup(node1,1)
	while result!=None:
		print result.val
		result=result.next


if __name__ == '__main__':
    main()