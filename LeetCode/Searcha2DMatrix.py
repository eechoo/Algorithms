#!/usr/bin/python
#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#Integers in each row are sorted from left to right.
#The first integer of each row is greater than the last integer of the previous row.
#For example,

#Consider the following matrix:

#[
#  [1,   3,  5,  7],
# [10, 11, 16, 20],
# [23, 30, 34, 50]
#]
#Given target = 3, return true.

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        n=len(matrix)
        print matrix
        m=len(matrix[0])
        if(n == 1):
            if(m == 0):
                return False
            if(target == matrix[0][m/2]):
                return True
            elif(target > matrix[0][m/2]):
                return self.searchMatrix([matrix[0][m/2+1:]],target)
            else:
                return self.searchMatrix([matrix[0][:m/2]],target)
        elif(n > 1):
            if(target == matrix[n/2][0]):
                return True
            elif(target > matrix[n/2][0]):
                return self.searchMatrix(matrix[n/2:],target)
            else:
                return self.searchMatrix(matrix[:n/2],target)
        return False



def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=Solution()
    test(ins.searchMatrix([[0,1]],1),True)
    test(ins.searchMatrix([[2,4,7,9],[13,17,19],[25,26,30]],31),False)
    test(ins.searchMatrix([[2,4,7,9],[13,17,19],[25,26,30]],1),False)
    test(ins.searchMatrix([[2,4,7,9],[13,17,19],[25,26,30]],7),True)
    test(ins.searchMatrix([[1,3]],1),True)

if __name__ == '__main__':
    main()