#!/usr/bin/python
'''
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if(s == ''):
            return 0
        dict={}
        longest=0
        cur=0
        for i in range(len(s)):
            if(dict.has_key(s[i]) and i-cur <= dict[s[i]]):
                    cur=i-dict[s[i]]
            else:
                cur+=1
                if(longest < cur):
                    longest=cur
            dict[s[i]]=i
        return longest
                       

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    s='mowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco'
#    test(ins.lengthOfLongestSubstring('abcabcbb'),3)
#    test(ins.lengthOfLongestSubstring('bbbbbbb'),1)
    test(ins.lengthOfLongestSubstring(s),12)


if __name__ == '__main__':
    main()