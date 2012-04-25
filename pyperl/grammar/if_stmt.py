#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from control_flow_stmt import ControlFlowStmt

class IfStmt(ControlFlowStmt):
    '''Implements perl if statements'''

    def __init__(self, row=0, col=0, test=None, body=None, orelse=None):
        super(IfStmt, self).__init__(row=row, col=col, keyword='if',
                                     condition=test, body=body, orelse=orelse)
        self.test = test
        self.body = body
        self.orelse = orelse
