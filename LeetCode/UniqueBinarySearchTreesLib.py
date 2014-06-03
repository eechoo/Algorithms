#!/usr/bin/python
    # @return an integer
class Unique(object):    
    def numTrees(self,n):
        A=[1,1,2]
        if n <= 2:
            return A[n] 
        for i in range(3,n+1):
            A.append(0)
            for j in range(1,i+1):
                A[i]+=A[j-1]*A[i-j]
        return A[n]