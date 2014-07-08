#!/usr/bin/python

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
    	if(num == []):
    		return 0
    	A={}
    	for i in range(len(num)):
    		A[num[i]]=True
    	max=0
    	for i in A.keys():
    		print A
    		cur=1
    		j=i+1
    		while(j in A.keys()):
    			cur+=1
    			A.pop(j)
    			j+=1
    		j=i-1
    		while(j in A.keys()):
    			cur+=1
    			A.pop(j)
    			j-=1
    		if(cur > max):
    			max=cur
    		A.pop(i)
    	return max



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.longestConsecutive([100, 4, 200, 1, 3, 2]),4)


if __name__ == '__main__':
    main()