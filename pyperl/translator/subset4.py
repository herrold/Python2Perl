#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset3 import Subset3 
from grammar import ArrayExpr, HashMapExpr, SubscriptExpr

class Subset4(Subset3):
    '''
    Implemets all that is required from subset 4.
    '''
    def visit_Expr(self, node):
        '''
        Handles all basic expressions.
        '''
        value = self.visit(node.value)
        if 'suffix' in dir(value):
            value.suffix = ';'
        return value

    def visit_List(self, node):
        '''
        Implements python lists in perl.
        '''
        args = [self.visit(elem) for elem in node.elts]
        return ArrayExpr(args=args)
    
    def visit_Dict(self, node):
        '''
        Implements python dictionarys in perl.
        '''
        keys = [self.visit(key) for key in node.keys]
        values = [self.visit(value) for value in node.values]
        
        return HashMapExpr(args=zip(keys, values))

    def visit_Subscript(self, node):
        value = self.visit(node.value)
        slice = self.visit(node.slice)
        return SubscriptExpr(name=value, slice=slice, row=node.lineno, col=node.col_offset)
            
    def visit_Index(self, node):
        value = self.visit(node.value)
        return value
