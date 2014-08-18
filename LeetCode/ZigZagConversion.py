#!/usr/bin/python
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution:
    # @return a string
    def convert(self, s, nRows):
    	if(s=='' or nRows<=1):
    		return s
    	conver=['' for i in range(nRows)]
    	for i in range(len(s)):
    		num=i%(2*nRows-2)
    		if(num < nRows-1):
    			conver[num]+=s[i]
    		else:
    			conver[2*nRows-2-num]+=s[i]
    	s=''
    	for j in range(nRows):
    		s+=conver[j]
    	return s
    	
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.convert("PAYPALISHIRING", 3),"PAHNAPLSIIGYIR")
    test(ins.convert("AB", 2),"AB")



if __name__ == '__main__':
    main()