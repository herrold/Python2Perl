#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from expression import Expression

class NumExpr(Expression):
    '''Handles all basic numeric expression.'''
    def __init__(self, row=0, col=0, value=None):
        super(NumExpr, self).__init__(row=row, col=col)
        self.value = value

    def __repr__(self):
        return repr(self.value)
