#!/usr/bin/python
'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, , ak) must be in non-descending order. (ie,  ).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
'''
class Solution:
	def combinationSum1(self,candidates,target,combin,result):
		if(target ==0):
			result.append(combin[:])
			return combin
		for i in range(len(candidates)):
			if(i>0 and candidates[i]==candidates[i-1]):
				continue
			if(candidates[i]> target):
				return
			combin.append(candidates[i])
			self.combinationSum1(candidates[i+1:],target-candidates[i],combin,result)
			combin.pop()

    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
	def combinationSum(self, candidates, target):
		if(candidates == []):
			return [[]]
		candidates.sort()
		result=[]
		combin=[]
		self.combinationSum1(candidates,target,combin,result)
		return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.combinationSum([2,3,6,7],7),[])


if __name__ == '__main__':
    main()