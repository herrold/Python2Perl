#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from statement import Statement

class PrintStmt(Statement):
    '''
    Defines a print statment in perl.
    '''
    def __init__(self, row=0, col=0, args=[]):
        super(PrintStat, self).__init__(row=row, col=col)
        self.args = args

    def __repr__(self):
        pass
