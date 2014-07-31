#!/usr/bin/python
'''
greedy alg
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        if(A == []):
            return True
        step=1
        for i in range(len(A)-1):
            step-=1
            if(A[i] > step):
                step=A[i]
            if(step <= 0):
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
    test(ins.canJump([2,3,1,1,0]),True)



if __name__ == '__main__':
    main()