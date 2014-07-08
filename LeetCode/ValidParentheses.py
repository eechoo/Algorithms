#!/usr/bin/python
'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        if(s == ''):
    		return True
    	A=[]
    	for i in range(len(s)):
    		if(s[i] == '(' or s[i]== '[' or s[i] == '{'):
    			A.append(s[i])
    		if(s[i] == ')' or s[i]==']' or s[i] =='}' ):
    			if(len(A)>0):
    			    tmp=A.pop()
    			    if(tmp == '(' and s[i]!=')'):
    				    return False
    			    elif(tmp == '[' and s[i]!=']'):
    				    return False
    			    elif(tmp == '{' and s[i]!='}'):
    				    return False
    			else:
    				return False
    		print A
    	if(len(A)):
    		return False
    	return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.isValid('['),True)
    test(ins.isValid('[(]'),False)


if __name__ == '__main__':
    main()