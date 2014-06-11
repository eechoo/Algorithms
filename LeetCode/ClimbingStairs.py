#!/usr/bin/python
#You are climbing a stair case. It takes n steps to reach to the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Climb(object): 
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if(n == 0):
            return 0
        if(n==1):
            return 1
        if(n==2):
            return 2;
        A=[0,1,2]
        for i in range(3,n+1):
            A.append(A[i-2]+A[i-1])
        return A[n]


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Climb()
    test(ins.climbStairs(1),1)
    test(ins.climbStairs(2),2)
    test(ins.climbStairs(4),5)

if __name__ == '__main__':
    main()