#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset2 import Subset2

class Subset3(Subset2):
    '''
    Implements the requirements of subset 3.
    '''
    def visit_Call(self, node):
        '''
        A call represents any call to  a function. The standard library
        is quite large and we cannot convert it all so we do it on a case by
        case basis.
        '''
        func = self.visit(node.func)
        args = [self.visit(arg) for arg in node.args]
        print func, args

