#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset4 import Subset4
from grammar import NameExpr, FunctionDefStmt, ReturnStmt

class Subset5(Subset4):
    '''
    Implements everything in subset 5.
    '''
    def visit_FunctionDef(self, node):
        '''
        Defines rewrite rules for a function definition.
        '''
        name = node.name
        args = self.visit(node.args)
        body = [self.visit(elem) for elem in node.body]
        return FunctionDefStmt(name=name, args=args, body=body) 
    
    def visit_arguments(self, node):
        '''
        Parses argument functions.
        '''
        args = [self.visit(arg) for arg in node.args]
        return args 
    def visit_Return(self, node):
        '''
        Parses argument returns.
        '''
        value = self.visit(node.value)
        return value
