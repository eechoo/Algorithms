#!/usr/bin/python
'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''

class Solution:
	# @param num, a list of integer
	# @return a list of lists of integers

	#@param pre num,alist of int,num
	def permute1(self,pre,num,A):
		if(len(num) == 0):
			A.append(pre)
		else:
			for i in range(len(num)):
				if(i>0 and num[i] == num[i-1]):
					continue
				A=self.permute1(pre+[num[i]],num[:i]+num[i+1:],A)
		return A

	# @param num, a list of integer
	# @return a list of lists of integers
	def permuteUnique(self, num):
		num.sort()
		result = self.permute1([],num,[])
		return result
	

def test(got, expected):
    if got == expected:
		prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.permuteUnique([1,1,2]),'')


if __name__ == '__main__':
    main()