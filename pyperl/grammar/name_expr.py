#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from expression import Expression

class NameExpr(Expression):
    '''Handles all basic numeric expression.'''
    def __init__(self, row=0, col=0, name=None):
        super(NameExpr, self).__init__(row=row, col=col)
        self.name = name    

    def __repr__(self):
        return "$%s" % self.name
