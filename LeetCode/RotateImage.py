#!/usr/bin/python
#You are given an n x n 2D matrix representing an image.

#Rotate the image by 90 degrees (clockwise).

#Follow up:
#Could you do this in-place?

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
    	if(matrix == None):
    		return []
    	n=len(matrix)
    	for i in range(n):
    		hang=matrix[i]
    		for j in range(n):
    			matrix[i][j]=matrix[j][n-1-i]




def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.generateParenthesis(1),['()'])
    test(ins.generateParenthesis(2),['(())','()()'])
    test(ins.generateParenthesis(3),['((()))','(()())','(())()','()(())','()()()'])


if __name__ == '__main__':
    main()
