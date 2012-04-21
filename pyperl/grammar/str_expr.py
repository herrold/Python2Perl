#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from expression import Expression

class StrExpr(Expression):
    '''
    Handles an basic perl string.
    '''
    def __init__(self, row=0, col=0, s=''):
        super(StrExpr, self).__init__(row=row, col=col)
        self.s = s

    def __repr__(self):
        pass
