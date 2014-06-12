#!/usr/bin/python
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
    	index0=0
    	index1=0
    	index2=len(A)-1
    	i=0
    	while  i < index2+1:
    		if(A[i] == 1):
    			index1+=1
    			i+=1
    		elif(A[i]==2):
    			tmp=A[i]
    			A[i]=A[index2]
    			A[index2]=tmp
    			index2-=1
    		else:
    			if(i != index0):
    				tmp=A[i]
    				A[i]=A[index0]
    				A[index0]=tmp
    			index0+=1
    			index1+=1
    			i+=1
    	return A


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.sortColors([0,2,1,2,0,1]),[0,0,1,1,2,2])
    test(ins.sortColors([2,1]),[1,2])
    test(ins.sortColors([2,1,0]),[0, 1, 2])


if __name__ == '__main__':
    main()