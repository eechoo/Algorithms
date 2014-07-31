#!/usr/bin/python
#Write a function to find the longest common prefix string amongst an array of strings.

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
    	if(strs == []):
    		return ''
    	common=strs[0]
    	for i in range(1,len(strs)):
    		if(len(strs[i])<len(common)):
    			common=common[:len(strs[i])]
    		if(len(common) == 0):
    			return ''
    		for j in range(len(common)):
    			if(common[j] != strs[i][j]):
    				common=common[:j]
    				break
    	return common

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.longestCommonPrefix(['a','ab']),'a')
    test(ins.longestCommonPrefix(['ab','bc']),'')
    test(ins.longestCommonPrefix(['aa','a']),'a')


if __name__ == '__main__':
    main()