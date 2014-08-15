#!/usr/bin/python
'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a  b  c  d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
'''

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
    	if(num == [] or len(num) < 4):
    		return []
    	num.sort()
    	result=[]
    	for first in range(len(num)-3):
            if(first>0 and num[first] == num[first-1]):
                continue
            for second in range(first+1,len(num)-2):
                if(second>first+1 and num[second] == num[second-1]):
                    continue
                third=second+1
                forth=len(num)-1
                while(third < forth):
                    if(third > second+1 and num[third]==num[third-1]):
    				    third+=1
    				    continue
                    if(forth < len(num)-1 and num[forth]==num[forth+1]):
    				    forth-=1
    				    continue
                    sum=num[first]+num[second]+num[third]+num[forth]
#                    print 'sum=%d,first=%d,second=%d,third=%d,forth=%d' % (sum,first,second,third,forth)
                    if(sum == target):
    				    result.append([num[first],num[second],num[third],num[forth]])
                    if(sum > target):
    				    forth-=1
                    else:
    				    third+=1
    	return result

    def fourSum1(self, num, target):
        if(num == [] or len(num) < 4):
            return []
        numhash={}
        num.sort()
        result=[]
        for i in range(len(num)-1):
            for j in range(i+1,len(num)):
                key=num[i]+num[j]
                if(numhash.has_key(key)):
                    numhash[key].append([i,j])
                else:
                    numhash[key]=[[i,j]]
        for first in range(len(num)-1):
            if(first>0 and num[first]==num[first-1]):
                continue
            for second in range(first+1,len(num)):
                if(second>first+1 and num[second]==num[second-1]):
                    continue 
                key=target-num[first]-num[second]
                if(numhash.has_key(key)):
                    for j in range(len(numhash[key])):
                        third,forth=numhash[key][j]
                        if(second < third ):
                            if(result == [] or result[-1]!=[num[first],num[second],num[third],num[forth]]):
                                result.append([num[first],num[second],num[third],num[forth]])
                            print 'key=%d,first=%d,second=%d,third=%d,forth=%d' % (key,first,second,third,forth)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    A=[-491,-486,-481,-479,-463,-453,-405,-393,-388,-385,-381,-380,-347,-340,-334,-333,-326,-325,-321,-321,-318,-317,-269,-261,-252,-241,-233,-231,-209,-203,-203,-196,-187,-181,-169,-158,-138,-120,-111,-92,-86,-74,-33,-14,-13,-10,-5,-1,8,32,48,73,80,82,84,85,92,134,153,163,192,199,199,206,206,217,232,249,258,326,329,341,343,345,363,378,399,409,428,431,447,449,455,476,493]
#    test(ins.fourSum([1,0,-1,0,-2,2],0),[])
#    test(ins.fourSum1([1,0,-1,0,-2,2],0),[])
    test(ins.fourSum1([-3,-2,-1,0,0,1,2,3],0),[])
#    test(ins.fourSum1(A,2328),[])


if __name__ == '__main__':
    main()