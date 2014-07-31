#!/usr/bin/python
'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        if(A == []):
            return [-1,-1]
        begin=-1
        end=-1
        #find begin
        left=0
        right=len(A)-1
        while(left <= right):
            mid=(right-left)/2+left
            if(A[mid] == target):
                begin=mid
                right=mid-1
            elif(A[mid] > target):
                right=mid-1
            elif(A[mid] < target):
                left=mid+1
        #find end
        left=0
        right=len(A)-1
        while(left <= right):
            mid=(right-left)/2+left
            if(A[mid] == target):
                end=mid
                left=mid+1
            elif(A[mid] > target):
                right=mid-1
            elif(A[mid] < target):
                left=mid+1
        return [begin,end]

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.searchRange([5, 7, 7, 8, 8, 10],8),[3,4])
    test(ins.searchRange([5, 7, 7, 8, 8, 10],5),[0,0])
    test(ins.searchRange([5, 7, 7, 8, 8, 10],11),[-1,-1])


if __name__ == '__main__':
    main()
