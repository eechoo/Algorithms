#!/usr/bin/python
#Given an array of integers, every element appears three times except for one. Find that single one.

# Note:
#Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
    	one=0
    	two=0
    	three=0
    	for i in A:
    		two |=(i & one)
    		one ^=i
    		three=~(two & one)
    		two &=three
    		one &=three
    	return one

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.singleNumber([5,6,5,6,7,5,6]),7)



if __name__ == '__main__':
    main()