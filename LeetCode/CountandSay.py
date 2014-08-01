#!/usr/bin/python
'''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
'''
class Solution:
    # @return a string
    def countAndSay(self, n):
    	if(n==0):
    		return ''
    	result='1'
    	for i in range(n-1):
    		j=0
    		tmp=''
    		for j in range(len(result)):
    			if(j==0):
    				num=1
    			elif(result[j] == result[j-1]):
    				num+=1
    			else:
    				tmp+=str(num)+result[j-1]
    				num=1
    		result=tmp+str(num)+result[j]
    		print result
    	return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.countAndSay(5),'11')



if __name__ == '__main__':
    main()