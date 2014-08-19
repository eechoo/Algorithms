#!/usr/bin/python
'''
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        if(A==[]):
        	return 1
        i=0
        while(i<len(A)):
        	if(A[i]>0 and A[i]-1!=i and A[i]<=len(A) and A[A[i]-1]!=A[i]):
        		cur=A[A[i]-1]
        		A[A[i]-1]=A[i]
        		A[i]=cur
        	else:
        		i+=1
        for i in range(len(A)):
        	if(A[i]!=i+1):
        		return i+1
        return A[i]+1


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.firstMissingPositive([2]),1)
    test(ins.firstMissingPositive([1]),2)
    test(ins.firstMissingPositive([1,1]),2)
    test(ins.firstMissingPositive([3,4,-1,1]),2)
    test(ins.firstMissingPositive([3,4,-1,1]),2)


if __name__ == '__main__':
    main()