#!/usr/bin/python
'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.
'''


class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if(len(s1)!=len(s2)):
        	return False
        l1=list(s1)
        l2=list(s2)
        l1.sort()
        l2.sort()
        if(l1!=l2):
        	return False
        flag=[ [[False for i in range(len(s1))] for i in range(len(s1))] for i in range(len(s1))]
        for length in range(len(s1)):
        	for i in range(len(s1)-length):
        		for j in range(len(s1)-length):
        			if(length==0): 
        				if(s1[i]==s2[j]):
        					flag[length][i][j]=True
        			else:
        				cur=False
        				for k in range(length):
        					if((flag[k][i][j] and flag[length-k-1][i+k+1][j+k+1]) or (flag[k][i][j+length-k] and flag[length-k-1][i+k+1][j])):
        						cur=True
        						break
        				flag[length][i][j]=cur
        print flag
        return flag[-1][0][0]

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.isScramble('abc','bac'),True)
    test(ins.isScramble('great','rgtae'),True)


if __name__ == '__main__':
    main()