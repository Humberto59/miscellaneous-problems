#!/usr/bin/env python
import sys

def candyCrush(arg):
    """ Candy Crush """
    while True:
        _len = len(arg)
        last = None
        streak = False
        start = None
        finish = None
        for indx in xrange(_len):
            val = arg[indx]
            if last != val:
                if streak is False:
                    last = val
                    continue
                arg = arg[:start] + arg[indx:]
                break
            if streak is False:
                streak = True
                start = indx - 1
            finish = indx
        else:
            return arg

def main():
    """ Candy Crush invocation """
    arg = [1, 2, 3, 4, 5, 5, 5, 4, 3, 3, 4, 6]
    print "Input: {0}".format(arg)
    out = candyCrush(arg)
    print "Output {0}".format(out)

if __name__ ==  '__main__':
    sys.exit(main())
