#!/usr/bin/python
'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3   1,3,2
3,2,1   1,2,3
1,1,5   1,5,1
'''
class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        if(num == [] or len(num)==1):
        	return num
        flag=False
        for i in range(len(num)-1):
        	if(num[i] < num[i+1]):
        		flag=True
        		first=i
        		second=i+1
        	if(flag == True and num[i+1]-num[first]<num[second]-num[first]):
        		second=i+1
        if(flag == True):
        	tmp=num[first]
        	num[first]=num[second]
        	num[second]=tmp
        else:
        	num.reverse()
        return num


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.nextPermutation([1,2,3]),['()'])
    test(ins.nextPermutation([3,2,1]),['()'])
    test(ins.nextPermutation([1,1,5]),['()'])


if __name__ == '__main__':
    main()