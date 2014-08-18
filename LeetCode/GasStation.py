#!/usr/bin/python
'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
    	if(gas == []  or cost == []):
    		return 0
    	buffer=0
    	total=0
    	start = -1
    	for i in range(len(gas)):
    		buffer=gas[i]-cost[i]+buffer
    		total+=gas[i]-cost[i]
    		if(buffer < 0):
    			start=i+1
    			buffer=0
    	if(total >=0):
    		return start
    	else:
    		return -1
        

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.canCompleteCircuit([1,2,3],[2,1,3]),2)


if __name__ == '__main__':
    main()