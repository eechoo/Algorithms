#!/usr/bin/python
#Follow up for N-Queens problem.

#Now, instead outputting board configurations, return the total number of distinct solutions.
'''
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
'''
class Solution:
    def totalNQueens2(self,n,m,result,cur):
        if(m==n):
            result.append([])
            for i in range(len(cur)):
                result[-1].append(''.join(cur[i]))
            return result
        row=['.' for i in range(n)]
        for i in range(n):
            flag=True
            if(cur != []):
                for k in range(len(cur)):
                    for j in range(n):
                        if(cur[k][j] == 'Q' ):
                            if(j==i or m-k == i-j or m-k == j-i):
                                flag=False
                                break
                            else:
                                break
                    if(flag == False):
                        break
            if(flag == True):
                row[i]='Q'
                cur.append(row[:])
                self.totalNQueens2(n,m+1,result,cur)
                cur.pop()
                row[i]='.'
        return result

    # @return an integer
    def totalNQueens(self, n):
        if(n==0):
            return []
        result=[]
        return self.totalNQueens2(n,0,result,[])

    def totalNQueensNum(self, n):
        if(n==0):
            return 0
        result=self.totalNQueens2(n,0,[],[])
        return len(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.totalNQueens(4),['()'])


if __name__ == '__main__':
    main()
    	