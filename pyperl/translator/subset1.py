#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset0 import Subset0
from grammar import AssignStmt, NameExpr, NumExpr, Operator, BinaryOperator

class Subset1(Subset0):
    '''
    This implements all the features required in subset 1.
    Specification of Subset 1:
    ADSL => Assign: Universal rewrite for assignments.
    ADSL => Name:   Universal rewrites for identifiers.
    ADSL => BinOp:  Univeral rewrites for all binary operators.
    ADSL => Add:    Universal rewrites for all add operators.
    ADSL => Sub:    Universal rewrites for all subtraction operators.
    ADSL => UAdd:   TODO
    ADSL => USub:   TODO
    ADSL => Mult:   Universal rewrites for all division operators.
    ADSL => Div:    Universal rewrites for all divison operators.
    ADSL => Mod:    Univeral rewrite for all modulus operators
    ADSL => Pow:    Universal rewrites for all power operators.
    '''
    def visit_Assign(self, node):
        '''
        Collects all the targets for the assigment and the corresponding
        values and builds a perl assignment statement.
        '''
        # Find all the targets.
        targets = [self.visit(target) for target in node.targets]
        # Find the value for the program.
        value =  self.visit(node.value)
        return AssignStmt(prefix='my', target=targets[0], value=value,
                          row=node.lineno, col=node.col_offset)

    def visit_Name(self, node):
        '''
        Retrieves the node id from the python name and creates a
        perl name expression from it. Note name is contextual (see assign).
        '''
        return NameExpr(name=node.id, row=node.lineno, col=node.col_offset)

    def visit_Num(self, node):
        '''
        Takes the number component of a python number and converts it into
        a perl number expression.
        '''
        return NumExpr(value=node.n, row=node.lineno, col=node.col_offset)
 
    def visit_BinOp(self, node):
        '''
        Visits the operator of the binary operation then the left and the
        right of the operation (note these can also be binary operations).
        It then constructs the corresponding perl binary operator.
        '''
        # Visit the operator for this binary operation.
        op = self.visit(node.op)
        # Visit the left hand side of this operation.
        left = self.visit(node.left)
        # Visit the right hand side of this operation.
        right = self.visit(node.right)
        # Generate a perl binary operator from this information.
        return BinaryOperator(op=op, left=left, right=right,
                              row=node.lineno, col=node.col_offset)

    def visit_Add(self, node):
        '''
        Directly converts a python add operator to a perl add operator.
        Note these rewrite to exactly the same thing.
        '''
        return Operator(op='+')

    def visit_Sub(self, node):
        '''
        Directly converts a python subtraction operator to a perl add operator.
        Note these rewrite to exactly the same thing.
        '''
        return Operator(op='-')

    def visit_Mult(self, node):
        '''
        Directly converts a python multiplication operator to a perl add operator.
        Note these rewrite to exactly the same thing.
        '''
        return Operator(op='*')

    def visit_Div(self, node):
        '''
        Directly converts a python division operator to a perl add operator.
        Note these rewrite to exactly the same thing.
        '''
        return Operator(op='/')

    def visit_Mod(self, node):
        '''
        Directly converts a python modulus operator to a perl add operator.
        Note these rewrite to exactly the same thing.
        '''
        return Operator(op='%')

    def visit_Pow(self, node):
        '''
        Directly converts a python power operator to a perl add operator.
        Note these rewrite to exactly the same thing.
        '''
        return Operator(op='**')
