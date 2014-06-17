#!/usr/bin/python
#Given a collection of numbers that might contain duplicates, return all possible unique permutations.

#For example,
#[1,1,2] have the following unique permutations:
#[1,1,2], [1,2,1], and [2,1,1].

class Solution:
	def swap(self,a,b):
		tmp=a
		a=b
		b=tmp

	#@param num,alist of int
	#@param n ,int
	#@param A , a List of List of int 
	def permute1(self,num,n,A):
		if(n == len(num)):
			A.append(num)
		for i in range(n,len(num)):
			if(num[i] != num[n] ):
				self.swap(num[i],num[n])
				A=self.permute1(num,n+1,A)
				self.swap(num[i],num[n])
		return A

    # @param num, a list of integer
    # @return a list of lists of integers
	def permute(self, num):
		result = self.permute1(num,0,[])
		return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.permute([1,1,2]),[[1,1,2],[1,2,1],[2,1,1]])


if __name__ == '__main__':
    main()