#!/usr/bin/python
'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example, 
Given s = "Hello World",
return 5.
'''
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        W=s.split()
        if(len(W)==0):
            return 0
    	return len(W[-1])

    def lengthOfLastWord1(self,s):
    	if(s == '' ):
    		return 0
    	space=True
    	Wbegin=0
    	Wend=0
    	for i in range(len(s)):
    		if(s[i].isalpha() and space==True):
    			Wbegin=i
    			space=False
    		elif(s[i] == ' ' and space == False):
    			Wend=i
    			space=True
    		if(s[i].isalpha() and i == len(s)-1):
    			Wend=i+1
    		print Wend
    		print Wbegin
    	return Wend-Wbegin

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.lengthOfLastWord1('  aa  ddd  '),2)


if __name__ == '__main__':
    main()