#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from statement import Statement
from operator import Operator

class AssignStmt(Statement):
    ''' Implements a perl assignment statement.'''
    def __init__(self, prefix='', row=0, col=0, target=None, value=None, sep=';', op=Operator(op='')):
        super(AssignStmt, self).__init__(row=row, col=col, sep=sep, prefix=prefix)
        self.target = target
        self.value = value
        self.op = op

    def __repr__(self):
        return self.prefix + ' ' +repr(self.target) + ' %s= ' % repr(self.op) + repr(self.value) + self.sep
