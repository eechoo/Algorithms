#!/usr/bin/python
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
    	if(A==[]):
    		return 0
    	left=[0 for i in range(len(A))]
    	right=[0 for i in range(len(A))]
    	max=A[0]
    	for i in range(len(A)):
    		if(max < A[i]):
    			max=A[i]
    		left[i]=max
    	max=A[-1]
    	for i in range(len(A)-1,-1,-1):
    		if(max < A[i]):
    			max=A[i]
    		right[i]=max
    	sum=0
    	for i in range(len(A)):
    		if(left[i] > right[i] ):
    			sum+=(right[i]-A[i])
    		else:
    			sum+=(left[i]-A[i])
    	return sum


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.trap([0,1,0,2,1,0,1,3,2,1,2,1]),6)


if __name__ == '__main__':
    main()