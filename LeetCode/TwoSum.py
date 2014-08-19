#!/usr/bin/python
'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''


class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		MapNum={}
		for  i in range(len(num)):
			if(MapNum.has_key(target-num[i])):
				index1=MapNum[target-num[i]]+1
				index2=i+1
			else:
				MapNum[num[i]]=i
		return (index1,index2)

def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	ins=Solution()
	test(ins.twoSum([2,7,11,15],9),(1,2))
	test(ins.twoSum([0,4,3,0],0),(1,4))
	test(ins.twoSum([5,75,25],100),(2,3))

if __name__ == '__main__':
    main()