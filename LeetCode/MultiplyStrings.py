#!/usr/bin/python
'''
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
'''

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
    	if(num1=='' or num1=='0'):
    		return num2
    	if(num2=='' or num2=='0'):
    		return num1
    	result=''
    	flag=0
    	for i in range(-1,-1*max(len(num1),len(num2))-1,-1):
    		if(i*(-1)-1<len(num1)):
    			if(i*(-1)-1 < len(num2)):
    				result=str((int(num1[i])+int(num2[i])+flag)%10)+result
    				flag=(int(num1[i])+int(num2[i])+flag)/10
    			else:
    				result=num1[:i]+str(int(num1[i])+flag)+result
    		else:
    			result=num2[:i]+str(int(num2[i])+flag)+result
    	return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.multiply('123','1'),'124')
    test(ins.multiply('0','0'),'0')
    test(ins.multiply('123456789','123456789'),'123456789')


if __name__ == '__main__':
    main()