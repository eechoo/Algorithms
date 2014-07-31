#!/usr/bin/python
#Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#DFS
class Solution:
    def combine2(self,n,k,level,solu,result):
        if(level == k):
            result.append(solu)
            return result
        for i in range(level,n):
            solu.append(i)
            self.combine2(n-i-1,k,level,solu,result)


    # @return a list of lists of integers
    def combine(self, n, k):
        solu=[]
        result=[]
        result=self.combine2(n,k,1,solu,result)
        return result


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.generateParenthesis(1),['()'])
    test(ins.generateParenthesis(2),['(())','()()'])
    test(ins.generateParenthesis(3),['((()))','(()())','(())()','()(())','()()()'])


if __name__ == '__main__':
    main()