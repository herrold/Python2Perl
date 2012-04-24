#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset0 import Subset0
from grammar import AssignStmt, NameExpr, NumExpr, Operator, BinaryOperator

class Subset1(Subset0):
    '''This implements all the features required in subset 1'''
    def visit_Assign(self, node):
        # Find all the targets.
        targets = [self.visit(target) for target in node.targets]
        # Find the value for the program.
        value =  self.visit(node.value)
        self.buffer.append(AssignStmt(target=targets[0],value=value))

    def visit_Name(self, node):
        return NameExpr(name=node.id)

    def visit_Num(self, node):
        return NumExpr(value=node.n)
 
    def visit_BinOp(self, node):
        op = self.visit(node.op)
        left = self.visit(node.left)
        right = self.visit(node.right)
        return BinaryOperator(op=op, left=left, right=right)

    def visit_Add(self, node):
        return Operator(op='+')

    def visit_Sub(self, node):
        return Operator(op='-')

    def visit_Mult(self, node):
        return Operator(op='*')

    def visit_Div(self, node):
        return Operator(op='/')

    def visit_Mod(self, node):
        return Operator(op='%')

    def visit_Pow(self, node):
        return Operator(op='**')
