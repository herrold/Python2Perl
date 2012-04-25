#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset1 import Subset1
from grammar import ComparisonOperator, Operator, CompareExpr, IfStmt

class Subset2(Subset1):
    '''Implements subset 2 of the assignment.'''
    '''
    def visit_LShift(self, node):
        return Operator(op='<<')
    def visit_RShift(self, node):
        return Operator(op='>>')
    def visit_BitOr(self, node):
        return Operator(op='|')
    def visit_BitXor(self, node):
        return Operator(op='~')
    def visit_BitAnd(self, node):
        return Operator(op='&')
    def visit_Invert(self, node):
        return Operator(op='')
    def visit_And(self, node):
        return Comparisonperator(op='&&')
    def visit_Or(self, node):
        return ComparisonOperator(op='||')
    '''
    def visit_Eq(self, node):
        return ComparisonOperator(op='==')
    def visit_NotEq(self, node):
        return ComparisonOperator(op='!=')
    def visit_Lt(self, node):
        return ComparisonOperator(op='<')
    def visit_LtE(self, node):
        return ComparisonOperator(op='<=')
    def visit_Gt(self, node):
        return ComparisonOperator(op='>')
    def visit_GtE(self, node):
        return ComparisonOperator(op='>=')
    '''
    def visit_Break(self, node):
    def visit_Continue(self, node):
    def visit_For(self, node):
    def visit_While(self, node):
    '''
    def visit_If(self, node):
        '''Defines the rewrite between a python if and a perl if.'''
        test = self.visit(node.test)
        body = [self.visit(element) for element in node.body]
        orelse = [self.visit(element) for element in node.orelse]
        return IfStmt(test=test, body=body, orelse=orelse, row=node.lineno,
                      col=node.col_offset)

    def visit_Compare(self, node):
        '''Defines the rewrite between a python cmp and a perl cmp.'''
        ops = [self.visit(op) for op in node.ops]
        comparators = [self.visit(comp) for comp in node.comparators]
        left = self.visit(node.left)
        return CompareExpr(ops=ops, comparators=comparators, left=left)
