#!/usr/bin/python
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''
class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
    	DP=[9999 for i in range(len(A))]
    	DP[0]=0
    	for i in range(1,len(A)):
    		for j in range(i):
    			if(j +A[j] >=i and DP[j]+1 < DP[i]):
    				DP[i]=DP[j]+1
    				break
    	return DP[-1]

    def jump1(self,A):
    	ret = 0
        last = 0
        curr = 0
        for i in range(len(A)):
            if i > last:
                # if not last one and can't go further
                if (curr == last) and (last < len(A)-1):
                    return -1   # never reach the last one
                last = curr
                ret += 1
            curr = max(curr, i+A[i])
        return ret

        

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.jump1([2,3,1,1,4]),2)


if __name__ == '__main__':
    main()