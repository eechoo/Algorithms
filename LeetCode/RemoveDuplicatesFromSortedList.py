#!/usr/bin/python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Remove(object): 
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if(head==None):
            return head
        tail=head
        same=head.val
        while(tail.next != None ):
            if(tail.next.val == same):
                tail.next=tail.next.next
            else:
                same=tail.next.val
                tail=tail.next
        return head

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Remove()
    A=ListNode(1)
    A.next=ListNode(1)
    A.next.next=ListNode(2)
    test(ins.deleteDuplicates(A),A)
    while(A != None):
        print A.val
        A=A.next


if __name__ == '__main__':
    main()