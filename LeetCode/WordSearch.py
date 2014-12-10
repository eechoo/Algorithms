#!/usr/bin/python
'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution:
	def exist1(self,board,word,path,pos):
		if(len(word)==0):
			return True
		i,j=pos
		if(i>0 and board[i-1][j]==word[0] and (i-1,j) not in path):
			newpos=(i-1,j)
			path.add(newpos)
			if(self.exist1(board,word[1:],path,newpos)):
				return True
			path.remove(newpos)
		if(j>0 and board[i][j-1]==word[0] and (i,j-1) not in path):
			newpos=(i,j-1)
			path.add(newpos)
			if(self.exist1(board,word[1:],path,newpos)):
				return True
			path.remove(newpos)
		if(j+2<=len(board[i]) and board[i][j+1]==word[0] and (i,j+1) not in path):
			newpos=(i,j+1)
			path.add(newpos)
			if(self.exist1(board,word[1:],path,newpos)):
				return True
			path.remove(newpos)
		if(i+2<=len(board) and board[i+1][j]==word[0] and (i+1,j) not in path):
			newpos=(i+1,j)
			path.add(newpos)
			if(self.exist1(board,word[1:],path,newpos)):
				return True
			path.remove(newpos)
		return False

	# @param board, a list of lists of 1 length string
	# @param word, a string
	# @return a boolean
	def exist(self, board, word):
		if(len(board) == 0 or len(word)==0):
			return False
		path=set([])
		for i in range(len(board)):
			for j in range(len(board[i])):
				if(board[i][j]==word[0]):
					print board[i][j]
					pos=(i,j)
					path.add(pos)
					if(self.exist1(board,word[1:],path,pos)):
						return True
					path.remove(pos)
		return False


def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	ins=Solution()
	board =["ABCE","SFCS","ADEE"]
	test(ins.exist(board,"ABCCED"),True)
	test(ins.exist(board,"SEE"),True)
	test(ins.exist(board,"ABCB"),False)


if __name__ == '__main__':
	main()