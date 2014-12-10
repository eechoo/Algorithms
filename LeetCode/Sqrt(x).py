#!/usr/bin/python
'''
Implement int sqrt(int x).

Compute and return the square root of x.
'''

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if(x <= 0):
            return 0
        right=x/2
        left=1
        while(right - left > 1):
            mid=(right+left)/2
            sum=mid*mid
            if(sum == x):
                return mid
            elif(sum > x):
                right=mid
            else:
                left=mid
        if(right*right <= x and right>left):
            return right
        else:
            return left

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.sqrt(1),1)
    test(ins.sqrt(5),2)
    test(ins.sqrt(6),2)


if __name__ == '__main__':
    main()