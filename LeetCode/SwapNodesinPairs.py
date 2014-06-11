#!/usr/bin/python
#Given a linked list, swap every two adjacent nodes and return its head.

#For example,
#Given 1->2->3->4, you should return the list as 2->1->4->3.

#Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
       if(head == None):
            return None
        tail=head
        if(tail.next!= None):
            head=tail.next
            tmp=tail.next.next
            tail.next.next=tail
            tail.next=tmp
        while(tail.next!=None and tail.next.next!=None):
            tmp1=tail.next.next.next
            tail.next=tail.next.next
            tail.next.next=tmp
            tmp.next=tmp1
            tmp=tmp1
            tail=tail.next.next
        return head
            
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Inorder()


if __name__ == '__main__':
    main()