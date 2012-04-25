#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from translator import Translator
from grammar import CallExpr, StrExpr

class Subset0(Translator):
    '''
    Handles all the rewrite rules that relate to subset 0 of the assignment.
    Definition of Subset 0:
    * Module: ADSL => Module -- Deals with the global scope.
    * Print:  ADSL => Print  -- Deals with print statements universally.
    * String: ADSL => Str    -- Deals with string literals universally.
    '''

    def visit_Module(self, node):
        '''
        For the purposes of this translator the module is the "global" scope
        therefore it makes sense for it to be the "root" node of our newly
        constructed buffer or perl abstract syntax tree. DFSing this tree
        will give you the source code to a perl program.
        '''
        module = [self.visit(grammar) for grammar in node.body]
        # module.sort(key=lambda grammar: grammar.row)
        self.module = self.module + module

    def visit_Print(self, node):
        '''Python to Perl rewrite rules for print.'''
        arguments = [self.visit(value) for value in node.values]
        arguments.append(StrExpr(value=r"\n"))
        return CallExpr(name='print', args=arguments, row=node.lineno, col=node.col_offset)

    def visit_Str(self, node):
        '''Python to Perl rewrite rules for str.'''
        return StrExpr(value=node.s, row=node.lineno, col=node.col_offset)
