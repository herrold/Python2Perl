#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

def indent(node):
    '''Returns the node indented correctly.'''
    return ' ' * node.col + repr(node)
