#!/usr/bin/python
'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
    	if(x < 0):
    		return False
    	i=1
    	while(x/i>=10):
    		i*=10
    	while(x != 0):
    		if(x%10 != x/i):
    			return False
    		else:
    			x%=i
    			x/=10
    			i/=100
    	return True        

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.isPalindrome(10000021),False)
    test(ins.isPalindrome(9999),True)
    test(ins.isPalindrome(-3),False)


if __name__ == '__main__':
    main()