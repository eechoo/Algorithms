#!/usr/bin/python
'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2,  , ak) must be in non-descending order. (ie, a1  a2  ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
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
	def combinationSum2(self, candidates, target):
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
    test(ins.combinationSum2([10,1,2,7,6,1,5],8),2)


if __name__ == '__main__':
    main()