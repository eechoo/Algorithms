#!/usr/bin/python

#Given a non-negative number represented as an array of digits, plus one to the number.

#The digits are stored such that the most significant digit is at the head of the list.
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
    	if(digits == []):
    		return [1]
    	flag=0
    	for i in range(len(digits)-1,-1,-1):
    		if(digits[i]+1 == 10):
    			digits[i] = 0
    			if(i==0):
    				digits.insert(0,1)
    		else:
    			digits[i]=digits[i]+1
    			break
    	return digits



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.plusOne([1]),[2])
    test(ins.plusOne([1,2,3]),[1,2,4])
    test(ins.plusOne([9,9,9]),[1,0,0,0])


if __name__ == '__main__':
    main()
