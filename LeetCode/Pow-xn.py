#!/usr/bin/python

class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
    	if(n==0):
    		return 1.0
    	if(n<0):
    		return 1.0/self.pow(x,-n)
    	return x*self.pow(x,n-1)

    def pow(self,x,n):
    	if(n==0):
            return 1.0;  
        if(n<0):  
            return 1.0/pow(x,-n);  
        half = pow(x,n>>1);  
        if(n%2==0):  
            return half*half;  
        else:  
            return half*half*x; 

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.pow(2,2),['()'])


if __name__ == '__main__':
    main()