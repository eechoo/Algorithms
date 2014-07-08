#!/usr/bin/python

'''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''

class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
    	m=len(obstacleGrid)
    	n=len(obstacleGrid[0])
    	A=[[0 for i in range(n)] for j in range(m) ]
    	for i in range(m-1,-1,-1):
    		for j in range(n-1,-1,-1):
    			if(i == m-1 ):
    				if(j+1 < n and A[i][j+1]==0):
    					A[i][j]=0
    				else:
    					A[i][j]=1
    			elif(j==n-1):
    				if(i+1 < m and A[i+1][j]==0):
    					A[i][j]=0
    				else:
    					A[i][j]=1
    			else:
    				A[i][j]=A[i+1][j]+A[i][j+1]
    			if(obstacleGrid[i][j] == 1):
    				A[i][j]=0
    	return A[0][0]

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.uniquePathsWithObstacles([[1]]),0)
    test(ins.uniquePathsWithObstacles([[0]]),1)
    test(ins.uniquePathsWithObstacles([[0,1]]),0)


if __name__ == '__main__':
    main()