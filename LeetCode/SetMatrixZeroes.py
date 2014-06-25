#!/usr/bin/python
#Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

#click to show follow up.

#Follow up:
#Did you use extra space?
#A straight forward solution using O(mn) space is probably a bad idea.
#A simple improvement uses O(m + n) space, but still not the best solution.
#Could you devise a constant space solution?

class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
    	m=len(matrix)
    	n=len(matrix[0])
    	xi=-1
    	xj=-1
    	for i in range(m):
    		for j in range(n):
    			if(matrix[i][j] == 0):
    				if(i == 0):
    					xj=1
    				if(j==0):
    					xi=1
    				if(i!=0 and j!=0):
    					matrix[0][j]=0
    					matrix[i][0]=0
    	for i in range(1,m):
    		for j in range(1,n):
    			if(matrix[0][j] == 0 or matrix[i][0] == 0):
    				matrix[i][j]=0
    	if(xi==1):
    		for i in range(m):
    			matrix[i][0]=0
    	if(xj==1):
    		for i in range(n):
    			matrix[0][i]=0
    	return matrix
        

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.setZeroes([[1]]),[[1]])
    test(ins.setZeroes([[0,1],[2,2]]),[[0,0],[0,2]])


if __name__ == '__main__':
    main()
