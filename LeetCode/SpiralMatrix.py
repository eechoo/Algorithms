#!/usr/bin/python
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of integers
	def spiralOrder(self, matrix):
		result=[]
		if(len(matrix)==0 or len(matrix[0])==0):
			return result
		m=len(matrix)
		n=len(matrix[0])
		for layor in range(min(m,n)/2+min(m,n)%2):
			for col in range(layor,n-layor):
				result.append(matrix[layor][col])
			for row in range(layor+1,m-layor-1):
				result.append(matrix[row][n-layor-1])
			if(m-layor*2>1):
				for col in range(n-layor-1,layor-1,-1):
					result.append(matrix[m-1-layor][col])
			if(n>layor+1):
				for row in range(m-2-layor,layor,-1):
					result.append(matrix[row][layor])
		return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    matrix1=[[ 1,2,3],[4,5,6], [7,8,9]]
    matrix2=[[1,2,3]]
    matrix3=[[1],[3],[2]]
    matrix4=[[4]]
    test(ins.spiralOrder(matrix4),[1,2,3,6,9,8,7,4,5])


if __name__ == '__main__':
    main()