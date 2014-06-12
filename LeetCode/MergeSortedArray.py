#!/usr/bin/python
#Given two sorted integer arrays A and B, merge B into A as one sorted array.

#Note:
#You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
    	i=0
    	j=0
    	x=0
    	while(j<n):
    		while(i<m+x):
    			print "i=%d,j=%d" % (i,j)
    			print "%d,%d" %(A[i],B[j])
    			if(A[i]>B[j]):
    				A.insert(i,B[j])
    				x+=1
    				print "insert %d intoA[%d]" %(B[j],i)
    				break
    			i+=1
    		j+=1
    	if(x  < n):
    		for x in range(x,n):
				A.insert(m+x,B[x])
    	return A

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.merge([2,4],2,[1,3,5,6],4),[1,2,3,4,5,6])


if __name__ == '__main__':
    main()