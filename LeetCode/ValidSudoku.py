#!/usr/bin/python
'''
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
    	flag=[0 for i in range(9)]
    	for i in range(9):
    		for j in range(9):
    			if(board[i][j] != '.'):
    				flag[int(board[i][j])-1]+=1
    		for j in range(9):
    			if(flag[j] >1 ):
    				return False
    			else:
    				flag[j]=0
    	for i in range(9):
    		for j in range(9):
    			if(board[j][i]!= '.'):
    				flag[int(board[j][i])-1]+=1
    		for j in range(9):
    			if(flag[j] >1 ):
    				return False
    			else:
    				flag[j]=0
    	for i in range(9/3):
    		for j in range(9/3):
    			for ii in range(3):
    				for jj in range(3):
    					if(board[3*i+ii][3*j+jj]!='.'):
    						flag[int(board[3*i+ii][3*j+jj])-1]+=1
    			for tmp in range(9):
    				if(flag[tmp] >1 ):
    					return False
    				else:
    					flag[tmp]=0
    	return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    A=[".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    A=["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
    A=["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."]
    test(ins.isValidSudoku(A),False)



if __name__ == '__main__':
    main()