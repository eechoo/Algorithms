#!/usr/bin/python
#Follow up for "Remove Duplicates":
#What if duplicates are allowed at most twice?

#For example,
#Given sorted array A = [1,1,1,2,2,3],

#Your function should return length = 5, and A is now [1,1,2,2,3].

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if(A ==[] ):
            return 0
        num,flag=0,1
        for i in range(1,len(A)):
            if(A[i-1] != A[i] ):
                flag=1
                num+=1
                A[num]=A[i]
            elif(flag==1):
                flag=2
                num+=1
                A[num]=A[i]
            else:
                flag+=1
        print A
        return num+1

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.removeDuplicates1([1,1,1,2,2,3]),5)
    test(ins.removeDuplicates1([1,1]),2)


if __name__ == '__main__':
    main()