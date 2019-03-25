#!/usr/bin/env python
import sys
import Common

def candyCrush(root):
    """ Candy Crush """
    node = root
    while True:
        last = root
        streak = False
        start = None
        finish = None
        node = last.next
        while node is not None:
            #act = node
            #nxt = node.next
            if last.value != node.value:
                if streak is False:
                    start = last
                    last = node
                    node = node.next
                    continue
                if start is None:
                    root = node
                    break
                start.next = node
                break
            if streak is False:
                streak = True
            if node.next is None:
                start.next = None
                break
            last = node
            node = node.next

        else:
            return root


def main():
    """ Candy Crush invocation """
    # Middle crush case
    #arg = [1, 2, 3, 4, 5, 5, 5, 4, 3, 3, 4, 6]
    # Start Crush case
    #arg = [1, 1, 2, 2, 3, 4]
    # Ending Crush
    arg = [1, 2, 3, 3, 4, 4]
    root = Common.build_linked_list(arg)
    print "Input:"
    Common.print_linked_list(root)
    out = candyCrush(root)
    print "Output:"
    Common.print_linked_list(out)

if __name__ ==  '__main__':
    sys.exit(main())
