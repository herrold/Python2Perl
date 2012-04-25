#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from statement import Statement

class KeywordStmt(Statement):
    '''Implements a valid perl content statement.'''

    def __init__(self, row=0, col=0, keyword='', suffix=';' ):
        super(KeywordStmt, self).__init__(row=row)
        self.keyword = keyword
        self.suffix = suffix
    def __repr__(self):
        return '%s%s' % (self.keyword, self.suffix)
