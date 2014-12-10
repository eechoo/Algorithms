#!/usr/bin/python
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
class Solution1:
	#check if board[i][j] is valid
	def checkValid(self,i,j,board):
		for row in range(9):
			if(row!=i and board[row][j]==board[i][j]):
				return False
		for col in range(9):
			if(col!=j and board[i][col]==board[i][j]):
				return False
		for row in range(3):
			for col in range(3):
				if((i/3*3+row !=i or j/3*3+col!=j) and board[i/3*3+row][j/3*3+col]==board[i][j] ):
					return False
		return True

	# @param board, a 9x9 2D array
	# Solve the Sudoku by modifying the input board in-place.
	# Do not return any value.
	def solveSudoku(self, board):
		for i in range(len(board)):
			for j in range(len(board)):
				if(board[i][j]=='.'):
					for k in range(1,10):
						board[i]=board[i][:j]+str(k)+board[i][j+1:]
						if(self.checkValid(i,j,board) and self.solveSudoku(board)):
							return True
					board[i]=board[i][:j]+'.'+board[i][j+1:]
					return False
		return True

class Solution2:
	def FindValid(self,i,j,board):
		valid=set(['1','2','3','4','5','6','7','8','9'])
		invalid=set([])
		for row in range(9):
			if(board[row][j] in valid ):
				invalid.add(board[row][j])
		for col in range(9):
			if(board[i][col] in valid):
				invalid.add(board[i][col])
		for row in range(3):
			for col in range(3):
				if( board[i/3*3+row][j/3*3+col]  in valid ):
					invalid.add(board[i/3*3+row][j/3*3+col])
		return valid-invalid

	# @param board, a 9x9 2D array
	# Solve the Sudoku by modifying the input board in-place.
	# Do not return any value.
	def solveSudoku(self, board):
		for i in range(len(board)):
			for j in range(len(board)):
				if(board[i][j]=='.'):
					valid=self.FindValid(i,j,board)
					if(len(valid)==0):
						return False
					for k in valid:
						board[i]=board[i][:j]+k+board[i][j+1:]
						if(self.solveSudoku(board)):
							return True
					board[i]=board[i][:j]+'.'+board[i][j+1:]
					return False
		return True

class Solution:
	def dfs(self,board,row,col,block):
		l=set(['1','2','3','4','5','6','7','8','9'])
		for i in range(9):
			for j in range(9):
				if(board[i][j]=='.'):
					valid=l-row[i]-col[j]-block[i/3*3+j/3]
					for k in valid:
						board[i]=board[i][:j]+k+board[i][j+1:]
						row[i].add(k)
						col[j].add(k)
						block[i/3*3+j/3].add(k)
						if(self.dfs(board,row,col,block)):
							return True
						row[i].discard(k)
						col[j].discard(k)
						block[i/3*3+j/3].discard(k)
						board[i]=board[i][:j]+'.'+board[i][j+1:]
#					print row[i]
#					print col[j]
#					print block[i/3*3+j/3]
#					print board
#					print valid
					return False
		return True

	# @param board, a 9x9 2D array
	# Solve the Sudoku by modifying the input board in-place.
	# Do not return any value.
	def solveSudoku(self, board):
		row=[]
		col=[]
		block=[set([]) for i in range(9)]
		for i in range(9):
			row.append(set([]))
			for j in range(9):
				if(board[i][j]=='.'):
					continue
				row[i].add(board[i][j])
		for j in range(9):
			col.append(set([]))
			for i in range(9):
				if(board[i][j]=='.'):
					continue
				col[j].add(board[i][j])
		for i in range(3):
			for j in range(3):
				for m in range(3):
					for n in range(3):
						if(board[i*3+m][j*3+n]=='.'):
							continue
						block[i*3+j].add(board[i*3+m][j*3+n])
		self.dfs(board,row,col,block)
		return board

def test(got, expected):
	if got == expected:
 		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	ins=Solution()
	board =[".....7..9",".4..812..","...9...1.","..53...72","293....5.",".....53..","8...23...","7...5..4.","531.7...."]
	result=['312547869','947681235','658932714','185364972','293718456','476295381','864123597','729856143','531479628']
	board1=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
	result1=["519748632","783652419","426139875","357986241","264317598","198524367","975863124","832491756","641275983"]
	test(ins.solveSudoku(board1),result1)


if __name__ == '__main__':
    main()