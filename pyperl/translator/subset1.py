#!/usr/bin/env python
# Benjamin James Wright (bwright@cse.unsw.edu.au)
# 2012.04.18 (ISO 8601)

from subset0 import Subset0
from grammar import AssignStmt, NameExpr, NumExpr, Operator, UnaryOperator, BinaryOperator, PerlType, Expression, ArrayExpr, HashMapExpr, CallExpr

class Subset1(Subset0):
    '''
    This implements all the features required in subset 1.
    Specification of Subset 1:
    ADSL => Assign: Universal rewrite for assignments.
    ADSL => Name:   Universal rewrites for identifiers.
    ADSL => UnaryOp: Universally rewrites all unary operators.
    ADSL => BinOp:  Univeral rewrites for all binary operators.
    ADSL => Add:    Universal rewrites for all add operators.
    ADSL => Sub:    Universal rewrites for all subtraction operators.
    ADSL => UAdd:   Universally rewrites unary addition.
    ADSL => USub:   Universallsy rewrites unary subtraction
    ADSL => Mult:   Universal rewrites for all division operators.
    ADSL => Div:    Universal rewrites for all divison operators.
    ADSL => Mod:    Univeral rewrite for all modulus operators
    ADSL => Pow:    Universal rewrites for all power operators.
    '''
    def visit_Assign(self, node):
        '''
        Collects all the targets for the assigment and the corresponding
        values and builds a perl assignment statement. It also updates
        the global context of the type of the current identifier. An
        identifier can be changed at multiple points in the program and
        perl uses a special prefix notation to indicate its "type" so to
        preserve that we need to maintain context!
        '''
        # Find the value for the program.
        value =  self.visit(node.value)

        # Find the first target. Note it will have to be parsed twice.
        target = self.visit(node.targets[0])
        
        # Assign the target prefix, based on the value.
        if isinstance(value, NameExpr):
            self.context[target.name] = self.context[value.name]
        elif isinstance(value, Expression) and value.perl_type:
            self.context[target.name] = value.perl_type
        else:
            self.context[target.name] = PerlType.SCALAR

        # Special case for open
        if isinstance(value, CallExpr) and value.name == 'open':
            self.context[target.name] = PerlType.SCALAR
            target.prefix = 'my ' + self.context[target.name]
            value.args = [target] + value.args
            value.suffix = ''' or die "No such file or directory: '%s'";''' % value.args[1].value
            return value

        # Refresh the first target now its context has been parsed (>.<)
        target = self.visit(node.targets[0])
        
        # Check if the node has an operator
        op = Operator(op='')
        if 'op' in dir(node):
            op = self.visit(node.op)

        return AssignStmt(prefix='my', target=target, value=value, op=op,
                          row=node.lineno, col=node.col_offset)

    def visit_AugAssign(self, node):
        '''
        Implements assignments such as += etc. This was not actually
        required in the solution. I just wanted to do it.
        '''
        # Modify a component.
        node.targets = [node.target]
        return self.visit_Assign(node)

    def visit_Name(self, node):
        '''
        Retrieves the node id from the python name and creates a
        perl name expression from it. Note name is contextual (see assign).
        '''
        # Python has certain reserved names, this handles them as special
        # cases. Bools do not really exist in perl so numbers are
        # sort of a defacto replacements (C like).
        dispatch = { 'True': NumExpr(value=1,
                                     row=node.lineno, col=node.col_offset),
                     'False': NumExpr(value=0,
                                      row=node.lineno, col=node.col_offset)
                   }
        # Check if the key is in the dispatch.
        if node.id in dispatch.keys():
            return dispatch[node.id]
        # Else use the global type context (we actually have a context parser)
        # to assign a valid prefix at this point in the program (>^_^)>
        return NameExpr(name=node.id, prefix=self.context[node.id],
                        row=node.lineno, col=node.col_offset)

    def visit_Num(self, node):
        '''
        Takes the number component of a python number and converts it into
        a perl number expression.
        '''
        return NumExpr(value=node.n, row=node.lineno, col=node.col_offset)

    def visit_UnaryOp(self, node):
        '''
        Visits the unary operation and then visits the operand which the
        action will be applied to. 
        '''
        op = self.visit(node.op)
        operand = self.visit(node.operand)
        return UnaryOperator(op=op, operand=operand,
                             row=node.lineno, col=node.col_offset)

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

    def visit_UAdd(self, node):
        '''
        Directly converts the unary operator for addition to perl.
        '''
        return Operator(op='+')

    def visit_Add(self, node):
        '''
        Directly converts a python add operator to a perl add operator.
        Note these rewrite to exactly the same thing.
        '''
        return Operator(op='+')

    def visit_USub(self, node):
        '''
        Directly converts the unary operator for subtraction to perl.
        '''
        return Operator(op='-')

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
