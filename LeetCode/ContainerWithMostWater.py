#!/usr/bin/python

#Given n non-negative integers a1, a2, ..., an, 
#where each represents a point at coordinate (i, ai). 
#n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
#Find two lines, which together with x-axis forms a container, such that the container contains the most water.

#Note: You may not slant the container.

class Solution:
	def min(self,a,b):
		if(a > b):
			return b
		else:
			return a

    # @return an integer
	def maxArea(self, height):
		if(height == []):
			return 0
		square,left,right=0,0,len(height)-1
		while(left <right):
			tmp=self.min(height[left],height[right])*(right-left)
			if(square < tmp):
				square=tmp
			if( height[left] < height[right]):
				left+=1
			else:
				right-=1
		return square

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.maxArea([1,2]),1)
    test(ins.maxArea([1,3,1,4,1]),6)


if __name__ == '__main__':
    main()