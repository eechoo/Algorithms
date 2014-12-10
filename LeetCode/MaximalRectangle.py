#!/usr/bin/python
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
'''

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if(len(matrix)==0):
            return 0
        dp=[[0 for i in matrix[0]] for j in matrix]
        dp[0]=matrix[0]
        for i in range(1,len(matrix)):
            for j in range(matrix[0]):
                if(matrix[i][j] == 1):
                    dp[i][j]=dp[i-1][j]+1
        result=0
        for i in range(len(dp)):
            higth=0
            width=0
            for j in range(len(dp[0])):
                if(dp[i][j]>0):
                    higth=min(dp[i][j],dp[i-1][j-1])
                    width+=1




def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.maxProfit([1,2,3]),2)
    test(ins.maxProfit([3,2,1]),0)
    test(ins.maxProfit([1,4,2]),3)


if __name__ == '__main__':
    main()