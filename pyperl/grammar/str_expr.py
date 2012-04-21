#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from expression import Expression

class StrExpr(Expression):
    '''
    Handles the implementation of a perl basic string.
    '''
    def __init__(self, row=0, col=0, s=''):
        super(StrExpr, self).__init__(row=row, col=col)
        self.s = s
    def __repr__(self):
        return '"%s"' % self.s

if __name__ == '__main__':
    node = StrExpr(s=r"\n")
    print(repr(node))
