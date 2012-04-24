#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from translator import Translator
from grammar import CallExpr, StrExpr

class Subset0(Translator):
    '''
    Handles all the rewrite rules that relate to subset 0 of the assignment.
    Definition of Subset 0:
    * Print:  ADSL => Print
    * String: ADSL => Str
    '''
    def visit_Print(self, node):
        '''Python to Perl rewrite rules for print.'''
        arguments = [self.visit(value) for value in node.values]
        self.buffer.append(CallExpr(name='print', args=arguments, row=node.lineno))

    def visit_Str(self, node):
        '''Python to Perl rewrite rules for str.'''
        return StrExpr(value=node.s)
