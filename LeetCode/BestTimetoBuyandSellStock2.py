#!/usr/bin/python
#Say you have an array for which the ith element is the price of a given stock on day i.

#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if(prices==[]):
            return 0
        benifit=0
        for i in range(0,len(prices)-1):
            if((prices[i+1]-prices[i])>0):
                benifit+=prices[i+1]-prices[i]
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