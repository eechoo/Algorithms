#!/usr/bin/python
#Given a collection of numbers, return all possible permutations.

#For example,
#[1,2,3] have the following permutations:
#[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

class Solution:
	#@param pre num,alist of int,num
	def permute1(self,pre,num,A):
		length=len(num)
		if(length == 0):
			A.append(pre)
		else:
			for i in range(len(num)):
				A=self.permute1(pre+[num[i]],num[:i]+num[i+1:],A)
		return A

    # @param num, a list of integer
    # @return a list of lists of integers
	def permute(self, num):
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
    test(ins.permute([1,2,3]),[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])


if __name__ == '__main__':
    main()