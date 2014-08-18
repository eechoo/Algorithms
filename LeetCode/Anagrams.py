#!/usr/bin/python
'''
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
'''
class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
    	if(strs == []):
    		return []
    	anag={}
    	result=[]
    	for i in range(len(strs)):
    		s=list(strs[i])
    		s.sort()
    		s= ''.join(s)
    		if( anag.has_key(s) ):
    			if(anag[s] != -1):
    				result.append(strs[anag[s]])
    				anag[s]=-1
    			result.append(strs[i])
    		else:
    			anag[s]=i
    	return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.anagrams(["tea","and","ate","eat","den"]),["tea","ate","eat"])


if __name__ == '__main__':
    main()