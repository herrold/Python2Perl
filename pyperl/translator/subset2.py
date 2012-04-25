#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset1 import Subset1
from grammar import ComparisonOperator, Operator, CompareExpr, IfStmt, KeywordStmt

class Subset2(Subset1):
    '''Implements subset 2 of the assignment.
    Subset 2 Specification
    ADSL => LShift: 
    ADSL => RShift:
    ADSL => BitOr:
    ADSL => BitXor:
    ADSL => BitAnd:
    ADSL => Invert:
    ADSL => And:
    ADSL => Or:
    ADSL => Eq:
    ADSL => NotEq:
    ADSL => Lt:
    ADSL => LtE:
    ADSL => Gt:
    ADSL => GtE:
    ADSL => Break:
    ADSL => Continue:
    ADSL => For:
    ADSL => While
    ADSL => If:
    ADSL => Compare:
    '''
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
        '''
        Translates a python equality comparison operator into a perl equality
        comparison operator.
        '''
        return ComparisonOperator(op='==')
    def visit_NotEq(self, node):
        '''
        Translates a not equal python comparison operator into a perl not equal
        comparison operator.
        '''
        return ComparisonOperator(op='!=')
    def visit_Lt(self, node):
        '''
        Translates a python less than comparison operator into a perl
        less than comparison operator.
        '''
        return ComparisonOperator(op='<')
    def visit_LtE(self, node):
        '''
        Translates a python less than or equal comparison operator into a perl
        less then or equal comparison operator.
        '''
        return ComparisonOperator(op='<=')
    def visit_Gt(self, node):
        '''
        Translates a python greater than comparison operator into a perl
        greater than comparison operator.
        '''
        return ComparisonOperator(op='>')
    def visit_GtE(self, node):
        '''
        Translates a python greater than or equal comparison operator into
        a perl greater than or equal comparison operator.
        '''
        return ComparisonOperator(op='>=')
    def visit_Break(self, node):
        '''
        Translates a python break keyword statement into a perl last 
        keyword statment.
        ''' 
        return KeywordStmt(keyword='last',
                           row=node.lineno, col=node.col_offset)
    def visit_Continue(self, node):
        '''
        Translates a python continue keyword statement into a perl
        keyword statment.
        ''' 
        return KeywordStmt(keyword='continue',
                           row=node.lineno, col=node.col_offset)
    '''
    def visit_For(self, node):
    def visit_While(self, node):
    '''
    def visit_If(self, node):
        '''
        An if statment represents a python block that can contain its
        own "code block" of children nodes. By visiting the test we
        can construct a CompareExpr and then pass the body and potentially
        else and or elif statments to a wider IfStmt. An IfStmt can also
        contain multiple other IfStmts etc.
        '''
        # Visit the test condition for the if statment.
        test = self.visit(node.test)
        # Visit the body of the block.
        body = [self.visit(element) for element in node.body]
        # Visit the body of the orelse (potentially another if statement.)
        orelse = [self.visit(element) for element in node.orelse]
        # Construct a perl if statment from the result.
        return IfStmt(test=test, body=body, orelse=orelse,
                      row=node.lineno, col=node.col_offset)

    def visit_Compare(self, node):
        '''
        A compare expression relates to any expression which resolves to
        a boolean result. This rewrites any python comparison expression
        into an equivelant perl compare expression via the CompareExpr
        grammar.
        '''
        # Visit the operators used in the compare expression.
        ops = [self.visit(op) for op in node.ops]
        # Visit the comparators in the compare expression.
        comparators = [self.visit(comp) for comp in node.comparators]
        # Visit the left hand side of the comparison expression.
        left = self.visit(node.left)
        # Construct a perl comparison expression from the result.
        return CompareExpr(ops=ops, comparators=comparators, left=left)
