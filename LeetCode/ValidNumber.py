#!/usr/bin/python
'''
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
'''
class Solution:
	# @param s, a string
	# @return a boolean
	def isNumber(self,s):
		i=0
		havepoint=False
		havenum=False
		while(i<len(s) and s[i]==' '):
			i+=1
		if(i<len(s) and (s[i]=='+' or s[i]=='-' )):
			i+=1
		while(i<len(s) and (s[i].isdigit() or s[i]=='.' )):
			if(s[i]=='.'):
				if(havepoint == False):
					havepoint=True
				else:
					return False
			else:
				havenum=True
			i+=1
		if(i<len(s) and s[i].upper()=='E' and havenum==True):
			i+=1
			havepoint=False
			havenum=False
			if(i<len(s) and (s[i] == '+' or s[i]=='-')):
				i+=1
			while(i<len(s) and s[i].isdigit() ):
				havenum=True
				i+=1
		while(i<len(s) and s[i]==' '):
			i+=1
		if(i < len(s) or havenum==False):
			return False
		else:
			return True


	def isNumber1(self, s):
		haveNum=False
		result=True
		havedot=False
		haveE=False
		havespace=False
		haveFlag=False
		for i in range(len(s)):
			if(s[i].isdigit()):
				haveNum=True
				if(havespace==True):
					result=False
					break
			elif(s[i].isalpha()):
				if(s[i].upper()=='E' and haveNum ):
					haveE=True
				else:
					result=False
					break
			elif(s[i]==' '):
				if(haveNum):
					havespace=True
			elif(s[i]=='.'):
				if(havedot==True):
					result=False
					break
				havedot=True
			elif(s[i]=='+' or s[i]=='-'):
				if(haveFlag==True and haveE=='False'):
					result=False
					break
				haveFlag=True
		if(haveNum==False):
			return False
		else:
			return result
        

def test(got, expected):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
	print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	ins=Solution()
	test(ins.isNumber("6e6.5"),False)
	test(ins.isNumber("e9"),False)
	test(ins.isNumber("5e"),False)
	test(ins.isNumber("1."),True)
	test(ins.isNumber("0e"),False)
	test(ins.isNumber(".1"),True)
	test(ins.isNumber(" "),False)
	test(ins.isNumber("."),False)
	test(ins.isNumber("0"),True)
	test(ins.isNumber(" 0.1 "),True)
	test(ins.isNumber("abc"),False)
	test(ins.isNumber("1 a"),False)
	test(ins.isNumber("2e10"),True)

if __name__ == '__main__':
	main()