#!/usr/bin/python
class Remove(object): 
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        if(A == []):
            return 0
        A=[i for i in A if (i != elem)]
        print A
        return len(A)

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Remove()
    test(ins.removeElement([1,2],1),1)
    test(ins.removeElement([3,3],3),0)
    test(ins.removeElement([4,5],4),1)

if __name__ == '__main__':
    main()