#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from operator import Operator

class ComparisonOperator(Operator):
    '''Just adds a type to seperate arithmetic from comparison operators.'''
    def __init__(self, row=0, col=0, op=None):
        super(ComparisonOperator, self).__init__(row=row, col=col, op=op)
