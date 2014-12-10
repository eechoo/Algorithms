#!/usr/bin/python
'''
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive.
'''

class Solution:
    def getPermutation1(self,list,k,result):
        if(list==[]):
            k-=1
            return k
        for i in range(len(list)):
            sum=1
            for j in range(1,len(list)):
                sum*=j
            if(sum < k):
                k-=sum
                continue
            result.append(list[i])
            k=self.getPermutation1(list[:i]+list[i+1:],k,result)
            if(k==0):
                return k
            result.pop()
        return k

    # @return a string
    def getPermutation(self, n, k):
        if(n==0 or k==0):
            return ''
        sum=1
        for i in range(1,n+1):
            sum*=i
        if(sum < k):
            return ''
        list=[str(i) for i in range(1,n+1)]
        result=[]
        self.getPermutation1(list,k,result)
        result.append('')
        return ''.join(result)
        

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.getPermutation(1,1),'1')
    test(ins.getPermutation(3,3),'213')


if __name__ == '__main__':
    main()