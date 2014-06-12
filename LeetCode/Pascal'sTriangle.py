#!/usr/bin/python
class Solution:
# @return a list of lists of integers
    def generate(self, numRows):
    	if(numRows == 0):
    		return []
    	A=[[1]]
    	for i in range(1,numRows):
    		A.append([])
    		for j in range(i+1):
    			if(j==0 or j==i):
    				A[i].append(1)
    			else:
    				A[i].append(A[i-1][j]+A[i-1][j-1])
    	return A


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.generate(2),[[1],[1,1]])
    test(ins.generate(3),[[1],[1,1],[1,2,1]])


if __name__ == '__main__':
    main()