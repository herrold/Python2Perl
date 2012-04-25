#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset3 import Subset3 
from grammar import ArrayExpr, HashMapExpr

class Subset4(Subset3):
    '''
    Implemets all that is required from subset 4.
    '''
    def visit_List(self, node): 
        args = [self.visit(elem) for elem in node.elts]
        return ArrayExpr(args=args)
    def visit_Dict(self, node):
        keys = [self.visit(key) for key in node.keys]
        values = [self.visit(value) for value in node.values]
        
        return HashMapExpr(args=zip(keys, values))
