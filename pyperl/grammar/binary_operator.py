#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from expression import Expression

class BinaryOperator(Expression):
    '''Implements binary operators for python.'''
    def __init__(self, row=0, col=0, op=None, left=None, right=None):
        super(BinaryOperator, self).__init__(row=row, col=col)
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return '%s %s %s' % (repr(self.left), repr(self.op), repr(self.right))
