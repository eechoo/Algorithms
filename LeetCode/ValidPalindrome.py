#!/usr/bin/python
'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
'''

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if(s == ''):
        	return True
        i=0
        j=len(s)-1
        while(i<j):
        	if(s[i].isalnum()):
        		if(s[j].isalnum()):
        			if( s[i].upper()== s[j].upper()):
        				i+=1
        				j-=1
        			else:
        				return False
        		else:
        			j-=1
        	else:
        		i+=1
        return True

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.isPalindrome("A man, a plan, a canal: Panama"),True)
    test(ins.isPalindrome("race a car"),False)


if __name__ == '__main__':
    main()