#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from translator import Translator
from grammar import PrintStmt, StrExpr

class Subset0(Translator):
    '''
    Handles all the rewrite rules that relate to subset 0 of the assignment.
    Definition of Subset 0:
    * Print:  ADSL => Print
    * String: ADSL => Str
    '''

    def visit_Print(self, node):
        '''Python to Perl rewrite rules for print.'''
        arguments = [self.visit(value) for value in values]
        grammar.PrintStmt(arguments)
        
        # print "print",
        #for value in node.values:
        #    self.visit(value)
        #    print ",",
        # print '"\\n";'

    def visit_Str(self, node):
        '''Python to Perl rewrite rules for str.'''
        return grammar.StrExpr(node.s)
        # print '"%s"' % node.s,

if __name__ == '__main__':
    pass
