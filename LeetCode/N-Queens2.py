#!/usr/bin/python
#Follow up for N-Queens problem.

#Now, instead outputting board configurations, return the total number of distinct solutions.

class Solution:
    # @return an integer
    def totalNQueens(self, n):


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
    	