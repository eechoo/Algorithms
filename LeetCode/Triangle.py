#!/usr/bin/python
'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
    	if(triangle==[] or triangle==[[]]):
    		return 0
    	row=[0 for i in range(len(triangle))]
    	for i in range(len(triangle)):
    		for j in range(len(triangle[i])-1,-1,-1):
    			if(i==0):
    				row[j]=triangle[i][j]
    			elif(j==0):
    				row[j]=triangle[i][j]+row[0]
    			elif(j==len(triangle[i])-1):
    				row[j]=triangle[i][j]+row[j-1]
    			elif(row[j] < row[j-1]):
    				row[j]=triangle[i][j]+row[j]
    			else:
    				row[j]=triangle[i][j]+row[j-1]
    	least=row[0]
    	for i in range(1,len(row)):
    		if(row[i] < least):
    			least=row[i]
    	return least

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    A=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
    test(ins.minimumTotal(A),11)


if __name__ == '__main__':
    main()