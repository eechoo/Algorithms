#!/usr/bin/python
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

#Note: You can only move either down or right at any point in time.
class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
    	m=len(grid)
    	if(m == 0):
    		return 0
    	n=len(grid[0])
    	if(n == 0):
    		return 0
    	minPathGrid=[[0 for col in range(n)] for row in range(m)]
    	for i in range(m):
    		for j in range(n):
    			if(i == 0 and j == 0):
    				minPathGrid[i][j]=grid[i][j]
    			elif(i==0):
    				minPathGrid[i][j]=grid[i][j]+minPathGrid[i][j-1]
    			elif(j==0):
    				minPathGrid[i][j]=grid[i][j]+minPathGrid[i-1][j]
    			else:
    				if(minPathGrid[i-1][j] > minPathGrid[i][j-1]):
    					minPathGrid[i][j]=minPathGrid[i][j-1]+grid[i][j]
    				else:
    					minPathGrid[i][j]=minPathGrid[i-1][j]+grid[i][j]
    	return minPathGrid[m-1][n-1]

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.minPathSum([[1],[2]]),3)
    test(ins.minPathSum([[1,2,3],[4,5,6]]),12)


if __name__ == '__main__':
    main()