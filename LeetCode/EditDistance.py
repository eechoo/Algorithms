#!/usr/bin/python
'''
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

class Solution:	
    # @return an integer
    def minDistance(self, word1, word2):
    	if(word1==''):
    		return len(word2)
    	elif(word2==''):
    		return len(word1)
    	DP = []
    	for i in range(len(word1)+1):
    		DP.append([0 for j in range(len(word2)+1)])
    		for j in range(len(word2)+1):
    			if( i==0):
    				DP[i][j] = j
    			elif(j==0):
    				DP[i][j] = i
    			else:
    				a=DP[i-1][j]+1
    				b=DP[i][j-1]+1
    				if(word1[i-1] == word2[j-1]):
    					c=DP[i-1][j-1]
    				else:
    					c=DP[i-1][j-1]+1
    				if(a<b and a<c):
    					DP[i][j]=a
    				elif(b<a and b<c):
    					DP[i][j]=b
    				else:
    					DP[i][j]=c
    	return DP[-1][-1]

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	ins=Solution()
	test(ins.minDistance("zoologicoarchaeologist", "zoogeologist"),1)
	test(ins.minDistance("ab", "a"),1)
if __name__ == '__main__':
    main()