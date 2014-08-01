#!/usr/bin/python
'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
DFS
For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
'''
class Solution:
    def combine2(self,n,k,index,solu,result):
        if(len(solu) == k):
            result.append(solu[:])
        else:
            for i in range(index,n+1):
                solu.append(i)
                if(k-len(solu)<=n-i):
                    self.combine2(n,k,i+1,solu,result)
                solu.pop()


    # @return a list of lists of integers
    def combine(self, n, k):
        solu=[]
        result=[]
        self.combine2(n,k,1,solu,result)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.combine(4,2),[])


if __name__ == '__main__':
    main()