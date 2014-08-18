#!/usr/bin/python
'''
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.
'''

class Solution:
    # @return an integer
    def numDistinct(self, S, T):
    	DP=[0 for i in range(len(T))]
    	for i in range(len(S)):
    		for j in range(len(T)-1,-1,-1):
    			if(S[i] == T[j]):
    				if(j>0):
    					DP[j]+=DP[j-1]
    				else:
    					DP[j]+=1
    	return DP[-1]



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.numDistinct("rabbbit","rabbit"),2)
    test(ins.numDistinct("ccc","c"),2)


if __name__ == '__main__':
    main()