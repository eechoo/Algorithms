#!/usr/bin/python
import UniqueBinarySearchTreesLib 

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    ins=UniqueBinarySearchTreesLib.Unique()
    test(ins.numTrees(3),5)
    test(ins.numTrees(4),14)
    test(ins.numTrees(5),42)
    test(ins.numTrees(1),1)
    test(ins.numTrees(2),2)

if __name__ == '__main__':
    main()
