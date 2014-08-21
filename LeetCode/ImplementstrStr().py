#!/usr/bin/python
'''Implement strStr().

Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.'''

class Solution:
	# @param haystack, a string
	# @param needle, a string
	# @return a string or None
	def strStr(self, haystack, needle):
		if (needle == ''):
			return haystack
		if (haystack == ''):
			return None
		for i in xrange(len(haystack)-len(needle)+1):
			if(haystack[i:i+len(needle)] == needle):
				return haystack[i:]
		return None


def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	ins=Solution()
	test(ins.strStr('abc','bc'),2)


if __name__ == '__main__':
    main()