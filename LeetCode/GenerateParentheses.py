#!/usr/bin/python
class Solution:
	# @param an integer
    # @return a list of string
    def generate(self,left,right,ListA,StringA):
    	if(left==0  and right == 0):
    		ListA.append(StringA)
    		return ListA
    	if(left > 0):
    		ListA=self.generate(left-1,right,ListA,StringA+'(')
    	if(left < right and right >0):
    		ListA=self.generate(left,right-1,ListA,StringA+')')
    	return ListA

    def generateParenthesis(self, n):
    	ListA=[]
    	if(n==0):
    		return ListA
    	StringA=''
    	A=self.generate(n,n,ListA,StringA)
    	return A

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.generateParenthesis(1),['()'])
    test(ins.generateParenthesis(2),['(())','()()'])
    test(ins.generateParenthesis(3),['((()))','(()())','(())()','()(())','()()()'])


if __name__ == '__main__':
    main()