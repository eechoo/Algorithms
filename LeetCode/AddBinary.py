#!/usr/bin/python
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
    	if(a == ''):
    		return b
    	if(b == ''):
    		return a
    	la=len(a)
    	lb=len(b)
    	if(la > lb):
    		max=la
    	else:
    		max=lb
    	flag=0
    	result=''
    	for i in range(1,max+1):
    		if(la < i ):
    			sum=int(b[-i])+flag
    		elif(lb < i):
    			sum=int(a[-i])+flag
    		else:
    			sum=int(a[-i])+int(b[-i])+flag
    		if(sum > 1):
    			flag=1
    			sum%=2
    		else:
    			flag=0
    		result=str(sum)+result
    	if(flag == 1):
    		result='1'+result
    	return result



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.addBinary('1010','1011'),100)


if __name__ == '__main__':
    main()