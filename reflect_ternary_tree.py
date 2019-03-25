#!/usr/bin/env python
import sys
import Common

def traverse(root):
    if root == None:
        return root
    left = traverse(root.left)
    mid = traverse(root.middle)
    rigth = traverse(root.right)

    tmp = left
    root.left = root.right
    root.right = tmp
    #print "root = '{0}'".format(root.value)
    return root

def main():
    """ Main """
    arg = [1,2,3,4,5,6,7,None,8,None,9,10,11]
    root = Common.build_ternary_tree(arg)
    Common.print_ternary_tree(root)
    traverse(root)
    Common.print_ternary_tree(root)


if __name__ == '__main__':
    sys.exit(main())
