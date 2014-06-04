#!/usr/bin/python
class Search(object): 
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if len(A)==0:
            return 0
        for i in range(0,len(A)):
            if(target == A[i] or target < A[i]):
                return i
        return len(A)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Search()
    test(ins.searchInsert([1,3,5,6], 5),2)
    test(ins.searchInsert([1,3,5,6], 2),1)
    test(ins.searchInsert([1,3,5,6], 7),4)
    test(ins.searchInsert([1,3,5,6], 0),0)

if __name__ == '__main__':
    main()