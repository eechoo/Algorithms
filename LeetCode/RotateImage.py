#!/usr/bin/python
#You are given an n x n 2D matrix representing an image.

#Rotate the image by 90 degrees (clockwise).

#Follow up:
#Could you do this in-place?

#一次旋转一个点，转一圈，涉及到4个点，仅需循环1/4矩阵
class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
    	if(matrix == None):
    		return []
    	n=len(matrix)
    	for i in range(n/2):
    		for j in range(i,n-i-1):
    			tmp=matrix[i][j]
    			matrix[i][j]=matrix[n-j-1][i]
    			matrix[n-j-1][i]=matrix[n-i-1][n-j-1]
    			matrix[n-i-1][n-j-1]=matrix[j][n-i-1]
    			matrix[j][n-i-1]=tmp
    	return matrix	
    	

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.rotate([[0]]),[[0]])
    test(ins.rotate([[1,2],[3,4]]),[[3,1],[4,2]])



if __name__ == '__main__':
    main()
