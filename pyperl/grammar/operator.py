#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from expression import Expression

class Operator(Expression):
    '''Handles all non unary expressions. Encoding each operator
       in its own type is really quite verbose for the purposes
       of this assigmnent.'''
    def __init__(self, row=0, col=0, op=None):
        super(Operator, self).__init__(row=row, col=col)
        self.op = op

    def __repr__(self):
        return self.op
