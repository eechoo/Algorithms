#!/usr/bin/python
'''
Given a collection of integers that might contain duplicates, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
class Solution:
	def IsDup(self,num,S):
		for i in range(len(S)):
			if(num == S[i]):
				return True
		return False

	def subsetsWithDup2(self,S,level,solu,result):
		if(len(solu)==level):
			result.append(solu[:])
		else:
			for i in range(len(S)):
				if(not self.IsDup(S[i],S[:i])):
					solu.append(S[i])
					self.subsetsWithDup2(S[i+1:],level,solu,result)
					solu.pop()

    # @param num, a list of integer
    # @return a list of lists of integer
	def subsetsWithDup(self, S):
		result=[]
		solu=[]
		if(S==[]):
			return []
		else:
			S.sort()
			for i in range(len(S)+1):
				self.subsetsWithDup2(S,i,solu,result)
		return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.subsetsWithDup([1,2,2]),[[1],[]])

if __name__ == '__main__':
    main()