#!/use/bin/python
#Given an index k, return the kth row of the Pascal's triangle.

#For example, given k = 3,
#Return [1,3,3,1].

#Note:
#Could you optimize your algorithm to use only O(k) extra space?
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
    	A,num1,num2,num3=[],1,1,1
    	for i in range(1,rowIndex+1):
    		num1*=i
    	for i in range(rowIndex+1):
    		for j in range(1,i+1):
    			num2*=j
    		for j in range(1,rowIndex+1-i):
    			num3*=j
    		A.append(num1/(num2*num3))
    		num2,num3=1,1
    	return A

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.getRow(1),[1,1])
    test(ins.getRow(2),[1,2,1])
    test(ins.getRow(3),[1,3,3,1])


if __name__ == '__main__':
    main()