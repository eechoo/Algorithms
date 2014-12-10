#!/usr/bin/python
'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

#Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
    	if(intervals ==[]):
    		return [newInterval]
    	result=[]
    	for i in intervals:
    		if(i.end<newInterval.start or i.start >newInterval.end):
    			result.append(i)
    		else:
    			if(i.start<newInterval.start):
    				newInterval.start=i.start
    			if(i.end > newInterval.end):
    				newInterval.end=i.end
    	result.append(newInterval)
    	result.sort(lambda x,y : cmp(x.start,y.start))
    	return result
        
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    node1=Interval(1,3)
    node2=Interval(6,9)
    node3=Interval(2,5)
    result=node1.insert([node1],node3)
    for i in result:
    	print '%d,%d' % (i.start,i.end)

if __name__ == '__main__':
    main()