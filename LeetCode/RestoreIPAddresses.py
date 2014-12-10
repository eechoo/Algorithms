#!/usr/bin/python
'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''

class Solution:
	def findAddress(self,s,cur,num,result):
		if(num >4 or (num==4 and len(s)>0)):
			return False
		if(len(s)==0 and num == 4 ):
			result.append(cur)
			return True
		for i in range(min(3,len(s))):
			if(s[0]=='0'):
				if(num <3):
					newcur=cur[:]+s[:i+1]+'.'
				else:
					newcur=cur[:]+s[:i+1]
				news=s[i+1:]
				self.findAddress(news,newcur,num+1,result)
				break
			if(int(s[:i+1])<256):
				if(num <3):
					newcur=cur[:]+s[:i+1]+'.'
				else:
					newcur=cur[:]+s[:i+1]
				news=s[i+1:]
				if(self.findAddress(news,newcur,num+1,result) == False):
					continue
			else:
				break

	# @param s, a string
	# @return a list of strings
	def restoreIpAddresses(self, s):
		if(len(s)>12):
			return []
		result=[]
		self.findAddress(s,'',0,result)
		return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
	ins=Solution()
	test(ins.restoreIpAddresses("25525511135"),["255.255.11.135", "255.255.111.35"])
	test(ins.restoreIpAddresses("0000"),["0.0.0.0"])
	test(ins.restoreIpAddresses("010010"),["0.10.0.10","0.100.1.0"])
	test(ins.restoreIpAddresses("101023"),["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"])
if __name__ == '__main__':
    main()