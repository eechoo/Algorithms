#!/usr/bin/python
class Solution:
    # @return a list of integers
    def grayCode(self, n):
    	A=[]
    	for i in range(0,1<<n):
    		A.append((i>>1)^i)
    	return A


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.grayCode(2),[0,1,3,2])
    test(ins.grayCode(1),[0,1])
    test(ins.grayCode(3),[0, 1, 3, 2, 6, 7, 5, 4])


if __name__ == '__main__':
    main()