#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from expression import Expression

class CompareExpr(Expression):
    '''Handles the implementation of perl compare expressions.'''
    def __init__(self, row=0, col=0, left=None, ops=None, comparators=None):
        super(CompareExpr, self).__init__(row=row, col=col)
        self.left = left
        self.ops = ops
        self.comparators = comparators

    def __repr__(self):
        left = repr(self.left)
        ops = map(repr, self.ops)
        comparators = map(repr, self.comparators)
        return ' '.join([left] + ops + comparators)
