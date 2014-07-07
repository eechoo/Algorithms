#!/usr/bin/python
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Preorder(object): 
    def findnext(self,root):
        while(root):
            if(root.next!=None and (root.next.left !=None or root.next.right!=None)):
                return root.next
            else:
                root=root.next
        return None

    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if(root == None):
            return 
        if(root.left == None and root.right == None):
            return
        elif(root.left != None and root.right != None):
            root.left.next=root.right
        p=self.findnext(root)
        linkedChild=None
        if(root.right!=None):
            linkedChild=root.right
        elif(root.left!=None):
            linkedChild=root.left
        if(linkedChild != None):
            if( p!= None and p.left != None):
                linkedChild.next=p.left
            elif(p!=None and p.right!=None):
                linkedChild.next=p.right
        self.connect(root.right)
        self.connect(root.left)



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Preorder()


if __name__ == '__main__':
    main()