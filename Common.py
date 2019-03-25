#!/usr/bin/env python
"""
Library for common classes and methods for
 - Ternary Trees
 - Single linked list
"""
import sys
# -----   Ternary Tree   -----

class Ternary_node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None

    def have_sons(self):
        if self.left is None and \
            self.middle is None and \
            self.right is None:
            return False
        return True


def build_ternary_tree(arg=None):
    root = Ternary_node(arg[0])
    pool = [root]
    indx = 1
    att = ['left', 'middle', 'right']
    while indx < len(arg):
        act = pool.pop(0)
        #print "act.val = {0}".format(act.value)
        for j in [0,1,2]:
            val = arg[indx+j]
            #print "val, att = {0},{1}".format(val, att[j])
            if val is None:
                continue
            nd = Ternary_node(val)
            setattr(act, att[j], nd)
            pool.append(nd)
        indx += 3
    return root


def print_ternary_tree(root=None):
    print "--- Printing ternary tree ---"
    pool = [root]
    attributes = ['left', 'middle', 'right']
    while pool != []:
        act = pool.pop(0)
        if act.have_sons() is True:
            print "Actual node: {0}".format(act.value)
        for att in attributes:
            nd = getattr(act, att)
            if nd is None:
                continue
            print "{0} : {1}".format(att, nd.value)
            pool.append(nd)
    print "--- Print Done !!! ---"


# -----   Single Linked List   -----


class Linked_node(object):
    """ Linked Node for single linked list """
    def __init__(self, value):
        """ Initialize the object """
        self.value = value
        self.next = None


def build_linked_list(arg=None):
    """ Build a sinle linked list with an array as input """
    root = Linked_node(arg[0])
    node = root
    for indx in xrange(1, len(arg)):
        node.next = Linked_node(arg[indx])
        node = node.next
    return root


def print_linked_list(node):
    """ Print all elements of a single linked list """
    print "--- Printing Single linked List ---"
    sys.stdout.write("[ ")
    i = 0
    while node is not None:
        i += 1
        #print "Node: {0}".format(node.value)
        sys.stdout.write("{0}".format(node.value))
        node = node.next
        if node is not None:
            sys.stdout.write(", ")
        if i % 20 == 0:
            sys.stdout.write("\n")
    sys.stdout.write("]\n")
    print "--- Print Done !!! ---"

#EOF
