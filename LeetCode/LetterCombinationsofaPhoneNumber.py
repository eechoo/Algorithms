#!/usr/bin/python
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution:
    def letterCombinations2(self, digits,result,string):
    	if(digits == ''):
    		result.append(string)
    		return
    	map={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    	tmp=map[digits[0]]
    	for i in range(len(tmp)):
    		string+=tmp[i]
    		self.letterCombinations2(digits[1:],result,string)
    		string=string[:-1]
    	

    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
    	if(digits == []):
    		return []
    	result=[]
    	self.letterCombinations2(digits,result,"")
    	return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.letterCombinations('23'),['()'])


if __name__ == '__main__':
    main()