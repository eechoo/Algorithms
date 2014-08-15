#!/usr/bin/python
'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]
'''

class Solution:
	def IsPalindrome(self,s):
		for i in range(len(s)/2+1):
			if(s[i]!=s[-(i+1)]):
				return False
		return True

	def partition2(self,s,result,cur):
		if(s == ''):
			result.append(cur[:])
			return result
		for i in range(len(s)):
			if( self.IsPalindrome(s[:i+1]) == True):
				cur.append(s[:i+1])
				self.partition2(s[i+1:],result,cur)
				cur.pop()
		return result

	# @param s, a string
	# @return a list of lists of string
	def partition(self, s):
		if(s == ''):
			return []
		result=[]
		cur=[]
		result=self.partition2(s,result,cur)
		return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    s='ltsqjodzeriqdtyewsrpfscozbyrpidadvsmlylqrviuqiynbscgmhulkvdzdicgdwvquigoepiwxjlydogpxdahyfhdnljshgjeprsvgctgnfgqtnfsqizonirdtcvblehcwbzedsmrxtjsipkyxk'
    test(ins.partition(s),['()'])


if __name__ == '__main__':
    main()