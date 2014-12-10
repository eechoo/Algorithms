#!/usr/bin/python
'''
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
'''
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
    	if(intervals ==[]):
    		return []
    	intervals.sort(lambda x,y : cmp(x.start,y.start))
    	length=len(intervals)
    	i=1
    	while(i<length):
    		if(intervals[i].start<=intervals[i-1].end):
    			if(intervals[i].end > intervals[i-1].end):
    				intervals[i-1].end=intervals[i].end
    			intervals.pop(i)
    			length=len(intervals)
    		else:
    			i+=1
    	return intervals



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    node1=Interval(1,4)
    node2=Interval(0,4)
    intervals=[[1,4],[1,4]]
#    test(ins.merge([[1,3],[2,6],[8,10],[15,18]]),[[1,6],[8,10],[15,18]])
    intv=node1.merge([node1,node2])
    print intv[0].end

if __name__ == '__main__':
    main()