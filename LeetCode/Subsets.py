#!/usr/bin/python
'''
DFS
Given a set of distinct integers, S, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]'''

class Solution:
    def subsets2(self,S,level,solu,result):
      if(len(solu)==level):
        result.append(solu[:])
      else:
#        for i in range(len(S)-1,-1,-1):
        for i in range(len(S)):
          solu.append(S[i])
          self.subsets2(S[i+1:],level,solu,result)
          solu.pop()

    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
      result=[]
      solu=[]
      if(S==[]):
        return []
      else:
        S.sort()
        for i in range(len(S)+1):
          self.subsets2(S,i,solu,result)
      return result

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.subsets([1,2]),[[1],[]])



if __name__ == '__main__':
    main()