#!/usr/bin/python
'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
    	if(num == []):
    		return 0
    	num.sort()
    	sum=num[0]+num[1]+num[-1]
    	for first in range(len(num)-2):
    		second=first+1
    		third=len(num)-1
    		while second < third:
    			cursum=num[first]+num[second]+num[third]
    			if(cursum -target >0):
    				third-=1
    			else:
    				second+=1
    			if(abs(cursum-target) < abs(sum-target)):
    				sum=cursum
    	return sum

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.threeSumClosest([-1,2,1,-4],1),2)
    test(ins.threeSumClosest([1,2,4,8,16,32,64,128],82),82)


if __name__ == '__main__':
    main()