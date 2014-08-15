#!/usr/bin/python
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:Elements in a triplet (a,b,c) must be in non-descending order (ie, a  b  c)

The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
    	if(num == []):
    		return []
    	num.sort()
    	result=[]
    	for first in range(len(num)-2):
    		if(first>0 and num[first] == num[first-1]):
    			continue
    		second=first+1
    		third=len(num)-1
    		while(second < third):
    			if(second > first+1 and num[second]==num[second-1]):
    				second+=1
    				continue
    			if(third < len(num)-1 and num[third]==num[third+1]):
    				third-=1
    				continue
    			sum=num[first]+num[second]+num[third]
    			if(sum == 0):
    				result.append([num[first],num[second],num[third]])
    			if(sum > 0):
    				third-=1
    			else:
    				second+=1
    	return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.threeSum([-1,0,1,2,-1,-4]),[])


if __name__ == '__main__':
    main()