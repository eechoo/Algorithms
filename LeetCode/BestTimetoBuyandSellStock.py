#!/usr/bin/python
#Say you have an array for which the ith element is the price of a given stock on day i.

#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	benifit=0
    	curbenifit=0
    	if(prices == []):
    		return benifit
    	for i in range(1,len(prices)):
    		curbenifit+=prices[i]-prices[i-1]
    		if(curbenifit<0):
    			curbenifit=0
    		if(benifit < curbenifit):
    			benifit=curbenifit
    	return benifit

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.maxProfit([1,2,3]),2)
    test(ins.maxProfit([3,2,1]),0)
    test(ins.maxProfit([1,4,2]),3)


if __name__ == '__main__':
    main()