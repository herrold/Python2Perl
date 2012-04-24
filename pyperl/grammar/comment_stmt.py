#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from statement import Statement

class CommentStmt(Statement):
    '''Implements a valid perl content statement.'''

    def __init__(self, row=0, col=0, value=''):
        super(CommentStmt, self).__init__(row=row, col=col)
        self.value = value
    
    def __repr__(self):
        return '#%s' % self.value 
