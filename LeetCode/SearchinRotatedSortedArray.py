#!/usr/bin/python
#Suppose a sorted array is rotated at some pivot unknown to you beforehand.

#(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

#You are given a target value to search. If found in the array return its index, otherwise return -1.

#You may assume no duplicate exists in the array.

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        if(A == []):
            return -1
        left=0
        right=len(A)-1
        while(left <= right):
            mid=(right-left)/2+left
            if(target == A[mid]):
                return mid
            if(A[left] <= A[mid]):
                if(target <= A[mid] and target >= A[left]):
                    right=mid-1
                else:
                    left=mid+1
            else:
                if(target <= A[right] and target >=A[mid]):
                    left=mid+1
                else:
                    right=mid-1
        return -1

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.search([1,3,5],1),0)
    test(ins.search([4,5,6,7,0,1,2],3),-1)
    test(ins.search([4,5,6,7,0,1,2],5),1)


if __name__ == '__main__':
    main()