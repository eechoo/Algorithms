#!/usr/bin/python
#Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

#For example,
#Given n = 3,

#You should return the following matrix:
#[
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
#]

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
    	if(n == 0):
    		return [[]]
    	grid=[[0 for col in range(n)] for row in range(n)]
    	num=0
    	for layer in range((n+1)/2):
    		for i in range(layer,n-layer):
    			num+=1
    			grid[layer][i]=num
    		for i in range(layer+1,n-layer):
    			num+=1
    			grid[i][n-layer-1]=num
    		for i in range(n-layer-2,layer-1,-1):
    			num+=1
    			grid[n-layer-1][i]=num
    		for i in range(n-layer-2,layer,-1):
    			num+=1
    			grid[i][layer]=num
    	return grid

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.generateMatrix(1),[[1]])
    test(ins.generateMatrix(2),[[1,2],[4,3]])
    test(ins.generateMatrix(3),[[1,2,3],[8,9,4],[7,6,5]])
    test(ins.generateMatrix(4),[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]])    


if __name__ == '__main__':
    main()