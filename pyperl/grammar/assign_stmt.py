#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from statement import Statement

class AssignStmt(Statement):
    ''' Implements a perl assignment statement.'''
    def __init__(self, prefix='', row=0, col=0, target=None, value=None, sep=';'):
        super(AssignStmt, self).__init__(row=row, col=col, sep=sep, prefix=prefix)
        self.target = target
        self.value = value

    def __repr__(self):
        return self.prefix + ' ' +repr(self.target) + ' = ' + repr(self.value) + self.sep
