#!/usr/bin/python
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

#How many possible unique paths are there?

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
    	if(m == 1 or n == 1):
    		return 1
    	else:
    		return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)

#A[i][j]=A[i+1][j]+A[i][j+1]
    def uniquePaths2(self,m,n):
    	if(m==1 or n==1):
    		return 1
    	count=0
    	A=[[0]*n ]*m
    	for i in range(m-1,-1,-1):
    		for j in range(n-1,-1,-1):
    			if(i == m-1 or j == n-1):
    				A[i][j]=1
    			else:
    				A[i][j]=A[i+1][j]+A[i][j+1]
    	return A[0][0]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.uniquePaths2(23,12),193536720)
    test(ins.uniquePaths2(2,3),3)


if __name__ == '__main__':
    main()
